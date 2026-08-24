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

## Dados Diários - Página 54

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| bb20c50d-42b1-344a-afaa-1865c8596655 | -16.0701 | -50.4552 | 2026-08-24 14:20:00 | GOES-19 | GOIÁS | GOIÁS | Brasil | 5208905 | 52 | 33 | nan | nan | nan | Cerrado | 51.1 |
| 0216b9a0-c1c2-3987-8b65-fc9413fa52b5 | -14.3933 | -52.9667 | 2026-08-24 14:20:00 | GOES-19 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 124.2 |
| f7c1bdc6-d4c5-360b-a439-6d38aae331f6 | -9.068 | -50.7784 | 2026-08-24 14:20:00 | GOES-19 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 101.9 |
| 3781163c-a375-3f2b-b49c-95daf1be4c65 | -7.8277 | -47.6602 | 2026-08-24 14:20:00 | GOES-19 | BARRA DO OURO | TOCANTINS | Brasil | 1703073 | 17 | 33 | nan | nan | nan | Cerrado | 90.1 |
| 1254d896-3477-3b2e-bc3b-807bbe9ccde8 | -9.6774 | -55.1022 | 2026-08-24 14:20:00 | GOES-19 | NOVO MUNDO | MATO GROSSO | Brasil | 5106265 | 51 | 33 | nan | nan | nan | Amazônia | 59.7 |
| 91606830-0f33-3013-9dbd-879078406ad0 | -15.266 | -52.8111 | 2026-08-24 14:20:00 | GOES-19 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 90.5 |
| 8f994ef7-bb1c-3086-972a-d442a76f6b11 | -7.2193 | -60.6316 | 2026-08-24 14:20:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 67.4 |
| 19ba2c48-099f-348b-a332-6a8064eddd5a | -7.2901 | -45.3683 | 2026-08-24 14:20:00 | GOES-19 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 236.2 |
| 93799a4a-5129-32b8-b342-50d7ada4c20b | -13.8954 | -54.0508 | 2026-08-24 14:20:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 101.2 |
| 8aeae247-d55b-3b42-81b4-00bcf8d44370 | -9.6776 | -55.082 | 2026-08-24 14:20:00 | GOES-19 | NOVO MUNDO | MATO GROSSO | Brasil | 5106265 | 51 | 33 | nan | nan | nan | Amazônia | 57.2 |
| becd0003-e761-3a4c-8f97-b14718fa38e6 | -7.828 | -47.6383 | 2026-08-24 14:20:00 | GOES-19 | BARRA DO OURO | TOCANTINS | Brasil | 1703073 | 17 | 33 | nan | nan | nan | Cerrado | 69.7 |
| 960087f4-d5d5-3873-a255-ed42fb01f78e | -6.8202 | -59.4194 | 2026-08-24 14:20:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 54.3 |
| c736ed63-26c7-39b0-a68b-e3e20934cfad | -15.2854 | -52.8084 | 2026-08-24 14:20:00 | GOES-19 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 129.8 |
| 25a65dda-fca9-3725-a8fa-f82cf4519188 | -6.3692 | -54.7455 | 2026-08-24 14:20:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 56.1 |
| bad2a139-a3c9-30e4-9344-857908cd7d5b | -15.2652 | -52.8535 | 2026-08-24 14:20:00 | GOES-19 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 92.0 |
| 1b4afe37-1bff-35da-80de-edade6931149 | -6.1727 | -53.7067 | 2026-08-24 14:20:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 91.5 |
| 329106ce-50c4-3ac7-9eb2-c5f3d78ea109 | -13.8957 | -54.03 | 2026-08-24 14:20:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 87.3 |
| 8638257b-e245-301d-8ddf-8dd41228d43c | -10.8174 | -50.9498 | 2026-08-24 14:20:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 117.7 |
| 3686b139-1381-37c5-b041-0108edd1c8eb | -7.4882 | -44.4601 | 2026-08-24 14:20:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 172.0 |
| 7d24d42f-ae36-31ad-8346-bd9c944850a4 | -7.2979 | -43.0137 | 2026-08-24 14:20:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 119.6 |
| 9a43c49f-1c24-3380-8142-450a0c06073c | -15.2648 | -52.8747 | 2026-08-24 14:20:00 | GOES-19 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 147.2 |
| 8536371a-87be-3f5d-a4fb-2ba6293f7679 | -6.332 | -54.7674 | 2026-08-24 14:20:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 316.1 |
| 06c501a6-b40c-33ec-bf06-010dc2fdde66 | -7.7706 | -61.1061 | 2026-08-24 14:20:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 65.8 |
| 212dfbcc-c7ac-3e68-a8a6-9d58cb6637bd | -14.2537 | -52.0964 | 2026-08-24 14:20:00 | GOES-19 | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 99.3 |
| 4f0106b5-b857-36bd-856a-320ffaeb2e14 | -14.3737 | -52.9903 | 2026-08-24 14:20:00 | GOES-19 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 146.2 |
| ba431779-4064-3330-8cc4-187e22b137f6 | -14.9586 | -52.6614 | 2026-08-24 14:20:00 | GOES-19 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 79.9 |
| 192cc445-57d0-38db-848d-25a9fb2536c4 | -14.2591 | -51.7764 | 2026-08-24 14:20:00 | GOES-19 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 68.8 |
| 5db667b6-76ff-38e7-a115-70c95acd3bea | -6.8305 | -52.5061 | 2026-08-24 14:20:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 100.1 |
| f6e1f45f-a821-3601-95d8-d6f62a221e3e | -6.1542 | -53.7077 | 2026-08-24 14:20:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 104.7 |
| c9bd88b4-29f3-3418-8073-05186f7d1334 | -9.473 | -56.9164 | 2026-08-24 14:20:00 | GOES-19 | PARANAÍTA | MATO GROSSO | Brasil | 5106299 | 51 | 33 | nan | nan | nan | Amazônia | 57.9 |
| 779fd332-7e12-3055-9ca5-ce1398a79fb2 | -6.1544 | -53.6874 | 2026-08-24 14:20:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 116.6 |
| 6acb231b-fc56-3aaf-b7dc-d183d6832467 | -10.7985 | -50.9518 | 2026-08-24 14:20:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 166.4 |
| 1e3eff7b-3ce0-3406-bec6-56adae824bab | -13.8768 | -54.0114 | 2026-08-24 14:20:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 83.7 |
| 44752a5f-b8fe-3a3d-bc2d-2ccb489e1722 | -10.4463 | -50.4353 | 2026-08-24 14:20:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 100.8 |
| 7cb8c6d4-a3ed-3ef9-be4e-fc5c49786089 | -12.1417 | -43.3945 | 2026-08-24 14:20:00 | GOES-19 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 149.2 |
| f78b9a7c-0db3-3980-a7a3-a45c2ccbbdb0 | -6.8491 | -52.505 | 2026-08-24 14:20:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 84.5 |
| da7402f9-2c47-3722-a276-938d410ae0f2 | -6.3507 | -54.7464 | 2026-08-24 14:20:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 378.1 |
| b3c94378-645e-3072-a3c7-cb896c0d06f7 | -14.393 | -52.9878 | 2026-08-24 14:20:00 | GOES-19 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 193.8 |
| 11315be8-2ed2-3399-8380-afda1a786eb0 | -14.2785 | -51.7739 | 2026-08-24 14:20:00 | GOES-19 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 89.1 |
| bf5cd1d9-1906-32ab-8f66-59d58e238aa3 | -13.1512 | -51.3854 | 2026-08-24 14:20:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 102.0 |
| 3a8ac5d7-22fd-3369-bfe7-1c2af198e2c9 | -6.3322 | -54.7473 | 2026-08-24 14:20:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 165.5 |
| a008d480-7160-3032-9717-d5024ec191a2 | -10.7988 | -50.9305 | 2026-08-24 14:20:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 141.8 |
| 8d337655-5837-3bfe-9204-7e98204dcf45 | -14.2785 | -51.7739 | 2026-08-24 14:30:00 | GOES-19 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 184.8 |
| d8404f05-b2fd-38e4-9d9a-00243934e091 | -12.0566 | -50.5567 | 2026-08-24 14:30:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 135.1 |
| 08e647b0-b073-3bff-bbda-e4d22e28e7dd | -10.0867 | -46.3846 | 2026-08-24 14:30:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 127.0 |
| 25aa5678-b625-30ee-99a9-6461c895aeb2 | -4.9535 | -45.1374 | 2026-08-24 14:30:00 | GOES-19 | LAGO DA PEDRA | MARANHÃO | Brasil | 2105708 | 21 | 33 | nan | nan | nan | Cerrado | 140.6 |
| e516bbfa-6635-3684-be20-db5d2c7eb116 | -12.0563 | -50.5782 | 2026-08-24 14:30:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 92.2 |
| f7396dca-45b4-3bf0-9440-08a80514a69f | -15.2648 | -52.8747 | 2026-08-24 14:30:00 | GOES-19 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 148.3 |
| 6c7c3e61-2931-32ac-8f37-3fe2e5c952eb | -12.0753 | -50.5759 | 2026-08-24 14:30:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 112.4 |
| f57d7774-9e90-354e-8e1b-d42111e8fd1f | -6.1727 | -53.7067 | 2026-08-24 14:30:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 107.9 |
| 0bbcd2cd-5de8-3e67-abf4-277dae20a46c | -10.4463 | -50.4353 | 2026-08-24 14:30:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 130.2 |
| 78d7a5b5-c7b7-3280-b067-f39ecec823de | -6.332 | -54.7674 | 2026-08-24 14:30:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 404.3 |
| 36ea1158-682f-354c-a471-10418fc1f48d | -10.7988 | -50.9305 | 2026-08-24 14:30:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 103.1 |
| 69d111f1-2b52-3aa1-9c93-2a78009868ca | -7.2901 | -45.3683 | 2026-08-24 14:30:00 | GOES-19 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 216.3 |
| b867e858-55a6-394f-ba5f-fc4414c0e993 | -12.1132 | -50.5929 | 2026-08-24 14:30:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 172.8 |
| e78b487f-f736-3e65-9ec0-89f84f51a234 | -14.3737 | -52.9903 | 2026-08-24 14:30:00 | GOES-19 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 117.4 |
| 70fddf81-d3be-358a-a89f-de44e5df6634 | -14.312 | -53.2291 | 2026-08-24 14:30:00 | GOES-19 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 84.5 |
| 7d574f65-ad38-3d27-b834-c4c1745794f2 | -10.7985 | -50.9518 | 2026-08-24 14:30:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 139.3 |
| d0fc3c40-d3a8-35ca-bcbc-84637a1a0938 | -12.1319 | -50.6121 | 2026-08-24 14:30:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 71.4 |
| 0101425c-5986-3a30-81dc-6f07547a27fd | -9.6776 | -55.082 | 2026-08-24 14:30:00 | GOES-19 | NOVO MUNDO | MATO GROSSO | Brasil | 5106265 | 51 | 33 | nan | nan | nan | Amazônia | 55.9 |
| 9673cf95-477e-324d-8d30-0c38f0c8fa05 | -4.9721 | -45.1362 | 2026-08-24 14:30:00 | GOES-19 | LAGO DA PEDRA | MARANHÃO | Brasil | 2105708 | 21 | 33 | nan | nan | nan | Cerrado | 64.5 |
| 6b99c261-2e81-3892-9468-b9897e114900 | -6.1544 | -53.6874 | 2026-08-24 14:30:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 141.6 |
| 658edbbd-14fb-3c20-a3b5-dd4aa59241af | -14.3933 | -52.9667 | 2026-08-24 14:30:00 | GOES-19 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 134.2 |
| 8cdda7e5-164a-3bca-9fdd-458b621d6281 | -7.2979 | -43.0137 | 2026-08-24 14:30:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 139.8 |
| b6a667c8-44ff-3c5b-acdd-46dbe8e0c7f3 | -14.2978 | -51.7713 | 2026-08-24 14:30:00 | GOES-19 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 95.5 |
| a1777d10-6868-38cc-a072-81ceaef75e94 | -14.2402 | -51.7576 | 2026-08-24 14:30:00 | GOES-19 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 86.5 |
| f34920f1-42bc-3c8c-9187-16bc3fa708e8 | -15.2854 | -52.8084 | 2026-08-24 14:30:00 | GOES-19 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 107.5 |
| 72fb8c00-6422-376d-af94-a190e686d115 | -7.2713 | -45.37 | 2026-08-24 14:30:00 | GOES-19 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 131.4 |
| bba1e89f-a190-37e2-b6ef-0255266f36d4 | -6.1542 | -53.7077 | 2026-08-24 14:30:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 136.2 |
| fccb88a4-2cd2-3a05-afff-02fad360eda6 | -10.0677 | -46.3869 | 2026-08-24 14:30:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 95.1 |
| 5858a1c6-0f3b-35c0-844f-205885561ec6 | -6.8491 | -52.505 | 2026-08-24 14:30:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 85.7 |
| f17c8f83-5837-3b06-ac4d-e2ad7b209513 | -12.1128 | -50.6143 | 2026-08-24 14:30:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 94.0 |
| f48d94b1-75f1-3269-b308-4aca7ded8ca3 | -6.8018 | -59.4201 | 2026-08-24 14:30:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 62.7 |
| 6d669472-dd83-33d7-8947-b1b84db3d9d2 | -9.068 | -50.7784 | 2026-08-24 14:30:00 | GOES-19 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 74.7 |
| 4bdb7b04-6d33-3fe9-a619-585008d0f926 | -7.2193 | -60.6316 | 2026-08-24 14:30:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 59.3 |
| 0c8426a6-647c-3a8c-8fb2-003e6e3b3612 | -6.7832 | -59.4401 | 2026-08-24 14:30:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 57.2 |
| 46025001-256f-33b6-bfa9-28fd96a66c94 | -10.8174 | -50.9498 | 2026-08-24 14:30:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 109.8 |
| dbdfeb7a-15d8-33cb-a810-079bc8d2f8ba | -6.3692 | -54.7455 | 2026-08-24 14:30:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 71.8 |
| ac313415-f9f0-339e-b855-7cd35701a238 | -14.293 | -53.2104 | 2026-08-24 14:30:00 | GOES-19 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 363.7 |
| 99abf9de-c4b3-3f12-945f-bd8da29eca2d | -14.2595 | -51.7551 | 2026-08-24 14:30:00 | GOES-19 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 89.3 |
| e07b9b46-dabf-3fd2-9452-6c491cafc2c0 | -13.8954 | -54.0508 | 2026-08-24 14:30:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 102.3 |
| 502ca1f0-bffa-3b1c-9c23-abad3524c6d4 | -7.507 | -44.4583 | 2026-08-24 14:30:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 151.8 |
| 837c608f-1ad1-35b2-87ce-d4fbff1fa450 | -15.2278 | -52.7738 | 2026-08-24 14:30:00 | GOES-19 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 101.1 |
| 6b74cd77-931d-37e8-bc7c-89c55e95f7c2 | -14.393 | -52.9878 | 2026-08-24 14:30:00 | GOES-19 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 209.4 |
| d6f03aa8-b546-396c-aae9-4ef997769259 | -7.4882 | -44.4601 | 2026-08-24 14:30:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 171.0 |
| 108d9726-2f37-3063-ab88-e38e8782b3fa | -7.8277 | -47.6602 | 2026-08-24 14:30:00 | GOES-19 | BARRA DO OURO | TOCANTINS | Brasil | 1703073 | 17 | 33 | nan | nan | nan | Cerrado | 73.7 |
| 08d05488-f08b-37db-bb47-4f62ec40d32d | -10.804 | -50.5473 | 2026-08-24 14:30:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 120.0 |
| f856e1b9-8c68-3b8f-a2ff-29cafda5ad6c | -14.2591 | -51.7764 | 2026-08-24 14:30:00 | GOES-19 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 93.2 |
| c2fff1b4-43f5-339c-92e8-c64f68757a09 | -6.3507 | -54.7464 | 2026-08-24 14:30:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 316.2 |
| 506f4b00-62e2-3c8a-a17f-1ddbdbe61390 | -12.1135 | -50.5714 | 2026-08-24 14:30:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 66.5 |
| 6b885728-57b4-35c3-a3de-c3ad0a740cc7 | -14.2781 | -51.7953 | 2026-08-24 14:30:00 | GOES-19 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 140.8 |
| 712c42e2-0cd2-3bdb-99c3-f492fe84f526 | -9.7131 | -46.0229 | 2026-08-24 14:30:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 86.5 |
| a152f2fa-9877-367d-bd32-bc5e8aef3b71 | -6.3322 | -54.7473 | 2026-08-24 14:30:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 193.8 |
| 596e797d-2d4d-3ce7-9a93-76d9afb1f4a4 | -12.5006 | -44.747 | 2026-08-24 14:30:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 86.9 |
| 2cd53b30-1a2a-31d8-a76f-c902455b614b | -15.2652 | -52.8535 | 2026-08-24 14:30:00 | GOES-19 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 85.8 |
| 4b665c29-f2d2-3bd7-a910-593a4f9f17ab | -6.8305 | -52.5061 | 2026-08-24 14:30:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 116.2 |
| bea5e4b2-4c6a-336e-941e-00d146c00bad | -16.0701 | -50.4552 | 2026-08-24 14:30:00 | GOES-19 | GOIÁS | GOIÁS | Brasil | 5208905 | 52 | 33 | nan | nan | nan | Cerrado | 63.3 |
| 8c347e01-eeec-33bd-bb1c-006e910e4cb8 | -10.785 | -50.5493 | 2026-08-24 14:30:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 121.9 |
| 08524327-6955-3084-8067-2dd01b3e87ce | -12.0566 | -50.5567 | 2026-08-24 14:40:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 128.8 |
| 8895790b-c501-34ea-90c2-094a9f825930 | -6.2136 | -55.9295 | 2026-08-24 14:40:00 | GOES-19 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 52.8 |


[Clique aqui para ver as próximas entradas](README55.md)
