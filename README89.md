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

## Dados Diários - Página 89

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 1eac5e9a-8aad-3c6c-b74f-d79ee1ce7ede | -12.15829 | -50.89082 | 2025-10-07 04:57:00 | NOAA-20 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 23ddb636-66e3-3b8b-a032-f18d0faf87f5 | -9.03809 | -51.4849 | 2025-10-07 04:57:00 | NOAA-20 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 84071572-d292-337d-b619-b93e3717d64e | -10.74522 | -50.47303 | 2025-10-07 04:57:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 10.4 |
| 929f1d05-7cb5-3670-8d62-5eeee70b9fcc | -11.13308 | -47.22264 | 2025-10-07 04:57:00 | NOAA-20 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 0.5 |
| e20daf7e-7a60-3a06-948e-3916a7496ee3 | -12.97909 | -51.02621 | 2025-10-07 04:57:00 | NOAA-20 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 3.5 |
| d3a9e0ba-37fa-318e-ac67-e669c1fc505e | -15.2723 | -46.35215 | 2025-10-07 04:57:00 | NOAA-20 | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 07207654-34e0-3bee-b781-3790ded921f9 | -9.4493 | -56.65441 | 2025-10-07 04:57:00 | NOAA-20 | PARANAÍTA | MATO GROSSO | Brasil | 5106299 | 51 | 33 | nan | nan | nan | Amazônia | 5.2 |
| d2ae4905-54d9-3efd-8f2a-2bab4519a699 | -8.84848 | -46.09706 | 2025-10-07 04:57:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 1b4adeda-926d-3b91-92b5-d5f6181a432a | -11.77408 | -45.13253 | 2025-10-07 04:57:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| d62e6b68-efb8-399a-8719-d846da88137d | -12.90842 | -54.73255 | 2025-10-07 04:57:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 5.1 |
| c4868dad-fd47-3d66-be52-3d0bf7f6e818 | -11.7963 | -45.09275 | 2025-10-07 04:57:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 9a0c69b7-ff92-375a-b7b1-2d45436aa652 | -8.85442 | -46.09156 | 2025-10-07 04:57:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| d3f5217a-012f-3efc-afe8-002371ce3394 | -10.09764 | -50.52238 | 2025-10-07 04:57:00 | NOAA-20 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| b5abc7ce-55e7-36d0-a4a9-35d23fd19c08 | -13.34763 | -48.02721 | 2025-10-07 04:57:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 6174daef-b84b-3475-8101-027775143d00 | -10.94264 | -49.47825 | 2025-10-07 04:57:00 | NOAA-20 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 60f4940e-15ba-31d9-a7ba-61b0019ae5f7 | -12.73082 | -47.9371 | 2025-10-07 04:57:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 19e3da6e-3d66-3135-9bdf-09c240c37a1e | -10.3916 | -45.38411 | 2025-10-07 04:57:00 | NOAA-20 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 2.9 |
| c31b2558-15f6-3452-9b34-90f58ce711c1 | -7.47954 | -63.56413 | 2025-10-07 04:57:00 | NOAA-20 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| fcd4e219-e972-3636-bda3-82cbff08806f | -15.36544 | -47.31958 | 2025-10-07 04:57:00 | NOAA-20 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 2.8 |
| e024a988-9533-39f3-9f9a-2f7dc8c8ff20 | -10.43432 | -50.32455 | 2025-10-07 04:57:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 15.9 |
| 7bbbb2ce-ad26-3b33-ab1a-3ba070c03cae | -10.42326 | -50.31778 | 2025-10-07 04:57:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 9.5 |
| 390a694d-9533-35a0-8f65-76184b7c308e | -12.97789 | -51.02873 | 2025-10-07 04:57:00 | NOAA-20 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 2.2 |
| db1a539a-4cb0-3ad0-a638-5105eec6c78b | -12.28852 | -51.36531 | 2025-10-07 04:57:00 | NOAA-20 | SERRA NOVA DOURADA | MATO GROSSO | Brasil | 5107883 | 51 | 33 | nan | nan | nan | Cerrado | 0.7 |
| d58d9084-5b95-3980-8f3f-d23ed7b0d272 | -9.04072 | -50.59215 | 2025-10-07 04:57:00 | NOAA-20 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 5d34b6a5-5634-3859-90e7-b40188d788ae | -14.76575 | -46.04228 | 2025-10-07 04:57:00 | NOAA-20 | SÍTIO D'ABADIA | GOIÁS | Brasil | 5220702 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| f761e84d-f08a-3716-821c-5a7c805c4e0c | -15.3651 | -47.32235 | 2025-10-07 04:57:00 | NOAA-20 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 7ffa5c78-1523-37b6-9d75-b5db978798dc | -8.86549 | -50.88539 | 2025-10-07 04:57:00 | NOAA-20 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 227f542e-d089-38f6-9a72-70d18edd4f31 | -9.09135 | -47.95623 | 2025-10-07 04:57:00 | NOAA-20 | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| fe9d2e4c-64ea-3eec-a1cc-7dcf5afef1bf | -8.67692 | -49.94147 | 2025-10-07 04:57:00 | NOAA-20 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 5d607218-b808-3c54-b51d-f37ab947e77d | -14.76193 | -46.02666 | 2025-10-07 04:57:00 | NOAA-20 | SÍTIO D'ABADIA | GOIÁS | Brasil | 5220702 | 52 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 1e2e7f30-232b-3631-9b5a-4fb9ee345c15 | -11.80576 | -45.13163 | 2025-10-07 04:57:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 2d267588-ca6c-3706-a111-cd167262631f | -13.08743 | -47.8125 | 2025-10-07 04:57:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.8 |
| e65858a6-fd6a-3a62-8790-341ca70bde0b | -14.61242 | -52.49158 | 2025-10-07 04:57:00 | NOAA-20 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 455682e7-7c4e-3ba2-839c-ca29f1a24480 | -11.09765 | -47.20599 | 2025-10-07 04:57:00 | NOAA-20 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| cf365088-4a26-3f0d-91f0-02c64f2f4507 | -7.51322 | -63.43912 | 2025-10-07 04:57:00 | NOAA-20 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| f0d6df8c-ad26-3148-920b-e91c6b85b5e6 | -9.00291 | -61.64469 | 2025-10-07 04:57:00 | NOAA-20 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 2.4 |
| f6300e5e-c915-3b8f-9fab-ac316d5740d9 | -10.11229 | -58.53092 | 2025-10-07 04:57:00 | NOAA-20 | COTRIGUAÇU | MATO GROSSO | Brasil | 5103379 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 1b194ae1-967c-3ea0-84ef-f89423040077 | -7.41356 | -63.03001 | 2025-10-07 04:57:00 | NOAA-20 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 0.6 |
| fc05c5e3-69f2-30ef-9254-addd9d8891ad | -10.10718 | -51.19596 | 2025-10-07 04:57:00 | NOAA-20 | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 19836832-671f-3bb0-8b7d-c6ed807ef6e9 | -13.33054 | -47.24292 | 2025-10-07 04:57:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 195718bf-6cf8-3f53-982e-851b0048af61 | -15.88199 | -46.2535 | 2025-10-07 04:57:00 | NOAA-20 | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 89f9bc84-0d45-3bae-94eb-c73805386937 | -12.91674 | -54.7229 | 2025-10-07 04:57:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| bc472165-5f8a-3e6a-9147-50a7d972311c | -13.27914 | -47.16783 | 2025-10-07 04:57:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 13c3a9eb-b98d-384b-98f5-66748ab1277d | -10.18262 | -45.53304 | 2025-10-07 04:57:00 | NOAA-20 | SÃO GONÇALO DO GURGUÉIA | PIAUÍ | Brasil | 2209757 | 22 | 33 | nan | nan | nan | Cerrado | 2.3 |
| fc3d9a84-23df-3997-95e7-bcfd61185705 | -14.92463 | -51.40537 | 2025-10-07 04:57:00 | NOAA-20 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 2.6 |
| b8f6e56d-775c-3967-993a-e9b91e013b20 | -10.41505 | -50.29078 | 2025-10-07 04:57:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| a38c2d56-6713-3387-8081-86a59c2d1b5a | -9.00694 | -49.21791 | 2025-10-07 04:57:00 | NOAA-20 | DOIS IRMÃOS DO TOCANTINS | TOCANTINS | Brasil | 1707207 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 558276c4-54d5-3a93-a64e-1b791c038a3c | -10.92847 | -51.15716 | 2025-10-07 04:57:00 | NOAA-20 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 256608fb-14e4-35d2-beeb-301f58f2edd7 | -8.74699 | -48.86921 | 2025-10-07 04:57:00 | NOAA-20 | COLMÉIA | TOCANTINS | Brasil | 1716703 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 73bd7e55-666e-3709-92af-c4e3d4252604 | -15.55778 | -46.82628 | 2025-10-07 04:57:00 | NOAA-20 | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |
| d3179b5e-1636-3684-af90-ba5b337bb1e4 | -11.77365 | -45.13601 | 2025-10-07 04:57:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 5bc04022-d7e2-3c8b-ab13-5927256cf5b9 | -10.61282 | -48.70099 | 2025-10-07 04:57:00 | NOAA-20 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 9bfc20bf-4487-344d-927e-96e6f947bfbe | -8.85836 | -62.36629 | 2025-10-07 04:57:00 | NOAA-20 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 13644431-b916-3608-88bf-ec1441d2316a | -8.14768 | -62.83247 | 2025-10-07 04:57:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 10fefbc5-fecb-3766-8c72-4ebd44fd9c30 | -14.91227 | -46.8246 | 2025-10-07 04:57:00 | NOAA-20 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 61910226-184c-3431-ab15-761639564f5b | -10.79744 | -48.59701 | 2025-10-07 04:57:00 | NOAA-20 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 6647f0b6-db82-3999-861b-ac84e15186df | -8.84732 | -46.10571 | 2025-10-07 04:57:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| b2095e6a-e04d-3bc9-9312-a6413a52e55f | -8.93673 | -49.85596 | 2025-10-07 04:57:00 | NOAA-20 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| fe54161d-f45b-350b-8807-88e5fccb6568 | -11.9446 | -51.47094 | 2025-10-07 04:57:00 | NOAA-20 | SERRA NOVA DOURADA | MATO GROSSO | Brasil | 5107883 | 51 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 6b36693a-2eb3-31b7-a2c3-2ca40b162774 | -14.76954 | -46.05803 | 2025-10-07 04:57:00 | NOAA-20 | SÍTIO D'ABADIA | GOIÁS | Brasil | 5220702 | 52 | 33 | nan | nan | nan | Cerrado | 3.9 |
| d37af48c-f06c-304b-b92e-086ae9011051 | -11.48652 | -44.97275 | 2025-10-07 04:57:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 377fb1ef-a03a-32a7-9eae-0d9f508bd4ac | -12.24478 | -47.85664 | 2025-10-07 04:57:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 10.0 |
| e3e7b3ca-dce4-305f-891b-e6459fcf6167 | -15.22409 | -49.3153 | 2025-10-07 04:57:00 | NOAA-20 | GOIANÉSIA | GOIÁS | Brasil | 5208608 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| b999ebcc-51f5-3117-af8c-99f74ff93c02 | -9.41607 | -61.89175 | 2025-10-07 04:57:00 | NOAA-20 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 1.8 |
| cb3c71a9-b254-37f5-964f-f25720337da1 | -13.36396 | -47.25657 | 2025-10-07 04:57:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 0cd2f556-ebdb-3a14-b945-9a22be07d405 | -13.51664 | -48.62875 | 2025-10-07 04:57:00 | NOAA-20 | TROMBAS | GOIÁS | Brasil | 5221452 | 52 | 33 | nan | nan | nan | Cerrado | 3.3 |
| a492b9a8-3b15-3eff-883d-85a5098d922f | -14.76357 | -46.06095 | 2025-10-07 04:57:00 | NOAA-20 | SÍTIO D'ABADIA | GOIÁS | Brasil | 5220702 | 52 | 33 | nan | nan | nan | Cerrado | 3.9 |
| c05465bb-9562-3775-9543-9296fc868401 | -10.43505 | -50.3195 | 2025-10-07 04:57:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 15.5 |
| 87b0bb36-a49c-37e7-b0c0-fff5dc89defb | -13.34589 | -47.77161 | 2025-10-07 04:57:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| e22aeec6-9e0b-37f0-bbcd-c05cad41806f | -11.09842 | -47.20016 | 2025-10-07 04:57:00 | NOAA-20 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 8a3631c0-941a-344c-bebe-964271fc65c9 | -11.94569 | -46.44753 | 2025-10-07 04:57:00 | NOAA-20 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 9fed82c0-50d8-3d73-8a73-7dcb31f2eadb | -14.91942 | -46.80897 | 2025-10-07 04:57:00 | NOAA-20 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 410c77b3-7974-3526-a100-ffaae28e4fc2 | -13.72941 | -48.2039 | 2025-10-07 04:57:00 | NOAA-20 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 56e62ef3-a532-3322-85c8-a948f7e69946 | -12.98688 | -51.02735 | 2025-10-07 04:57:00 | NOAA-20 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 6db7b4ef-b042-3343-b44d-da4bc3390dd6 | -13.67985 | -47.33736 | 2025-10-07 04:57:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 648337fb-aafb-3b3b-9954-aa8ec0dc608c | -12.29967 | -55.11055 | 2025-10-07 04:57:00 | NOAA-20 | VERA | MATO GROSSO | Brasil | 5108501 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 5d613986-425d-30a3-b80c-fcb57b60ac64 | -11.72229 | -44.44071 | 2025-10-07 04:57:00 | NOAA-20 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| b6c80b04-406e-39b7-bbd0-bcaeb7818c46 | -10.18016 | -45.5358 | 2025-10-07 04:57:00 | NOAA-20 | SÃO GONÇALO DO GURGUÉIA | PIAUÍ | Brasil | 2209757 | 22 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 97049175-a64c-3cdf-8776-54677ec963f4 | -11.15279 | -47.75191 | 2025-10-07 04:57:00 | NOAA-20 | PINDORAMA DO TOCANTINS | TOCANTINS | Brasil | 1717008 | 17 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 2e824128-93cc-3a60-b8b8-d1aede589ab0 | -9.06182 | -54.51583 | 2025-10-07 04:57:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 010ddb5b-58b8-372c-85b6-6b7a05e39540 | -15.05316 | -42.3413 | 2025-10-07 04:57:00 | NOAA-20 | MORTUGABA | BAHIA | Brasil | 2921807 | 29 | 33 | nan | nan | nan | Caatinga | 5.4 |
| 6a4c65bf-2753-3fc2-9353-b5e43c9ab3a1 | -13.13607 | -48.006 | 2025-10-07 04:57:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 1f44de4f-76e6-3fc9-9a47-55362d1bfb0f | -7.68283 | -61.06192 | 2025-10-07 04:57:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 2aa8d967-4ef3-3009-af96-fc2869ebcce2 | -11.02161 | -51.15491 | 2025-10-07 04:57:00 | NOAA-20 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 2.6 |
| da5b0c7b-9713-3375-b014-b8ed57a68d3a | -13.00634 | -51.03019 | 2025-10-07 04:57:00 | NOAA-20 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 8.6 |
| ee379bd8-1c41-3c06-869b-f6f64ef2bd44 | -9.63484 | -57.02259 | 2025-10-07 04:57:00 | NOAA-20 | NOVA MONTE VERDE | MATO GROSSO | Brasil | 5108956 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 340431e0-5357-3e73-b119-bbac15620d10 | -10.40898 | -50.30538 | 2025-10-07 04:57:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 52.4 |
| 65b45d82-af4c-300a-bccb-d1eacd1fb19f | -10.32303 | -51.45462 | 2025-10-07 04:57:00 | NOAA-20 | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| cb018668-e3ab-35d4-952d-8ff3ab2a0f3a | -9.68619 | -48.39743 | 2025-10-07 04:57:00 | NOAA-20 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 242bca4f-0b9a-3d04-a596-754b1b31abc5 | -15.76296 | -47.77529 | 2025-10-07 04:57:00 | NOAA-20 | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 1.0 |
| f70e60b7-5bd4-386d-8834-9724574da482 | -10.03639 | -52.08507 | 2025-10-07 04:57:00 | NOAA-20 | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 83727735-d4d6-3366-8e24-1ba5de631832 | -13.23093 | -51.68732 | 2025-10-07 04:57:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 2.1 |
| c70e5b4c-e530-3922-9463-eeabe13f0e49 | -9.06498 | -49.50346 | 2025-10-07 04:57:00 | NOAA-20 | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 39c0061b-3127-3258-ad19-2dcb63913357 | -10.38608 | -50.30013 | 2025-10-07 04:57:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 14.0 |
| d56ca4b2-7c7d-3ef2-8e34-d24e7d30eaf1 | -14.28387 | -45.84792 | 2025-10-07 04:57:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 42b01e59-8200-319c-b52c-848a2079a192 | -13.6744 | -47.94784 | 2025-10-07 04:57:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 1ba0bd15-21aa-39a6-8276-8bd7f45955c6 | -12.93116 | -54.71788 | 2025-10-07 04:57:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| bad08848-0dcd-3cbb-8dd9-c1348dcefdad | -13.53503 | -42.99299 | 2025-10-07 04:57:00 | NOAA-20 | RIACHO DE SANTANA | BAHIA | Brasil | 2926400 | 29 | 33 | nan | nan | nan | Caatinga | 12.1 |
| b5559cb4-1854-3b3e-b59c-ff51860d2f40 | -11.467 | -51.49116 | 2025-10-07 04:57:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| bbb19efc-b308-3fb5-a195-0218a3152e82 | -8.10291 | -55.07948 | 2025-10-07 04:57:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.4 |


[Clique aqui para ver as próximas entradas](README90.md)
