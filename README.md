# Monitoramento de Queimadas na Amazônia

Este projeto tem como objetivo monitorar as queimadas na Amazônia e apresentar informações diárias atualizadas sobre os focos de incêndio detectados. Abaixo, você pode visualizar as queimadas mais recentes, com detalhes sobre localização, satélite que realizou a detecção, e outros fatores relevantes.

## Estrutura dos Dados

Cada entrada na tabela representa um foco de incêndio com as seguintes informações:

- **ID:** Identificador único do foco de incêndio.
- **Latitude/Longitude:** Coordenadas geográficas do foco detectado. Para visualizar o local exato, insira estas coordenadas no Google Maps ou outro aplicativo de mapas.
- **Data/Hora GMT:** Data e hora da detecção em formato GMT (Greenwich Mean Time).
- **Satélite:** Satélite responsável pela detecção do foco de incêndio.
- **Município, Estado e País:** Localização administrativa do foco detectado.
- **Dias sem Chuva:** Número de dias consecutivos sem precipitação na região, o que pode indicar um aumento no risco de incêndio.
- **Precipitação:** Quantidade de chuva (em milímetros) registrada no local.
- **Risco de Fogo:** Índice que indica a probabilidade de ocorrência de incêndio, baseado em fatores como condições climáticas e quantidade de combustível disponível.
- **Bioma:** Bioma onde o foco foi identificado, como Amazônia, Cerrado, ou Mata Atlântica.
- **FRP (Fire Radiative Power):** Potência radiativa do fogo, que mede a intensidade do incêndio. Focos com FRP mais alto indicam incêndios mais intensos.

## Visualização Gráfica

Se você deseja visualizar de forma gráfica onde as queimadas estão ocorrendo, copie as coordenadas de latitude e longitude mais recentes e cole no Google Maps. Isso permite uma compreensão espacial mais clara da distribuição dos focos de incêndio. Alternativamente, você também pode usar a descrição de localização (Município, Estado e País) para identificar a região afetada.

## Informação Adicional

As queimadas na Amazônia não apenas afetam a biodiversidade local, mas também têm implicações globais, contribuindo para o aquecimento global e a emissão de gases de efeito estufa. O monitoramento contínuo é essencial para entender e mitigar os impactos desses incêndios, além de auxiliar na gestão de políticas ambientais e ações de preservação.

## Dados Diários - Página 1

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 26684984-b0a1-334e-85a9-202366da4d9b | 1.0844 | -60.6741 | 2026-03-18 00:00:00 | GOES-19 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 62.8 |
| e29b3145-c610-31ae-93c8-0bc7890c67cf | 1.0844 | -60.6931 | 2026-03-18 00:00:00 | GOES-19 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 62.9 |
| c53f0f0c-ad46-32e8-a2da-d72f8eed9cc2 | 0.7751 | -59.8592 | 2026-03-18 00:00:00 | GOES-19 | SÃO JOÃO DA BALIZA | RORAIMA | Brasil | 1400506 | 14 | 33 | nan | nan | nan | Amazônia | 48.2 |
| 8e15653e-e4fa-3bcc-a8f2-d5a12742ed7d | 3.0546 | -60.7659 | 2026-03-18 00:00:00 | GOES-19 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 56.5 |
| 7a2f9833-76e9-3c0d-8ce5-b533ceb5ce8b | 0.775 | -59.8782 | 2026-03-18 00:00:00 | GOES-19 | SÃO JOÃO DA BALIZA | RORAIMA | Brasil | 1400506 | 14 | 33 | nan | nan | nan | Amazônia | 51.4 |
| 515764fd-de8c-3684-9620-1de85b1759d6 | 0.775 | -59.8782 | 2026-03-18 00:10:00 | GOES-19 | SÃO JOÃO DA BALIZA | RORAIMA | Brasil | 1400506 | 14 | 33 | nan | nan | nan | Amazônia | 50.0 |
| dc8993b9-9437-342e-b987-9c9bf8aaed41 | 0.7751 | -59.8592 | 2026-03-18 00:10:00 | GOES-19 | SÃO JOÃO DA BALIZA | RORAIMA | Brasil | 1400506 | 14 | 33 | nan | nan | nan | Amazônia | 45.4 |
| a5d0a520-85e3-3eae-9edb-0bd6e87bb76e | -10.2548 | -36.4443 | 2026-03-18 00:10:00 | GOES-19 | PENEDO | ALAGOAS | Brasil | 2706703 | 27 | 33 | nan | nan | nan | Mata Atlântica | 111.1 |
| c5a3836b-a0fb-3f09-bb44-18adafb4846c | 3.0546 | -60.7659 | 2026-03-18 00:10:00 | GOES-19 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 60.9 |
| 1a5e0a9a-a427-3db0-9b71-866c96e341a5 | -10.0662 | -36.2359 | 2026-03-18 00:20:00 | GOES-19 | CORURIPE | ALAGOAS | Brasil | 2702306 | 27 | 33 | nan | nan | nan | Mata Atlântica | 538.4 |
| 52a259b5-2886-31e0-9b11-0521ff8f49fc | -10.085 | -36.2595 | 2026-03-18 00:20:00 | GOES-19 | CORURIPE | ALAGOAS | Brasil | 2702306 | 27 | 33 | nan | nan | nan | Mata Atlântica | 129.2 |
| 5f3c47f8-7a18-35f2-8fd4-a0a0d3f26eff | -10.0855 | -36.2324 | 2026-03-18 00:20:00 | GOES-19 | CORURIPE | ALAGOAS | Brasil | 2702306 | 27 | 33 | nan | nan | nan | Mata Atlântica | 476.1 |
| 2311bb80-996c-3bc6-91a7-3e4594e2ba30 | -10.0656 | -36.263 | 2026-03-18 00:20:00 | GOES-19 | CORURIPE | ALAGOAS | Brasil | 2702306 | 27 | 33 | nan | nan | nan | Mata Atlântica | 142.3 |
| d2a223fb-e139-34f5-8b35-048d0a8a45dd | -10.0667 | -36.2088 | 2026-03-18 00:20:00 | GOES-19 | CORURIPE | ALAGOAS | Brasil | 2702306 | 27 | 33 | nan | nan | nan | Mata Atlântica | 99.6 |
| a849f5f4-dc28-3e60-a691-1bfaed22fe0f | 3.0546 | -60.7659 | 2026-03-18 00:20:00 | GOES-19 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 51.5 |
| 59ce5827-9e95-304a-8632-66fcaa8b2aee | -10.2548 | -36.4443 | 2026-03-18 00:20:00 | GOES-19 | PENEDO | ALAGOAS | Brasil | 2706703 | 27 | 33 | nan | nan | nan | Mata Atlântica | 132.9 |
| 72163bbe-fb5f-3e3d-a673-ea14c71daf6e | -10.086 | -36.2053 | 2026-03-18 00:20:00 | GOES-19 | CORURIPE | ALAGOAS | Brasil | 2702306 | 27 | 33 | nan | nan | nan | Mata Atlântica | 89.2 |
| 1d399fde-6a01-3abb-b107-ef955300fe6b | 3.0546 | -60.7659 | 2026-03-18 00:40:00 | GOES-19 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 76.3 |
| 5229f04b-9fd6-3cd0-9286-b10547e5e469 | 3.0728 | -60.7656 | 2026-03-18 00:40:00 | GOES-19 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 50.8 |
| 1cf8532a-5363-3ea5-ba06-16d77ab094e3 | 0.775 | -59.8782 | 2026-03-18 00:50:00 | GOES-19 | SÃO JOÃO DA BALIZA | RORAIMA | Brasil | 1400506 | 14 | 33 | nan | nan | nan | Amazônia | 49.4 |
| 137ab450-756e-3d82-8a8b-fd4b846b116c | -16.4423 | -58.172 | 2026-03-18 00:50:00 | GOES-19 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 58.8 |
| 004c4c93-36fa-392d-99af-4017855bdd91 | 0.775 | -59.8782 | 2026-03-18 01:00:00 | GOES-19 | SÃO JOÃO DA BALIZA | RORAIMA | Brasil | 1400506 | 14 | 33 | nan | nan | nan | Amazônia | 45.8 |
| 44aa21c3-6691-3596-aba2-acddb15f0a40 | 3.0546 | -60.7659 | 2026-03-18 01:20:00 | GOES-19 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 56.8 |
| 5d765dd2-2f42-3b29-a230-9a20858b267c | -16.58315 | -57.80857 | 2026-03-18 01:20:00 | TERRA_M-M | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 6.0 |
| f9fabffe-15c7-38c4-9fa1-4e26584a88c1 | -16.44599 | -58.17178 | 2026-03-18 01:20:00 | TERRA_M-M | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 31.8 |
| 8df8e79d-4b34-3adf-bef4-f4180f5274e0 | -16.44851 | -58.1873 | 2026-03-18 01:20:00 | TERRA_M-M | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 15.4 |
| a4674e90-0b2a-31fa-9653-e2d6bb38ceff | 3.06724 | -60.76008 | 2026-03-18 01:24:00 | TERRA_M-M | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 37.3 |
| 62738646-08a1-39cc-a612-c6359d463002 | 2.44239 | -60.246 | 2026-03-18 01:24:00 | TERRA_M-M | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 14.7 |
| 7c2c32b4-23d4-36be-becd-0eda75815a11 | 3.05422 | -60.75831 | 2026-03-18 01:24:00 | TERRA_M-M | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 12.7 |
| 43e5d4ed-4cc4-32f1-8625-37551f1d45c4 | 3.05146 | -60.7787 | 2026-03-18 01:24:00 | TERRA_M-M | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 39.3 |
| 1e94b52d-3d8a-32cc-a130-3633bfd0bab6 | 3.06265 | -60.78683 | 2026-03-18 01:24:00 | TERRA_M-M | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 28.3 |
| 87517f41-a233-3eff-8413-c8d60258812f | 3.06528 | -60.76644 | 2026-03-18 01:24:00 | TERRA_M-M | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 76.7 |
| c046f117-2e04-3766-8339-147166a127c7 | 3.06445 | -60.78046 | 2026-03-18 01:24:00 | TERRA_M-M | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 40.7 |
| 96dd8965-7e79-3ff4-810c-46142752d17c | 1.07365 | -60.69333 | 2026-03-18 01:24:00 | TERRA_M-M | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 15.6 |
| aff5b1bf-dc76-3534-ac15-85303ed616c5 | 3.0545 | -60.7849 | 2026-03-18 01:30:00 | GOES-19 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 50.8 |
| 0af94a21-5bb6-330b-ba60-596dfd63447a | 3.0546 | -60.7659 | 2026-03-18 01:30:00 | GOES-19 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 77.5 |
| 78f6e79c-5dec-3867-aa7e-b7841f45e3bc | 3.0728 | -60.7656 | 2026-03-18 01:40:00 | GOES-19 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 51.5 |
| ec331418-fd47-3cf5-9f25-70eacf964d9a | 3.0546 | -60.7659 | 2026-03-18 01:40:00 | GOES-19 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 90.1 |
| b80e972e-b030-3a05-91a8-5939cbce34ce | 3.0545 | -60.7849 | 2026-03-18 01:40:00 | GOES-19 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 46.4 |
| c5a4a70b-96d2-3355-a67a-6db41db545e9 | 3.0546 | -60.7659 | 2026-03-18 01:50:00 | GOES-19 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 56.3 |
| c1c59425-ae0c-3e2f-acef-259050ed6353 | -16.4618 | -58.1699 | 2026-03-18 01:50:00 | GOES-19 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 53.3 |
| ee79a0a3-cca2-389f-a813-b9a02941b827 | -10.69178 | -36.92555 | 2026-03-18 03:32:00 | NOAA-21 | SANTO AMARO DAS BROTAS | SERGIPE | Brasil | 2806602 | 28 | 33 | nan | nan | nan | Mata Atlântica | 2.0 |
| 666c61d2-2bf3-314c-858e-6d4d0e0a889a | -11.89289 | -37.77053 | 2026-03-18 03:32:00 | NOAA-21 | ESPLANADA | BAHIA | Brasil | 2910602 | 29 | 33 | nan | nan | nan | Mata Atlântica | 22.1 |
| 1ce30aee-6d70-34a2-83ed-a18454ad43b6 | -11.88903 | -37.76984 | 2026-03-18 03:32:00 | NOAA-21 | ESPLANADA | BAHIA | Brasil | 2910602 | 29 | 33 | nan | nan | nan | Mata Atlântica | 14.1 |
| 1429bf89-a982-3217-bbb5-3524079f2b46 | -11.02264 | -37.08849 | 2026-03-18 03:32:00 | NOAA-21 | ARACAJU | SERGIPE | Brasil | 2800308 | 28 | 33 | nan | nan | nan | Mata Atlântica | 3.6 |
| 5d255772-c71d-3400-a235-03083e8b4f82 | -13.39684 | -40.37872 | 2026-03-18 03:32:00 | NOAA-21 | MARACÁS | BAHIA | Brasil | 2920502 | 29 | 33 | nan | nan | nan | Mata Atlântica | 3.4 |
| 890bb11c-6711-303a-95b8-5af797557406 | -13.21409 | -39.81569 | 2026-03-18 03:32:00 | NOAA-21 | UBAÍRA | BAHIA | Brasil | 2932101 | 29 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 390255c9-e7ee-3fce-88c0-4cb87982485d | -11.26002 | -41.04773 | 2026-03-18 03:32:00 | NOAA-21 | MORRO DO CHAPÉU | BAHIA | Brasil | 2921708 | 29 | 33 | nan | nan | nan | Caatinga | 1.0 |
| e7edc775-e039-3c85-a022-e2e1c8590f0c | -13.06056 | -38.98853 | 2026-03-18 03:32:00 | NOAA-21 | ARATUÍPE | BAHIA | Brasil | 2902302 | 29 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| d2b3088d-3081-3ec6-9b35-6e9d3cec01a3 | -22.59144 | -49.31005 | 2026-03-18 03:36:00 | NOAA-21 | PAULISTÂNIA | SÃO PAULO | Brasil | 3536570 | 35 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 6853b468-d1bd-369d-aca1-81e66daeb0da | -22.59006 | -49.31576 | 2026-03-18 03:36:00 | NOAA-21 | PAULISTÂNIA | SÃO PAULO | Brasil | 3536570 | 35 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 28348365-9abb-333b-846a-f23d8f766885 | -22.59094 | -49.31131 | 2026-03-18 03:36:00 | NOAA-21 | PAULISTÂNIA | SÃO PAULO | Brasil | 3536570 | 35 | 33 | nan | nan | nan | Cerrado | 8.0 |
| 8201d711-93dc-336b-9dd3-ff62217d54ef | -5.53086 | -35.52116 | 2026-03-18 04:00:00 | NPP-375D | TAIPU | RIO GRANDE DO NORTE | Brasil | 2413904 | 24 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 341c8852-bfe8-3354-b7a0-b19e67ca00ca | -13.39695 | -40.37573 | 2026-03-18 04:02:00 | NPP-375D | MARACÁS | BAHIA | Brasil | 2920502 | 29 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 5c78cb62-74aa-3795-b9e6-9ccd2006a55f | -11.89279 | -37.77002 | 2026-03-18 04:02:00 | NPP-375D | ESPLANADA | BAHIA | Brasil | 2910602 | 29 | 33 | nan | nan | nan | Mata Atlântica | 13.3 |
| c3dac70a-dd50-327f-98f5-2234f97ab1c5 | -13.3997 | -40.37985 | 2026-03-18 04:02:00 | NPP-375D | MARACÁS | BAHIA | Brasil | 2920502 | 29 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| fa0889e9-6c8d-395b-9ae3-fa659092de26 | -12.67684 | -38.80544 | 2026-03-18 04:02:00 | NPP-375D | SANTO AMARO | BAHIA | Brasil | 2928604 | 29 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 845aaa72-4cba-32b4-a06e-e7c68c7b3faa | -13.21613 | -39.81556 | 2026-03-18 04:02:00 | NPP-375D | UBAÍRA | BAHIA | Brasil | 2932101 | 29 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 49a0dc93-5b3a-376b-8b04-337b82a1f4c2 | -10.79177 | -37.28534 | 2026-03-18 04:02:00 | NPP-375D | AREIA BRANCA | SERGIPE | Brasil | 2800506 | 28 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| dcd0edc1-3c55-3880-b339-9ba0156917a3 | -7.05586 | -45.06644 | 2026-03-18 04:02:00 | NPP-375D | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 9fd71d05-49ce-3f78-b071-09cb28444e79 | -11.94461 | -40.06001 | 2026-03-18 04:02:00 | NPP-375D | BAIXA GRANDE | BAHIA | Brasil | 2902609 | 29 | 33 | nan | nan | nan | Caatinga | 0.6 |
| d1fe298e-5b61-36f0-bfca-e9ac5ca06f63 | -13.39638 | -40.37929 | 2026-03-18 04:02:00 | NPP-375D | MARACÁS | BAHIA | Brasil | 2920502 | 29 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 3ed327da-1863-3dc8-bf27-a84c7c83b5f6 | -11.96 | -41.29412 | 2026-03-18 04:02:00 | NPP-375D | BONITO | BAHIA | Brasil | 2904050 | 29 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 2b5e1156-3ef0-35eb-9d67-d3f3f8c14649 | -10.20782 | -44.76208 | 2026-03-18 04:02:00 | NPP-375D | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| ebf02ed9-5de5-3a79-a189-74fe6dc2b1c9 | -11.88937 | -37.76949 | 2026-03-18 04:02:00 | NPP-375D | ESPLANADA | BAHIA | Brasil | 2910602 | 29 | 33 | nan | nan | nan | Mata Atlântica | 12.0 |
| 47ad73a9-39db-369b-9cf6-8b99207ac4ac | -10.69116 | -36.9283 | 2026-03-18 04:02:00 | NPP-375D | GENERAL MAYNARD | SERGIPE | Brasil | 2802502 | 28 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| f577b6c4-e2ad-3172-9486-b9d1bafa8791 | -10.04398 | -37.72991 | 2026-03-18 04:02:00 | NPP-375D | MONTE ALEGRE DE SERGIPE | SERGIPE | Brasil | 2804201 | 28 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 647bb6fb-62e3-3bf1-b391-3d8aab64fb24 | -6.28545 | -43.92743 | 2026-03-18 04:02:00 | NPP-375D | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| afa423d2-4289-3a9c-b98c-4e7e27631e73 | -11.94128 | -40.05946 | 2026-03-18 04:02:00 | NPP-375D | BAIXA GRANDE | BAHIA | Brasil | 2902609 | 29 | 33 | nan | nan | nan | Caatinga | 0.6 |
| ed5ea51f-6637-3777-b1b4-e0ac92ae6053 | -17.58358 | -39.4664 | 2026-03-18 04:04:00 | NPP-375D | ALCOBAÇA | BAHIA | Brasil | 2900801 | 29 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 7dec3d9a-b722-349d-b701-eb2cd0224491 | -18.73152 | -40.0303 | 2026-03-18 04:04:00 | NPP-375D | SÃO MATEUS | ESPÍRITO SANTO | Brasil | 3204906 | 32 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| a2ba1390-a6e2-3f10-b6c9-4d25d16099dd | -15.38478 | -39.15609 | 2026-03-18 04:04:00 | NPP-375D | UNA | BAHIA | Brasil | 2932507 | 29 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 3d7fe298-fae5-3fe9-84e6-9660bda403c8 | -21.70243 | -42.26671 | 2026-03-18 04:06:00 | NPP-375D | SANTO ANTÔNIO DE PÁDUA | RIO DE JANEIRO | Brasil | 3304706 | 33 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 2b0bb29d-8ca3-37b3-bab2-1ce0033d9b93 | -23.42878 | -46.75704 | 2026-03-18 04:06:00 | NPP-375D | SÃO PAULO | SÃO PAULO | Brasil | 3550308 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| 7864d7fb-3e6b-366a-9d3d-607969a3226d | -23.70383 | -46.59443 | 2026-03-18 04:06:00 | NPP-375D | DIADEMA | SÃO PAULO | Brasil | 3513801 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 4b702f8b-8f74-3c49-874c-146c924cb0e7 | -10.20863 | -44.76003 | 2026-03-18 04:21:00 | NOAA-20 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 804cd752-cdef-37a0-a79b-01461447f47d | -10.36654 | -44.87875 | 2026-03-18 04:21:00 | NOAA-20 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 0.3 |
| fa063c93-6d2f-396e-8982-1639ee6b2c64 | -10.20808 | -44.76358 | 2026-03-18 04:21:00 | NOAA-20 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 81a2193d-f946-36e6-b2d8-bf51524ee6af | -9.47843 | -46.11659 | 2026-03-18 04:21:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 3bb067b3-35f6-3806-aae6-f02a527a16cc | -7.98936 | -40.21743 | 2026-03-18 04:21:00 | NOAA-20 | OURICURI | PERNAMBUCO | Brasil | 2609907 | 26 | 33 | nan | nan | nan | Caatinga | 0.5 |
| d702073d-05f5-3ddc-8142-4b1af300a569 | -13.57071 | -42.56292 | 2026-03-18 04:23:00 | NOAA-20 | TANQUE NOVO | BAHIA | Brasil | 2931053 | 29 | 33 | nan | nan | nan | Caatinga | 1.5 |
| bf8228c0-82a5-32ac-b483-c11700325b9d | -11.88888 | -37.76719 | 2026-03-18 04:23:00 | NOAA-20 | CONDE | BAHIA | Brasil | 2908606 | 29 | 33 | nan | nan | nan | Mata Atlântica | 4.2 |
| fda2f5f4-a759-34bd-93db-99520ca5a509 | -11.94481 | -40.0601 | 2026-03-18 04:23:00 | NOAA-20 | BAIXA GRANDE | BAHIA | Brasil | 2902609 | 29 | 33 | nan | nan | nan | Caatinga | 0.6 |
| 086ecb26-c2dc-3709-9b48-c06cd9758bc6 | -13.21488 | -39.8157 | 2026-03-18 04:23:00 | NOAA-20 | UBAÍRA | BAHIA | Brasil | 2932101 | 29 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 9559bcfa-972c-3c43-9a65-40557512875d | -11.94052 | -40.05952 | 2026-03-18 04:23:00 | NOAA-20 | BAIXA GRANDE | BAHIA | Brasil | 2902609 | 29 | 33 | nan | nan | nan | Caatinga | 0.6 |
| 6b631fb2-b0d8-3e49-a5ac-8712a01cb3f0 | -11.8886 | -37.76842 | 2026-03-18 04:23:00 | NOAA-20 | ESPLANADA | BAHIA | Brasil | 2910602 | 29 | 33 | nan | nan | nan | Mata Atlântica | 5.0 |
| 25c4526a-4234-3535-a3cc-78a7388f85db | -13.39598 | -40.3758 | 2026-03-18 04:23:00 | NOAA-20 | MARACÁS | BAHIA | Brasil | 2920502 | 29 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 93117fa5-73f7-31f9-9d62-32a6de1c5a02 | -11.88821 | -37.77137 | 2026-03-18 04:23:00 | NOAA-20 | ESPLANADA | BAHIA | Brasil | 2910602 | 29 | 33 | nan | nan | nan | Mata Atlântica | 5.0 |
| 13993179-b156-3c15-a7ed-bbf8eb56c4ad | -11.88851 | -37.77013 | 2026-03-18 04:23:00 | NOAA-20 | ESPLANADA | BAHIA | Brasil | 2910602 | 29 | 33 | nan | nan | nan | Mata Atlântica | 5.5 |
| ba1ee876-a92b-316f-b8aa-bfd7f2ecf773 | -11.89353 | -37.77076 | 2026-03-18 04:23:00 | NOAA-20 | ESPLANADA | BAHIA | Brasil | 2910602 | 29 | 33 | nan | nan | nan | Mata Atlântica | 5.5 |
| 7644f6f7-d08c-3284-abee-2a5cf1d7cfe7 | -16.55066 | -42.65768 | 2026-03-18 04:23:00 | NOAA-20 | JOSENÓPOLIS | MINAS GERAIS | Brasil | 3136579 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 5ca9714d-ec0f-3adf-a081-730ba37822ce | -11.8939 | -37.76781 | 2026-03-18 04:23:00 | NOAA-20 | ESPLANADA | BAHIA | Brasil | 2910602 | 29 | 33 | nan | nan | nan | Mata Atlântica | 4.2 |
| 3454f0fc-e0ed-3aea-8fb7-c7a5a318d069 | -16.44684 | -58.17735 | 2026-03-18 04:25:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 5.4 |
| cf908c52-13c3-3c56-82b0-88deef2de00e | -16.58044 | -57.80182 | 2026-03-18 04:25:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.4 |
| 2fd6ff6b-dd71-3b2b-aba9-6ee9de79a877 | -23.42667 | -46.75814 | 2026-03-18 04:25:00 | NOAA-20 | SÃO PAULO | SÃO PAULO | Brasil | 3550308 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| dc673063-e140-3e48-847e-be6aaed7601c | -21.97921 | -54.62736 | 2026-03-18 04:25:00 | NOAA-20 | DOURADINA | MATO GROSSO DO SUL | Brasil | 5003504 | 50 | 33 | nan | nan | nan | Mata Atlântica | 2.2 |
| 08e284d3-eee1-380e-a27f-5d2567359924 | -16.57392 | -57.80466 | 2026-03-18 04:25:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.2 |
| ab1e93f7-d1f1-3667-b33f-e577cfaa2bf5 | -23.70207 | -46.59365 | 2026-03-18 04:25:00 | NOAA-20 | DIADEMA | SÃO PAULO | Brasil | 3513801 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 9bb345a9-b0a2-394b-9200-108b9321d763 | -16.44775 | -58.17313 | 2026-03-18 04:25:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 9.1 |
| 8d6541e9-18c9-3f98-b75e-286f1df7b278 | -16.45263 | -58.17867 | 2026-03-18 04:25:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 5.4 |


[Clique aqui para ver as próximas entradas](README2.md)
