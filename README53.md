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

## Dados Diários - Página 53

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 820b27dc-cad2-3b01-a776-43f5f15d4ea2 | -16.0701 | -50.4552 | 2026-08-24 14:00:00 | GOES-19 | GOIÁS | GOIÁS | Brasil | 5208905 | 52 | 33 | nan | nan | nan | Cerrado | 57.9 |
| 9678939a-c1eb-3181-8a72-f27aac0788be | -10.7988 | -50.9305 | 2026-08-24 14:00:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 105.6 |
| a12109d1-b174-3f96-956b-b36b58e6abc4 | -9.068 | -50.7784 | 2026-08-24 14:00:00 | GOES-19 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 99.0 |
| b9c83a8e-78b6-3949-84e4-d178ad0305c1 | -16.4143 | -49.9158 | 2026-08-24 14:00:00 | GOES-19 | ANICUNS | GOIÁS | Brasil | 5201306 | 52 | 33 | nan | nan | nan | Cerrado | 72.7 |
| cf6d727c-2063-310f-8d8c-cd86850d0865 | -14.2982 | -51.75 | 2026-08-24 14:00:00 | GOES-19 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 109.6 |
| 7a3120f2-7485-3a51-9039-3edb4e158f18 | -12.0941 | -50.5951 | 2026-08-24 14:00:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 92.5 |
| 250aafef-785b-3d3b-85e7-4953f6aefe88 | -14.2785 | -51.7739 | 2026-08-24 14:00:00 | GOES-19 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 136.6 |
| 9804a83d-3719-3b52-a4f5-1f7d9087cd9c | -15.2375 | -48.2231 | 2026-08-24 14:00:00 | GOES-19 | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 83.8 |
| 670321f2-5698-3a16-b7f3-23b017a2e514 | -7.507 | -44.4583 | 2026-08-24 14:00:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 115.3 |
| 6402ecd9-961f-3528-95e2-b261897954c1 | -14.2978 | -51.7713 | 2026-08-24 14:00:00 | GOES-19 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 170.9 |
| 1e63f5bb-a58a-34d0-8392-0e1f28c6bb45 | -7.4882 | -44.4601 | 2026-08-24 14:00:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 88.4 |
| 5a4cd4df-48d0-3842-9870-7e4ef06ba68c | -14.2788 | -51.7525 | 2026-08-24 14:00:00 | GOES-19 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 97.0 |
| 59c79d65-3a04-31b9-9384-f0f4807961c8 | -14.2781 | -51.7953 | 2026-08-24 14:00:00 | GOES-19 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 75.3 |
| c724b707-b45a-34fc-b40f-213dce537042 | -12.0566 | -50.5567 | 2026-08-24 14:00:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 130.4 |
| f370f963-87a6-3844-b1cc-b6f79bcb3cd6 | -10.7796 | -50.9537 | 2026-08-24 14:00:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 54.9 |
| cc8be6c5-9ac4-361d-aa84-43b16dc49572 | -15.4979 | -53.9813 | 2026-08-24 14:00:00 | GOES-19 | POXORÉU | MATO GROSSO | Brasil | 5107008 | 51 | 33 | nan | nan | nan | Cerrado | 66.3 |
| 7bc14ab7-cb18-3b99-bb06-87fb81db17a9 | -10.8174 | -50.9498 | 2026-08-24 14:00:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 103.8 |
| 650a22b0-0504-3904-b07d-611e5b054ff1 | -10.0867 | -46.3846 | 2026-08-24 14:00:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 115.5 |
| 51eb6f2d-b100-3414-a619-5e537772f315 | -10.0677 | -46.3869 | 2026-08-24 14:00:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 102.1 |
| 3cfa8d7e-fab2-3ad9-af2f-8a369c0b2cdc | -6.8491 | -52.505 | 2026-08-24 14:00:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 106.0 |
| 63ec4464-4929-3339-ac62-1bb7a5393c8e | -4.9535 | -45.1374 | 2026-08-24 14:00:00 | GOES-19 | LAGO DA PEDRA | MARANHÃO | Brasil | 2105708 | 21 | 33 | nan | nan | nan | Cerrado | 69.5 |
| ef2a8ebc-43e3-3740-a8a3-5ab7bb274dad | -10.7985 | -50.9518 | 2026-08-24 14:00:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 118.0 |
| 99630501-449f-3c97-ab56-dd57d96e4e65 | -15.2854 | -52.8084 | 2026-08-24 14:00:00 | GOES-19 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 78.9 |
| 19ca1125-4244-3f34-acd6-715e5f6af412 | -7.2713 | -45.37 | 2026-08-24 14:00:00 | GOES-19 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 99.6 |
| 0ea3ab35-4b4d-3991-a4b4-ca66063145e0 | -17.4412 | -44.936 | 2026-08-24 14:00:00 | GOES-19 | PIRAPORA | MINAS GERAIS | Brasil | 3151206 | 31 | 33 | nan | nan | nan | Cerrado | 74.0 |
| 39421840-6fce-3bfb-8340-0a6c70d83e9c | -14.9388 | -52.6853 | 2026-08-24 14:00:00 | GOES-19 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 77.6 |
| ff419c94-aa1a-3f8c-83d0-3762edcf8872 | -10.0046 | -46.8201 | 2026-08-24 14:00:00 | GOES-19 | SÃO FÉLIX DO TOCANTINS | TOCANTINS | Brasil | 1720150 | 17 | 33 | nan | nan | nan | Cerrado | 96.4 |
| 1974fc1b-94d5-3df9-8573-2ad7b4e568d6 | -10.0681 | -46.3643 | 2026-08-24 14:00:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 94.1 |
| 9a518766-a035-3c87-9b6a-949f911b5a34 | -14.2402 | -51.7576 | 2026-08-24 14:00:00 | GOES-19 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 73.7 |
| 77fb078f-d2f7-3ef3-9ae4-04c5460203fd | -7.2901 | -45.3683 | 2026-08-24 14:00:00 | GOES-19 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 187.5 |
| b207a73c-54a8-3c8c-968e-763bc6f32765 | -12.1132 | -50.5929 | 2026-08-24 14:00:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 181.5 |
| 749b825e-25a4-382f-8767-169a6c576436 | -7.2979 | -43.0137 | 2026-08-24 14:00:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 125.6 |
| 6345e047-b107-3ebc-91ac-64e4fa95af18 | -9.0311 | -50.7183 | 2026-08-24 14:00:00 | GOES-19 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 100.5 |
| 2e38ff45-3e45-383e-ab7f-f416fa967f73 | -7.2193 | -60.6316 | 2026-08-24 14:00:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 53.5 |
| e2f74992-7c32-3324-ac38-fbba80d470b9 | -6.8305 | -52.5061 | 2026-08-24 14:00:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 93.6 |
| c840b96b-baef-3a77-96a5-6c9d23d104e1 | -10.0871 | -46.3621 | 2026-08-24 14:00:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 94.6 |
| 219dcbec-4fb9-3a09-93b5-3e194261f7e8 | -13.8954 | -54.0508 | 2026-08-24 14:00:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 90.4 |
| 02d5ca6b-2939-3969-820b-5f2c4e0f6675 | -15.2648 | -52.8747 | 2026-08-24 14:00:00 | GOES-19 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 78.8 |
| 2a47de6a-c7b9-3c34-a325-6a5b95e65f4b | -12.1135 | -50.5714 | 2026-08-24 14:00:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 84.1 |
| f1bb6089-047d-35c4-943e-08e42c51dc6a | -16.434 | -49.9125 | 2026-08-24 14:00:00 | GOES-19 | ANICUNS | GOIÁS | Brasil | 5201306 | 52 | 33 | nan | nan | nan | Cerrado | 73.9 |
| 21da16dd-64c1-3c3e-b06b-5d49cdffc0ff | -15.3241 | -53.9407 | 2026-08-24 14:00:00 | GOES-19 | POXORÉU | MATO GROSSO | Brasil | 5107008 | 51 | 33 | nan | nan | nan | Cerrado | 87.4 |
| 092ac7a5-c97c-3775-a4be-01f287d7b49e | -13.8957 | -54.03 | 2026-08-24 14:10:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 95.4 |
| 92e3f3a5-8476-35ac-bb3b-acc73926eff4 | -14.3737 | -52.9903 | 2026-08-24 14:10:00 | GOES-19 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 112.9 |
| 50743b47-bd79-3ed4-84c6-e03722ff5c3b | -6.8491 | -52.505 | 2026-08-24 14:10:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 92.8 |
| 1938ba25-d457-30d4-be07-e371d69d9924 | -12.1132 | -50.5929 | 2026-08-24 14:10:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 225.1 |
| 7164c380-4d0a-398c-b541-269b86b6dd15 | -9.0311 | -50.7183 | 2026-08-24 14:10:00 | GOES-19 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 193.9 |
| b5b98137-21df-3a3f-b421-bbe89acc9729 | -12.0941 | -50.5951 | 2026-08-24 14:10:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 93.2 |
| 5fe7db64-1c8f-3231-8da6-402d73fd6526 | -14.3933 | -52.9667 | 2026-08-24 14:10:00 | GOES-19 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 92.4 |
| b25fa2df-0266-3a2d-b08b-017e80d4c1d4 | -12.1135 | -50.5714 | 2026-08-24 14:10:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 81.8 |
| 6d8218f4-0d23-3bbc-9dbd-405e8075c1a5 | -7.4882 | -44.4601 | 2026-08-24 14:10:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 175.1 |
| 9fad7fb8-07ea-37de-9f47-d59dfe2ee4a0 | -7.8277 | -47.6602 | 2026-08-24 14:10:00 | GOES-19 | BARRA DO OURO | TOCANTINS | Brasil | 1703073 | 17 | 33 | nan | nan | nan | Cerrado | 88.9 |
| 9b06e708-23d3-3900-a2f3-f3ede8bcc54c | -7.2979 | -43.0137 | 2026-08-24 14:10:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 131.3 |
| a035dbbe-85cf-3f90-9f35-a4fe2faf3359 | -14.2781 | -51.7953 | 2026-08-24 14:10:00 | GOES-19 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 71.6 |
| 1b1be713-7233-3f95-97f3-40905e786278 | -8.5788 | -54.7162 | 2026-08-24 14:10:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 60.9 |
| 3ff5066b-82cb-3beb-9463-a24dbba2f187 | -10.7988 | -50.9305 | 2026-08-24 14:10:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 95.6 |
| d57e8ce1-658b-3fee-a866-e58a58321e65 | -10.7796 | -50.9537 | 2026-08-24 14:10:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 75.8 |
| e6b1eb6b-0f12-3cc7-b8c6-2dbbe3a34fcf | -10.0867 | -46.3846 | 2026-08-24 14:10:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 107.0 |
| fb0588e0-5b91-3a8a-b263-af1a53f70467 | -15.2854 | -52.8084 | 2026-08-24 14:10:00 | GOES-19 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 86.6 |
| 8d3d02a9-9b77-37d8-bba4-f6abe3fd7029 | -7.2901 | -45.3683 | 2026-08-24 14:10:00 | GOES-19 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 240.4 |
| 7680926d-b0f3-324c-a95b-16a0594319e0 | -6.5408 | -45.2962 | 2026-08-24 14:10:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 102.3 |
| 99de4570-b557-3b06-a8dc-f967f78f162d | -12.1128 | -50.6143 | 2026-08-24 14:10:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 88.1 |
| 0e0f33fd-72dd-3341-8d86-4e0a847c7cc8 | -15.208 | -52.7976 | 2026-08-24 14:10:00 | GOES-19 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 83.3 |
| cbcb2ede-d80c-3c6d-bacb-002babe344e2 | -10.0677 | -46.3869 | 2026-08-24 14:10:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 98.1 |
| b10b5384-144a-3a24-b49a-ed3f1158982b | -13.1512 | -51.3854 | 2026-08-24 14:10:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 95.3 |
| 1cafa80f-da9a-372f-89ba-0bab7327168a | -14.9396 | -52.6428 | 2026-08-24 14:10:00 | GOES-19 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 82.1 |
| 4360c236-c4b9-39d1-9aaf-479d9a5b980a | -14.393 | -52.9878 | 2026-08-24 14:10:00 | GOES-19 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 147.4 |
| ef0caff2-eb3c-30a8-aba9-69cc2f87892c | -9.7131 | -46.0229 | 2026-08-24 14:10:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 102.8 |
| 8766cd31-dfff-30fa-9890-67c08712f9dd | -7.2193 | -60.6316 | 2026-08-24 14:10:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 66.8 |
| d6048b5b-65c6-3a6f-a53f-375ed4523265 | -13.8954 | -54.0508 | 2026-08-24 14:10:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 112.3 |
| 04b5dd7c-707e-3755-9a66-01c804589fac | -7.2713 | -45.37 | 2026-08-24 14:10:00 | GOES-19 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 100.1 |
| 6e3d3d01-7608-3e37-aaf6-80169b8efc64 | -10.7985 | -50.9518 | 2026-08-24 14:10:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 122.1 |
| 0c91ed07-f264-37d7-a00a-e3d1bbd8660b | -15.2648 | -52.8747 | 2026-08-24 14:10:00 | GOES-19 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 97.4 |
| 2c29c8ca-1e07-3078-865e-01eae4616656 | -6.332 | -54.7674 | 2026-08-24 14:10:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 319.5 |
| 31c60d76-dec5-3de6-9f33-6fac4cc9add5 | -10.8174 | -50.9498 | 2026-08-24 14:10:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 91.8 |
| a7b3fca8-f315-3f3f-8b23-6a902dd56df3 | -8.5787 | -54.7364 | 2026-08-24 14:10:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 61.5 |
| bfdc5cbf-c6e5-309f-8940-a83e85b232a2 | -12.0566 | -50.5567 | 2026-08-24 14:10:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 111.2 |
| fbb2ff5b-a012-3395-9f06-8f5ac1416266 | -9.068 | -50.7784 | 2026-08-24 14:10:00 | GOES-19 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 147.1 |
| bb7b8a68-5eb5-3cd3-819c-f3f2e971cb04 | -13.1879 | -51.4874 | 2026-08-24 14:10:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 85.8 |
| 832e6848-f153-3d38-a71e-7bcd0b54dc1a | -6.3507 | -54.7464 | 2026-08-24 14:10:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 406.2 |
| 4f2c33b6-426d-3549-bc68-10ae2cb8afed | -9.7134 | -46.0003 | 2026-08-24 14:10:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 82.1 |
| 8962f266-4435-395c-a4cf-22ecfe464609 | -6.1542 | -53.7077 | 2026-08-24 14:10:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 103.5 |
| 832ce48d-ecf9-359e-9c23-8edb0099503c | -11.58 | -46.9594 | 2026-08-24 14:10:00 | GOES-19 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 81.2 |
| eaa4562c-df35-31a9-86fe-ea36aed32a51 | -6.1544 | -53.6874 | 2026-08-24 14:10:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 123.8 |
| 5a1679aa-4a89-393d-88a3-2c4ef627f9c3 | -6.3322 | -54.7473 | 2026-08-24 14:10:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 170.1 |
| e783d71f-024d-315f-8991-6dca1898f727 | -6.3692 | -54.7455 | 2026-08-24 14:10:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 79.5 |
| 86a6dbda-d52d-3d90-b6b7-80759bb4fce6 | -6.8305 | -52.5061 | 2026-08-24 14:10:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 75.5 |
| 1b5cab2c-68a6-3d6a-8db0-4d3b6fb62fe4 | -10.0871 | -46.3621 | 2026-08-24 14:10:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 92.4 |
| 4c30b1e5-56c4-3b3b-8d93-cf1ffa7ab508 | -7.828 | -47.6383 | 2026-08-24 14:10:00 | GOES-19 | BARRA DO OURO | TOCANTINS | Brasil | 1703073 | 17 | 33 | nan | nan | nan | Cerrado | 73.9 |
| 2188ab03-a78a-30c1-9ca1-2dc89d06a1f6 | -14.2402 | -51.7576 | 2026-08-24 14:10:00 | GOES-19 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 76.4 |
| 6a0d3607-2eca-38d5-a974-1e0ebea24043 | -6.5596 | -45.2947 | 2026-08-24 14:10:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 180.1 |
| 3c9c40a4-996d-3831-ad49-501b57b2f03d | -7.507 | -44.4583 | 2026-08-24 14:10:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 360.1 |
| ea49c7d3-88bc-3b80-98e5-72db9ef2e626 | -14.2537 | -52.0964 | 2026-08-24 14:10:00 | GOES-19 | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 67.6 |
| eb7c302a-2f4c-3ca4-bcec-0cf4be7165fd | -10.4463 | -50.4353 | 2026-08-24 14:10:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 245.1 |
| 6f929471-d3eb-3893-865d-bf4c7ef3adef | -14.2785 | -51.7739 | 2026-08-24 14:10:00 | GOES-19 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 83.9 |
| 53e34d14-a898-3ff8-9704-62b1e9f09d0a | -6.34 | -54.74 | 2026-08-24 14:15:00 | MSG-03 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| bdb59810-90f9-301c-a5f1-02cb88e0e2a4 | -6.34 | -54.81 | 2026-08-24 14:15:00 | MSG-03 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 19c6802e-d879-31fa-9456-8be0f894c90f | -10.0677 | -46.3869 | 2026-08-24 14:20:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 111.4 |
| 3121e6be-0078-3f4e-94c9-3bbfc7f74e0a | -16.434 | -49.9125 | 2026-08-24 14:20:00 | GOES-19 | ANICUNS | GOIÁS | Brasil | 5201306 | 52 | 33 | nan | nan | nan | Cerrado | 79.6 |
| b7b53072-17ee-3142-90ec-21fb749d76c5 | -7.507 | -44.4583 | 2026-08-24 14:20:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 299.3 |
| 6938964f-08e9-371b-a614-454ab238873c | -7.2713 | -45.37 | 2026-08-24 14:20:00 | GOES-19 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 104.6 |


[Clique aqui para ver as próximas entradas](README54.md)
