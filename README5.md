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

## Dados Diários - Página 5

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 26481ec1-6a79-3caf-9924-691a0f85d766 | -7.36863 | -48.14301 | 2026-07-15 04:40:00 | NOAA-21 | ARAGUAÍNA | TOCANTINS | Brasil | 1702109 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 6deaf990-3ae0-3a92-926c-01d528b50842 | -9.73799 | -49.04525 | 2026-07-15 04:40:00 | NOAA-21 | DIVINÓPOLIS DO TOCANTINS | TOCANTINS | Brasil | 1707108 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 95422c94-6da5-306a-950f-c94a5587f5e9 | -8.50258 | -49.56388 | 2026-07-15 04:40:00 | NOAA-21 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 32963039-55e9-341d-a58f-1caddc874de3 | -11.4584 | -45.12766 | 2026-07-15 04:40:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 3aad4493-0030-3686-93ef-52abe7b5627f | -8.7421 | -49.4445 | 2026-07-15 04:40:00 | NOAA-21 | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| f2d5a1fb-ae17-39e5-a487-d686bc4e41a3 | -8.43926 | -51.56354 | 2026-07-15 04:40:00 | NOAA-21 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| dd5131bd-1314-3898-9a55-f1ac88874b39 | -11.45428 | -45.12712 | 2026-07-15 04:40:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 4bb4fab8-e859-3237-9c5f-bc870dce4d64 | -11.49515 | -49.80336 | 2026-07-15 04:40:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| e64bc51e-4824-3e14-9d8c-53a964016723 | -9.18449 | -50.8782 | 2026-07-15 04:40:00 | NOAA-21 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| a63787ab-42c0-384d-bb36-028fbb06570f | -5.62813 | -49.19125 | 2026-07-15 04:40:00 | NOAA-21 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 82941dca-d47b-3560-b5f0-659ac0cefe8a | -11.42419 | -47.52677 | 2026-07-15 04:40:00 | NOAA-21 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 5a27375a-10da-38b8-be2c-5b0e5cdcdd62 | -10.48376 | -49.14639 | 2026-07-15 04:40:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| e9395f57-b955-3417-9aa9-642c1c2bb1dd | -13.44016 | -43.8572 | 2026-07-15 04:40:00 | NOAA-21 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 1b648029-d635-3e13-83b6-8385113fdb0f | -11.43369 | -47.53674 | 2026-07-15 04:40:00 | NOAA-21 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| d3ae70b1-fac7-3bf6-b009-9a0db7adb7de | -7.906 | -48.26506 | 2026-07-15 04:40:00 | NOAA-21 | PALMEIRANTE | TOCANTINS | Brasil | 1715705 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 49114d3c-3987-3dd8-8b98-805a8112a9fd | -12.43756 | -49.57381 | 2026-07-15 04:40:00 | NOAA-21 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 89bb571e-65f7-3f6d-8a69-1e51108ef4b5 | -16.43227 | -51.77949 | 2026-07-15 04:42:00 | NOAA-21 | PIRANHAS | GOIÁS | Brasil | 5217203 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 50994f94-57e2-38e6-b7e0-0f038736e6de | -18.49098 | -46.9409 | 2026-07-15 04:42:00 | NOAA-21 | COROMANDEL | MINAS GERAIS | Brasil | 3119302 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 36674ba0-52a5-3d49-828f-982a06ba9c39 | -14.62907 | -54.46007 | 2026-07-15 04:42:00 | NOAA-21 | PLANALTO DA SERRA | MATO GROSSO | Brasil | 5106455 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 52509122-6768-3a6d-963f-8ca5e4fb7bfe | -16.55773 | -52.06472 | 2026-07-15 04:42:00 | NOAA-21 | CAIAPÔNIA | GOIÁS | Brasil | 5204409 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| e9a3ea29-84d3-3fb9-bd3b-d2b818c4b35b | -18.71671 | -53.27227 | 2026-07-15 04:42:00 | NOAA-21 | COSTA RICA | MATO GROSSO DO SUL | Brasil | 5003256 | 50 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 86eb8fa1-f260-360a-a6f4-d2901ffbc8bc | -19.30238 | -47.44068 | 2026-07-15 04:42:00 | NOAA-21 | SANTA JULIANA | MINAS GERAIS | Brasil | 3157708 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 923d0c84-6f8f-39e8-b539-b538649be409 | -17.34053 | -42.62615 | 2026-07-15 04:42:00 | NOAA-21 | MINAS NOVAS | MINAS GERAIS | Brasil | 3141801 | 31 | 33 | nan | nan | nan | Cerrado | 4.6 |
| b574b8e9-dc5f-3fa2-b3a9-957510af9e14 | -15.56267 | -48.03622 | 2026-07-15 04:42:00 | NOAA-21 | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 74d012d3-e4f1-3f32-b367-1822fc9eec35 | -13.12882 | -53.78408 | 2026-07-15 04:42:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| b6584cca-12fc-30c5-ae77-04799b7f2a01 | -12.87393 | -58.28256 | 2026-07-15 04:42:00 | NOAA-21 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 2.6 |
| c7115fc8-6375-3c99-ae54-a6d00a31cec7 | -15.94258 | -48.06924 | 2026-07-15 04:42:00 | NOAA-21 | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 0.9 |
| b8c8ce17-b236-3b2d-b94b-f2413da2a294 | -17.82182 | -55.06726 | 2026-07-15 04:42:00 | NOAA-21 | SONORA | MATO GROSSO DO SUL | Brasil | 5007935 | 50 | 33 | nan | nan | nan | Pantanal | 0.6 |
| 11e1a774-3b62-3206-b8c6-343427ae6950 | -17.34507 | -42.63355 | 2026-07-15 04:42:00 | NOAA-21 | MINAS NOVAS | MINAS GERAIS | Brasil | 3141801 | 31 | 33 | nan | nan | nan | Cerrado | 4.9 |
| efa6e0ba-e8d3-3143-93da-16755a47f067 | -16.16357 | -59.32153 | 2026-07-15 04:42:00 | NOAA-21 | PORTO ESPERIDIÃO | MATO GROSSO | Brasil | 5106828 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| a943b2c7-7f70-3581-ad35-a59d39fe6a7a | -18.78621 | -52.40679 | 2026-07-15 04:42:00 | NOAA-21 | CASSILÂNDIA | MATO GROSSO DO SUL | Brasil | 5002902 | 50 | 33 | nan | nan | nan | Cerrado | 2.4 |
| d51f3e56-7442-3851-a338-e16964bd11f4 | -15.93893 | -48.06861 | 2026-07-15 04:42:00 | NOAA-21 | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 6bc73415-8b2e-33ea-8a22-83fb8e467142 | -17.52661 | -44.11625 | 2026-07-15 04:42:00 | NOAA-21 | FRANCISCO DUMONT | MINAS GERAIS | Brasil | 3126604 | 31 | 33 | nan | nan | nan | Cerrado | 1.8 |
| f5a39a1f-3d93-3b12-925e-8b5e07cd0883 | -17.70468 | -46.23291 | 2026-07-15 04:42:00 | NOAA-21 | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 1c6e5eb8-85a5-3d36-be81-ffba391a774c | -12.08795 | -62.09692 | 2026-07-15 04:42:00 | NOAA-21 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 3943971b-566e-3006-b657-744b0193e8b5 | -15.77777 | -47.79904 | 2026-07-15 04:42:00 | NOAA-21 | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 1b1493bf-1955-3449-9558-8187739636db | -18.49364 | -46.95255 | 2026-07-15 04:42:00 | NOAA-21 | COROMANDEL | MINAS GERAIS | Brasil | 3119302 | 31 | 33 | nan | nan | nan | Cerrado | 17.1 |
| 7210aa40-6c82-3508-9641-34e67c26b853 | -17.34015 | -42.62959 | 2026-07-15 04:42:00 | NOAA-21 | MINAS NOVAS | MINAS GERAIS | Brasil | 3141801 | 31 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 75153a57-cdf8-3bf3-b8c8-155800902918 | -17.34544 | -42.63025 | 2026-07-15 04:42:00 | NOAA-21 | MINAS NOVAS | MINAS GERAIS | Brasil | 3141801 | 31 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 96e68503-631b-3e18-8872-f1df98dc2a65 | -18.14538 | -46.91443 | 2026-07-15 04:42:00 | NOAA-21 | LAGAMAR | MINAS GERAIS | Brasil | 3137106 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| c20dc130-ad6b-38f3-b013-4ce3902b259c | -18.1494 | -46.91503 | 2026-07-15 04:42:00 | NOAA-21 | LAGAMAR | MINAS GERAIS | Brasil | 3137106 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| ead6e632-1736-3b73-8513-22f1f19e87c0 | -13.53772 | -47.77802 | 2026-07-15 04:42:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 9af6208f-b70a-3be0-8ab8-bef22fadd7dd | -13.53834 | -47.77364 | 2026-07-15 04:42:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| d130509b-c913-3e0e-8fe3-f8a263832937 | -17.34581 | -42.62685 | 2026-07-15 04:42:00 | NOAA-21 | MINAS NOVAS | MINAS GERAIS | Brasil | 3141801 | 31 | 33 | nan | nan | nan | Cerrado | 4.6 |
| b1e382d0-0299-327d-a2ea-93775a8fca03 | -14.04388 | -54.07055 | 2026-07-15 04:42:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 3c8ddad9-3bbe-3b8a-863a-c8e4e20c7c48 | -18.7829 | -52.40622 | 2026-07-15 04:42:00 | NOAA-21 | CASSILÂNDIA | MATO GROSSO DO SUL | Brasil | 5002902 | 50 | 33 | nan | nan | nan | Cerrado | 2.4 |
| efc0f913-645d-30b1-8917-f2bf3186daef | -16.16619 | -59.32407 | 2026-07-15 04:42:00 | NOAA-21 | PORTO ESPERIDIÃO | MATO GROSSO | Brasil | 5106828 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| a369237f-164c-3b0d-8099-f411ca0e8e6d | -15.77952 | -47.7971 | 2026-07-15 04:42:00 | NOAA-21 | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 45db507e-4d40-3213-8a62-60119b8233fa | -18.14988 | -46.91132 | 2026-07-15 04:42:00 | NOAA-21 | LAGAMAR | MINAS GERAIS | Brasil | 3137106 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 0c932b08-89e4-386c-9a24-9dab6dab6977 | -18.7173 | -53.26858 | 2026-07-15 04:42:00 | NOAA-21 | COSTA RICA | MATO GROSSO DO SUL | Brasil | 5003256 | 50 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 7e4dd796-32c4-3391-ae02-1fa20b30ef6d | -17.33943 | -42.63623 | 2026-07-15 04:42:00 | NOAA-21 | MINAS NOVAS | MINAS GERAIS | Brasil | 3141801 | 31 | 33 | nan | nan | nan | Cerrado | 4.9 |
| d48c3e50-31e3-30d6-8478-d04da41a175c | -17.33979 | -42.63293 | 2026-07-15 04:42:00 | NOAA-21 | MINAS NOVAS | MINAS GERAIS | Brasil | 3141801 | 31 | 33 | nan | nan | nan | Cerrado | 4.9 |
| f500b3f3-51bc-3308-a5ad-4b4e229f1644 | -16.13306 | -47.96044 | 2026-07-15 04:42:00 | NOAA-21 | LUZIÂNIA | GOIÁS | Brasil | 5212501 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| f3be8fc3-240b-3b8b-9e5a-fd67dd0ebf4b | -18.78421 | -49.08418 | 2026-07-15 04:42:00 | NOAA-21 | CANÁPOLIS | MINAS GERAIS | Brasil | 3111804 | 31 | 33 | nan | nan | nan | Cerrado | 6.5 |
| d6437abb-63ea-3408-b898-ec5b3ccb6b78 | -16.16053 | -59.32824 | 2026-07-15 04:42:00 | NOAA-21 | PORTO ESPERIDIÃO | MATO GROSSO | Brasil | 5106828 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 83cec82d-0527-3a08-ae8a-11e3a87ce411 | -12.87484 | -58.27748 | 2026-07-15 04:42:00 | NOAA-21 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 5a527be0-a805-3ee4-ad3e-848e8fd88a39 | -11.75055 | -57.83142 | 2026-07-15 04:42:00 | NOAA-21 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 4cdd5353-4610-3024-9473-5c337d434aa4 | -16.6929 | -47.50619 | 2026-07-15 04:42:00 | NOAA-21 | CRISTALINA | GOIÁS | Brasil | 5206206 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 4f92fe26-8240-39d7-945b-0a8cbde4ecb4 | -17.52688 | -44.11548 | 2026-07-15 04:42:00 | NOAA-21 | FRANCISCO DUMONT | MINAS GERAIS | Brasil | 3126604 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 9e01d7ff-7a0a-3f26-9a5c-8491c3027184 | -19.9177 | -42.32477 | 2026-07-15 04:42:00 | NOAA-21 | BOM JESUS DO GALHO | MINAS GERAIS | Brasil | 3107802 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| 262ee0d0-79c3-36f2-80ba-3edf27b81efc | -18.49408 | -46.94903 | 2026-07-15 04:42:00 | NOAA-21 | COROMANDEL | MINAS GERAIS | Brasil | 3119302 | 31 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 2ad71321-d78f-3cfd-a66e-1ab370c548ca | -23.56071 | -47.51357 | 2026-07-15 04:44:00 | NOAA-21 | SOROCABA | SÃO PAULO | Brasil | 3552205 | 35 | 33 | nan | nan | nan | Mata Atlântica | 9.4 |
| d4aacdbd-0c1a-3298-af8c-e8e561447769 | -22.24994 | -53.33153 | 2026-07-15 04:44:00 | NOAA-21 | NOVA ANDRADINA | MATO GROSSO DO SUL | Brasil | 5006200 | 50 | 33 | nan | nan | nan | Mata Atlântica | 3.1 |
| 25773437-c2b7-3f19-a583-b92547fc58c1 | -20.65416 | -48.67686 | 2026-07-15 04:44:00 | NOAA-21 | BARRETOS | SÃO PAULO | Brasil | 3505500 | 35 | 33 | nan | nan | nan | Cerrado | 3.9 |
| f623969e-c427-3251-aec9-c6d1ea1f9924 | -22.38062 | -49.79296 | 2026-07-15 04:44:00 | NOAA-21 | LUPÉRCIO | SÃO PAULO | Brasil | 3527801 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.1 |
| 54cf7e30-bfea-35ea-acdb-ea072b4175ed | -20.22713 | -50.91706 | 2026-07-15 04:44:00 | NOAA-21 | SANTA FÉ DO SUL | SÃO PAULO | Brasil | 3546603 | 35 | 33 | nan | nan | nan | Mata Atlântica | 6.2 |
| 26d7717b-c468-3ea0-a1e1-ae94399dca87 | -23.14006 | -48.66623 | 2026-07-15 04:44:00 | NOAA-21 | ITATINGA | SÃO PAULO | Brasil | 3523503 | 35 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 0a9727e9-184c-3270-99e3-0f9dd69be511 | -21.47611 | -47.33819 | 2026-07-15 04:44:00 | NOAA-21 | SANTA ROSA DE VITERBO | SÃO PAULO | Brasil | 3547601 | 35 | 33 | nan | nan | nan | Cerrado | 2.8 |
| e32a5664-977f-3cb1-ba0d-61b5fb2e3f9d | -22.79751 | -49.35233 | 2026-07-15 04:44:00 | NOAA-21 | ÁGUAS DE SANTA BÁRBARA | SÃO PAULO | Brasil | 3500550 | 35 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 42d92053-f105-35f5-9522-01c93f7d32b8 | -20.63386 | -49.98088 | 2026-07-15 04:44:00 | NOAA-21 | NHANDEARA | SÃO PAULO | Brasil | 3532603 | 35 | 33 | nan | nan | nan | Cerrado | 1.9 |
| e6383fd0-b4cc-342b-965c-cb61cffddf53 | -23.56487 | -47.51423 | 2026-07-15 04:44:00 | NOAA-21 | SOROCABA | SÃO PAULO | Brasil | 3552205 | 35 | 33 | nan | nan | nan | Mata Atlântica | 5.9 |
| bcd3d809-a82c-3322-b81e-bb0253396e9c | -22.377 | -49.79239 | 2026-07-15 04:44:00 | NOAA-21 | LUPÉRCIO | SÃO PAULO | Brasil | 3527801 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 295b8a4c-84e6-3236-b8c0-966bf0777e35 | -23.13941 | -48.67149 | 2026-07-15 04:44:00 | NOAA-21 | ITATINGA | SÃO PAULO | Brasil | 3523503 | 35 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 7bfa9bc2-7bd4-3da0-90a2-fd0899fbc936 | -22.10098 | -46.99707 | 2026-07-15 04:44:00 | NOAA-21 | AGUAÍ | SÃO PAULO | Brasil | 3500303 | 35 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 04acecab-fee1-3a9f-af76-8bcc87b7fd44 | -19.96543 | -47.20601 | 2026-07-15 04:44:00 | NOAA-21 | SACRAMENTO | MINAS GERAIS | Brasil | 3156908 | 31 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 295cf0c4-8f71-3a50-83ea-75773a85fe93 | -20.52445 | -48.57432 | 2026-07-15 04:44:00 | NOAA-21 | BARRETOS | SÃO PAULO | Brasil | 3505500 | 35 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 8fc2b1c1-21ab-3bb8-8bff-104e553349c2 | -21.4802 | -47.33887 | 2026-07-15 04:44:00 | NOAA-21 | SANTA ROSA DE VITERBO | SÃO PAULO | Brasil | 3547601 | 35 | 33 | nan | nan | nan | Cerrado | 2.8 |
| a51432d5-a470-31c2-9006-9e028e9ec893 | -21.44384 | -54.56964 | 2026-07-15 04:44:00 | NOAA-21 | NOVA ALVORADA DO SUL | MATO GROSSO DO SUL | Brasil | 5006002 | 50 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 94b92038-dbed-33a8-a597-8d2f510a1c0f | -22.96541 | -52.70655 | 2026-07-15 04:44:00 | NOAA-21 | GUAIRAÇÁ | PARANÁ | Brasil | 4108908 | 41 | 33 | nan | nan | nan | Mata Atlântica | 5.6 |
| 70117661-4098-3abb-8003-42f692f0e9c7 | -21.54512 | -52.01459 | 2026-07-15 04:44:00 | NOAA-21 | PRESIDENTE EPITÁCIO | SÃO PAULO | Brasil | 3541307 | 35 | 33 | nan | nan | nan | Mata Atlântica | 3.3 |
| 657d5e5f-0c95-3702-980a-d8da7eb75de5 | -23.55282 | -47.43692 | 2026-07-15 04:44:00 | NOAA-21 | VOTORANTIM | SÃO PAULO | Brasil | 3557006 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 635c56d1-1060-3a95-aa98-66a2231fd716 | -19.9614 | -47.20524 | 2026-07-15 04:44:00 | NOAA-21 | SACRAMENTO | MINAS GERAIS | Brasil | 3156908 | 31 | 33 | nan | nan | nan | Cerrado | 0.5 |
| b0e28884-8bd1-39fc-82c3-4983d9e7dc0c | -21.42247 | -48.4852 | 2026-07-15 04:44:00 | NOAA-21 | TAQUARITINGA | SÃO PAULO | Brasil | 3553708 | 35 | 33 | nan | nan | nan | Cerrado | 0.6 |
| ad96fbb7-e6e2-3f22-84cc-b7f9d5f76dc3 | -23.79662 | -48.44907 | 2026-07-15 04:44:00 | NOAA-21 | BURI | SÃO PAULO | Brasil | 3508009 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.5 |
| 8d65d29e-9101-388d-9fdf-43f66667a2ad | -22.24533 | -52.88082 | 2026-07-15 04:44:00 | NOAA-21 | ANAURILÂNDIA | MATO GROSSO DO SUL | Brasil | 5000807 | 50 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 3b78f12d-e8ba-3c1b-8d1a-bd29de1c284c | -29.18949 | -51.99509 | 2026-07-15 04:46:00 | NOAA-21 | NOVA BRÉSCIA | RIO GRANDE DO SUL | Brasil | 4313003 | 43 | 33 | nan | nan | nan | Mata Atlântica | 15.0 |
| d403c8bb-bca3-300e-a85d-c9069c8c13ab | -1.66529 | -54.45994 | 2026-07-15 05:31:00 | NOAA-20 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 800ede14-2079-3553-bcb0-72ee21a9a832 | -1.66077 | -54.45919 | 2026-07-15 05:31:00 | NOAA-20 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| b9451388-3cd2-3743-886c-a808bf2343e0 | -3.15108 | -48.58376 | 2026-07-15 05:31:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 4f2f201b-90a8-33aa-b3d3-7a6e56c3e218 | -0.0905 | -51.27959 | 2026-07-15 05:31:00 | NOAA-20 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 4cb1ae29-7523-3cdd-8c74-075391e79b55 | -1.82705 | -54.48018 | 2026-07-15 05:31:00 | NOAA-20 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| c3bd8011-e19a-3bf2-833d-4eeb2f5984c1 | -1.82543 | -54.48158 | 2026-07-15 05:31:00 | NOAA-20 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 53336a0f-16c4-344c-9aba-ee8402b5b0ae | -3.15343 | -48.57999 | 2026-07-15 05:31:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 74d52050-b3ba-3404-85c4-fd6e3773900e | -3.152 | -48.57772 | 2026-07-15 05:31:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 9e47116d-780e-35d8-92c0-8a37da7c4c25 | -3.15789 | -48.58475 | 2026-07-15 05:31:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 385ff448-4ddb-36eb-a71b-fddf380258ae | -1.82252 | -54.4795 | 2026-07-15 05:31:00 | NOAA-20 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 210e6566-4155-315e-adeb-1b63852394a4 | -1.8209 | -54.4809 | 2026-07-15 05:31:00 | NOAA-20 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 22bb4ee2-3c10-3c55-9448-50ebfbf1187e | -9.74674 | -49.04903 | 2026-07-15 05:33:00 | NOAA-20 | DIVINÓPOLIS DO TOCANTINS | TOCANTINS | Brasil | 1707108 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| c84d9103-8872-36e4-b815-2b6b14869800 | -9.73956 | -49.04803 | 2026-07-15 05:33:00 | NOAA-20 | DIVINÓPOLIS DO TOCANTINS | TOCANTINS | Brasil | 1707108 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 0118a0fa-8cfc-3aba-bb33-737fd7f34220 | -9.74047 | -49.0407 | 2026-07-15 05:33:00 | NOAA-20 | DIVINÓPOLIS DO TOCANTINS | TOCANTINS | Brasil | 1707108 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |


[Clique aqui para ver as próximas entradas](README6.md)
