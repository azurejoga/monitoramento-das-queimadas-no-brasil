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

## Dados Diários - Página 126

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 9dc226ff-3ecb-33bf-9ebb-643d2e4b4c5e | -2.0768 | -56.4282 | 2026-09-19 16:10:00 | GOES-19 | TERRA SANTA | PARÁ | Brasil | 1507979 | 15 | 33 | nan | nan | nan | Amazônia | 73.5 |
| 4d29bca5-9d29-3357-bc66-119f624da814 | -5.6408 | -43.392 | 2026-09-19 16:10:00 | GOES-19 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 221.3 |
| 3a0892f1-cb04-3a7f-94b0-dc8d4e83b9f9 | 1.3817 | -56.0636 | 2026-09-19 16:10:00 | GOES-19 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 72.4 |
| 0f7a827a-3db9-385b-ab39-bd074098827d | -11.8549 | -50.0437 | 2026-09-19 16:10:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 127.2 |
| 7a1cb193-7098-31ac-8950-e21439481a6e | -2.6966 | -57.5889 | 2026-09-19 16:10:00 | GOES-19 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 64.9 |
| 0c8df289-89e2-3ff8-b889-003bc6e75e86 | -6.1838 | -47.5258 | 2026-09-19 16:10:00 | GOES-19 | TOCANTINÓPOLIS | TOCANTINS | Brasil | 1721208 | 17 | 33 | nan | nan | nan | Cerrado | 116.5 |
| 836d2c25-27d6-347a-89a5-c24a356d9995 | -3.331 | -59.8292 | 2026-09-19 16:10:00 | GOES-19 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 105.7 |
| 42495291-3b5e-326b-adf2-97c5475979ae | -10.932 | -50.8742 | 2026-09-19 16:10:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 171.7 |
| 9359fc85-c6cb-30a0-8cf5-61e12e458c32 | -12.1527 | -46.9933 | 2026-09-19 16:10:00 | GOES-19 | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 85.8 |
| ee1e90d1-97a7-3439-84c4-912aab4f0948 | -2.8975 | -57.7793 | 2026-09-19 16:10:00 | GOES-19 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 76.7 |
| 30345e75-2907-3e82-852a-9b0f371d1ab4 | -3.4462 | -57.9812 | 2026-09-19 16:10:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 65.2 |
| f7d049ee-116c-335f-b5d8-3e962fd63ee2 | -11.9303 | -50.0993 | 2026-09-19 16:10:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 209.8 |
| 87c9c1d0-e5db-3e47-a7fb-fc16fcd00ea3 | -7.8601 | -44.8366 | 2026-09-19 16:10:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 304.2 |
| d9f0dbb2-1645-35ea-8a71-3aef795f14f7 | -12.5036 | -50.0291 | 2026-09-19 16:10:00 | GOES-19 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 628.4 |
| 46f37db2-1e30-38a8-ad5b-152305432dee | -3.3638 | -61.3093 | 2026-09-19 16:10:00 | GOES-19 | CAAPIRANGA | AMAZONAS | Brasil | 1300839 | 13 | 33 | nan | nan | nan | Amazônia | 163.3 |
| 8954b9d5-fc14-3470-a4db-8f97a38fc74b | -10.9133 | -50.8549 | 2026-09-19 16:10:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 138.3 |
| c3b91592-32ad-3539-ab86-a44ebcfe74bc | -11.8553 | -50.0221 | 2026-09-19 16:10:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 147.9 |
| c383c6a4-9191-372e-9810-111e820e1adb | -3.4461 | -58.0005 | 2026-09-19 16:10:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 57.0 |
| 4dfdb214-a826-3e0b-992a-48221237f169 | -12.5032 | -50.0508 | 2026-09-19 16:10:00 | GOES-19 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 533.9 |
| 66f5d789-6e10-3c09-b95c-d031141daa3f | -11.7313 | -50.68 | 2026-09-19 16:10:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 120.5 |
| 7dc84ab2-5d70-3b71-befe-e866ff360a57 | -3.1816 | -61.1235 | 2026-09-19 16:10:00 | GOES-19 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 103.0 |
| c4b7a4fc-6297-39fb-bdba-7bcc4007fc03 | -10.809 | -50.1836 | 2026-09-19 16:10:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 162.1 |
| 829ed862-fe88-32e3-94e8-5f1155e7febe | -10.913 | -50.8762 | 2026-09-19 16:10:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 147.5 |
| e96dbbfb-cdfb-3c3c-8b23-2ddb7adbf459 | -11.4715 | -50.2603 | 2026-09-19 16:10:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 146.8 |
| 87521e2b-9c69-3980-aacd-2645cc8c1e7e | -11.3433 | -44.0376 | 2026-09-19 16:10:00 | GOES-19 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 154.6 |
| 79247066-f3a4-3487-ad72-bfbd0bee484f | -10.7133 | -50.258 | 2026-09-19 16:10:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 167.3 |
| f95afbd8-2f5b-35cd-9000-1cc945e66618 | -11.9356 | -49.7535 | 2026-09-19 16:10:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 99.4 |
| e1565c99-5611-3b74-a20c-702ad82c62b6 | -3.1816 | -61.1045 | 2026-09-19 16:10:00 | GOES-19 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 92.6 |
| 3f2dfdb9-1b95-3108-bfdb-65a0ab875acd | -3.4278 | -58.0009 | 2026-09-19 16:10:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 54.2 |
| 751416d9-0f28-3591-8c57-520becad46bf | -7.7118 | -44.6451 | 2026-09-19 16:10:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 252.3 |
| 2d3f48e4-e5a9-3bc8-b3bf-bcefb1753007 | -6.1836 | -47.5477 | 2026-09-19 16:10:00 | GOES-19 | TOCANTINÓPOLIS | TOCANTINS | Brasil | 1721208 | 17 | 33 | nan | nan | nan | Cerrado | 115.7 |
| 1b2b84a7-7724-3b0e-8b4d-12733549fdd2 | -3.3638 | -61.2904 | 2026-09-19 16:10:00 | GOES-19 | CAAPIRANGA | AMAZONAS | Brasil | 1300839 | 13 | 33 | nan | nan | nan | Amazônia | 112.3 |
| 206177cb-b3b7-3ad1-8b3d-f7bf5e27dfc2 | -10.8367 | -50.9266 | 2026-09-19 16:10:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 83.6 |
| 462ae5be-d382-33e6-a104-cf01f9981c6c | -10.2821 | -50.0035 | 2026-09-19 16:10:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 97.4 |
| f5d0f018-b788-33d8-a2df-0b17bbf14628 | -12.4841 | -50.0532 | 2026-09-19 16:10:00 | GOES-19 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 89.9 |
| bc0f48a7-a1ec-3c3f-be22-6036d540fd86 | -3.3321 | -59.4469 | 2026-09-19 16:10:00 | GOES-19 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 56.8 |
| 0890d64e-5195-357c-afe0-077523917fcf | -12.52 | -50.09 | 2026-09-19 16:15:00 | MSG-03 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| dce7a2c1-c360-303b-938d-27542f4efaca | -5.65 | -43.4 | 2026-09-19 16:15:00 | MSG-03 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 65eacf6b-6f44-3a9d-a835-7bcc90f2e103 | -12.7 | -46.07 | 2026-09-19 16:15:00 | MSG-03 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 07bc7717-7277-3585-a812-3d196594a750 | -13.24 | -51.76 | 2026-09-19 16:15:00 | MSG-03 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 5cf332f1-728a-3b53-bb90-e2b2c6dafcae | -13.9 | -48.01 | 2026-09-19 16:15:00 | MSG-03 | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| ad208c7f-4336-3930-8a43-4a33d24eab7d | -11.14 | -54.04 | 2026-09-19 16:15:00 | MSG-03 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 93a6e888-cd4a-360f-a9ca-70ddc7713ba7 | -12.52 | -50.04 | 2026-09-19 16:15:00 | MSG-03 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| b0ba5836-1509-3486-8c16-5bb79e63be3f | -4.29 | -48.63 | 2026-09-19 16:15:00 | MSG-03 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 37319e48-ad1c-3220-ba9a-b08475e3d139 | -12.49 | -50.08 | 2026-09-19 16:15:00 | MSG-03 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 30238298-a9f6-3a3f-a32a-1ce85059f083 | -12.01 | -50.03 | 2026-09-19 16:15:00 | MSG-03 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 6471f42b-da02-3aa2-9a72-720ce8600716 | -3.99 | -41.29 | 2026-09-19 16:15:00 | MSG-03 | SÃO JOÃO DA FRONTEIRA | PIAUÍ | Brasil | 2209872 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 6a69e4ea-c4c0-3454-99fa-abd09240c707 | -11.47 | -45.35 | 2026-09-19 16:15:00 | MSG-03 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 7644ecee-49ab-3e30-9568-83cd7690f229 | -10.932 | -50.8742 | 2026-09-19 16:20:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 146.1 |
| 7ebba03d-2adf-36b3-9e45-e624cb2e623d | -3.1816 | -61.1045 | 2026-09-19 16:20:00 | GOES-19 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 106.6 |
| cb5fa366-7a31-3324-90df-72e9eaee5929 | -10.913 | -50.8762 | 2026-09-19 16:20:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 171.7 |
| cf6b2b12-6eac-39f1-b8f3-b2a8d4603cc4 | -10.9133 | -50.8549 | 2026-09-19 16:20:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 166.3 |
| 7350a44c-12a1-376f-ae8f-75a2f5090de1 | -10.8469 | -50.1795 | 2026-09-19 16:20:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 230.1 |
| 2dfe895c-da30-3301-96b4-8ec96e030f28 | -11.3241 | -44.0404 | 2026-09-19 16:20:00 | GOES-19 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 158.6 |
| 1ed39b6c-65cc-3317-8dcb-24bc607f55c0 | -7.8601 | -44.8366 | 2026-09-19 16:20:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 279.4 |
| c1fd1d91-5631-32cc-9fc1-824bcd142413 | -3.3455 | -61.2908 | 2026-09-19 16:20:00 | GOES-19 | CAAPIRANGA | AMAZONAS | Brasil | 1300839 | 13 | 33 | nan | nan | nan | Amazônia | 102.9 |
| 50ca9e18-c5dc-3e08-a9e5-8b2dd96165c4 | -3.7311 | -60.6018 | 2026-09-19 16:20:00 | GOES-19 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 96.1 |
| 069b6176-eb1e-3bb7-9ca2-ace1f57e3c26 | -10.8367 | -50.9266 | 2026-09-19 16:20:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 90.9 |
| 072f9f15-94cb-3f87-9c1c-d47ce11924d3 | -10.7715 | -46.3001 | 2026-09-19 16:20:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 114.2 |
| 4a45384c-5c6b-301c-9ea3-8c09818873f2 | -2.0768 | -56.4282 | 2026-09-19 16:20:00 | GOES-19 | TERRA SANTA | PARÁ | Brasil | 1507979 | 15 | 33 | nan | nan | nan | Amazônia | 73.5 |
| 5bde3c29-d28d-3f16-87c3-de7a980af0d0 | 1.2059 | -50.7685 | 2026-09-19 16:20:00 | GOES-19 | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 57.0 |
| 4556eeff-4f06-3514-89db-d044818bc2e7 | -10.7546 | -46.1667 | 2026-09-19 16:20:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 163.1 |
| 191cabfe-dd50-39a4-adcf-49587ed23642 | -10.809 | -50.1836 | 2026-09-19 16:20:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 127.7 |
| bf3a0883-4573-3406-8964-1b4f83d97546 | -7.7118 | -44.6451 | 2026-09-19 16:20:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 198.8 |
| a6c8ad33-a243-3ac6-b64a-5bc5a778c504 | -10.7994 | -50.8881 | 2026-09-19 16:20:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 109.5 |
| ee72ac47-eeed-3f7e-a61a-5da087dd0fd4 | -11.8549 | -50.0437 | 2026-09-19 16:20:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 101.0 |
| 38a4ca71-a4a8-3118-8efc-75e92c3cbdef | -11.8556 | -50.0006 | 2026-09-19 16:20:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 99.3 |
| 3d3511e3-7926-3994-91c1-bc69777a1881 | -6.1836 | -47.5477 | 2026-09-19 16:20:00 | GOES-19 | TOCANTINÓPOLIS | TOCANTINS | Brasil | 1721208 | 17 | 33 | nan | nan | nan | Cerrado | 129.8 |
| e89802ed-b589-3ec9-8d4a-850cf452bb63 | -11.7313 | -50.68 | 2026-09-19 16:20:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 182.8 |
| 1023af14-869d-371d-ae27-cae1f4417219 | -3.4461 | -58.0005 | 2026-09-19 16:20:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 57.9 |
| 32f4b75a-14d5-37d8-9e20-0bc82cf40db0 | -11.9303 | -50.0993 | 2026-09-19 16:20:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 191.7 |
| c9b5c3d0-067e-3afa-8687-cb1003a531e2 | -10.7133 | -50.258 | 2026-09-19 16:20:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 168.8 |
| 78bd6dbe-c725-39a2-a67e-d603480c21c3 | -3.1904 | -57.7734 | 2026-09-19 16:20:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 43.4 |
| 049cb076-99e6-3de1-a7e1-b0e9dfc8ce4c | -11.8553 | -50.0221 | 2026-09-19 16:20:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 108.0 |
| d6422d80-29b5-3809-bcc8-a880afc40f9d | -7.7847 | -44.8441 | 2026-09-19 16:20:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 150.3 |
| 6854c828-9098-3313-821a-ad7541be5230 | -11.3609 | -44.1286 | 2026-09-19 16:20:00 | GOES-19 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 186.4 |
| b46669fd-6486-3197-a2be-fe4a47b4c6f7 | -12.0086 | -49.9606 | 2026-09-19 16:20:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 183.9 |
| 5e93b258-dcbd-38f9-8af7-211b7b0d802e | -11.4715 | -50.2603 | 2026-09-19 16:20:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 109.4 |
| df13a1dd-bacf-3f75-86f4-2d497abed8fd | -6.1838 | -47.5258 | 2026-09-19 16:20:00 | GOES-19 | TOCANTINÓPOLIS | TOCANTINS | Brasil | 1721208 | 17 | 33 | nan | nan | nan | Cerrado | 157.0 |
| 75c60be6-6f12-3155-91d3-b1a64fa97f1a | -7.7844 | -44.8669 | 2026-09-19 16:20:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 140.6 |
| 9af0d37e-2785-3a06-918b-124cd0ea67f3 | 1.3817 | -56.0636 | 2026-09-19 16:20:00 | GOES-19 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 78.0 |
| 3292a7bf-df34-32ca-a4c8-568596f75877 | -10.8466 | -50.2009 | 2026-09-19 16:20:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 152.2 |
| e8d316bd-bdaf-3f31-bd27-942c572345af | -2.6966 | -57.5889 | 2026-09-19 16:20:00 | GOES-19 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 72.8 |
| e88d1eb2-88c9-33fc-9f2f-3052d261e40b | -3.1816 | -61.1235 | 2026-09-19 16:20:00 | GOES-19 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 123.6 |
| d18af918-72d5-32c3-a198-6daa15d46cfe | -3.4462 | -57.9812 | 2026-09-19 16:20:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 77.0 |
| 48d2bf95-c275-35f9-8986-a68e8c1e8bb2 | -11.9112 | -50.1016 | 2026-09-19 16:20:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 206.0 |
| ef04a1bb-9770-32be-8d74-1912ddf597b6 | -6.1836 | -47.5477 | 2026-09-19 16:30:00 | GOES-19 | TOCANTINÓPOLIS | TOCANTINS | Brasil | 1721208 | 17 | 33 | nan | nan | nan | Cerrado | 112.6 |
| 20ca315e-c1ab-3ace-b788-f760eaa63226 | -11.8549 | -50.0437 | 2026-09-19 16:30:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 115.1 |
| 63a2b2ca-5bb2-3d99-8bb5-e1d8fab5bc8a | -10.7546 | -46.1667 | 2026-09-19 16:30:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 202.1 |
| b5d4c9e6-9217-344d-953a-1561d9341631 | -10.9127 | -50.8974 | 2026-09-19 16:30:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 127.3 |
| 18aa770b-302f-3aca-914d-07d395de9cd4 | -10.7133 | -50.258 | 2026-09-19 16:30:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 165.6 |
| 9fdd259f-540e-3e46-9ba9-abb664aa7e96 | -10.9133 | -50.8549 | 2026-09-19 16:30:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 136.3 |
| 74d20d7d-86d1-3e59-b9a6-d7b1c2039763 | -3.8039 | -60.7332 | 2026-09-19 16:30:00 | GOES-19 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 90.1 |
| 6f1cd746-5895-3527-80a2-f1af4def05c3 | 1.3817 | -56.0636 | 2026-09-19 16:30:00 | GOES-19 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 74.9 |
| 53be6af0-0d92-32ce-907c-c7ac5cff873b | -10.8469 | -50.1795 | 2026-09-19 16:30:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 235.3 |
| 0cb0252a-1454-3022-8912-4d0e8a04c6b2 | -3.1816 | -61.1045 | 2026-09-19 16:30:00 | GOES-19 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 102.3 |
| 91c520cd-1ca6-377f-9826-88e2cd9f69a7 | -10.7991 | -50.9093 | 2026-09-19 16:30:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 81.2 |
| ef2b5bb6-dbac-3063-81a1-4c01b22cc832 | -10.8466 | -50.2009 | 2026-09-19 16:30:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 138.8 |
| c68182d1-bf12-35fb-b92f-2d877085dec9 | -11.3241 | -44.0404 | 2026-09-19 16:30:00 | GOES-19 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 181.0 |
| 4a1d0c44-b312-32c4-baad-00b670911592 | -10.7994 | -50.8881 | 2026-09-19 16:30:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 120.0 |


[Clique aqui para ver as próximas entradas](README127.md)
