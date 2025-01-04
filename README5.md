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
| 2df37e49-c929-36b0-95fd-47f0d575e987 | -3.26993 | -43.52131 | 2025-01-04 04:06:00 | NPP-375D | SÃO BENEDITO DO RIO PRETO | MARANHÃO | Brasil | 2110401 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 57612f16-bbcf-367b-9831-9c990486bb77 | -2.44669 | -49.02807 | 2025-01-04 04:06:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| f0d56e31-2399-3de9-aae7-530bf0733e97 | -1.99512 | -46.52501 | 2025-01-04 04:06:00 | NPP-375D | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| fba7a2e5-69f7-3bb8-af60-c1336ff231d1 | -8.83949 | -49.89706 | 2025-01-04 04:08:00 | NPP-375D | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 52523c46-23a9-3d40-936f-6c3781fa518c | -10.41875 | -39.86507 | 2025-01-04 04:08:00 | NPP-375D | ANDORINHA | BAHIA | Brasil | 2901353 | 29 | 33 | nan | nan | nan | Caatinga | 2.4 |
| ab9ab551-ceb0-349d-b15d-66acdc3fa7ab | -10.61438 | -44.34403 | 2025-01-04 04:08:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 94d0948f-69f6-35ba-84df-23cb3dd03fd8 | -9.92617 | -36.00249 | 2025-01-04 04:08:00 | NPP-375D | JEQUIÁ DA PRAIA | ALAGOAS | Brasil | 2703759 | 27 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 394931c4-98ee-34a9-b97d-212c98bd463d | -8.22855 | -42.87384 | 2025-01-04 04:08:00 | NPP-375D | BREJO DO PIAUÍ | PIAUÍ | Brasil | 2201988 | 22 | 33 | nan | nan | nan | Caatinga | 0.6 |
| 487c0881-465f-38f4-84ce-043b1b2baeaf | -5.17016 | -40.76171 | 2025-01-04 04:08:00 | NPP-375D | CRATEÚS | CEARÁ | Brasil | 2304103 | 23 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 0b6715bf-1dd4-3e4a-9b6b-dc8f524565c9 | -9.18103 | -43.11733 | 2025-01-04 04:08:00 | NPP-375D | JUREMA | PIAUÍ | Brasil | 2205532 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 5fd26f23-9772-3e48-a66d-929f659f5bb0 | -9.32019 | -43.1615 | 2025-01-04 04:08:00 | NPP-375D | JUREMA | PIAUÍ | Brasil | 2205532 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| a070a340-b32d-349b-9a26-2cff4b03916e | -4.00585 | -40.93576 | 2025-01-04 04:08:00 | NPP-375D | SÃO BENEDITO | CEARÁ | Brasil | 2312304 | 23 | 33 | nan | nan | nan | Caatinga | 2.9 |
| 645483ee-75d8-3714-8512-d9477cfe1b7c | -10.61377 | -44.34776 | 2025-01-04 04:08:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 0f6b7022-32bc-3bb8-8c57-ecdd98dcfd28 | -9.31741 | -43.15741 | 2025-01-04 04:08:00 | NPP-375D | JUREMA | PIAUÍ | Brasil | 2205532 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| f340d179-882a-3922-859e-f16758c164f0 | -7.02344 | -39.65892 | 2025-01-04 04:08:00 | NPP-375D | NOVA OLINDA | CEARÁ | Brasil | 2309201 | 23 | 33 | nan | nan | nan | Caatinga | 1.0 |
| fc7c9e2e-0fce-3a2e-b66d-1c5bc9eb7d17 | -4.16191 | -42.0231 | 2025-01-04 04:08:00 | NPP-375D | BATALHA | PIAUÍ | Brasil | 2201507 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 9f9ab1a3-21be-3b00-a3be-39d1346a7b56 | -7.99871 | -35.22443 | 2025-01-04 04:08:00 | NPP-375D | CHÃ DE ALEGRIA | PERNAMBUCO | Brasil | 2604403 | 26 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 6c294fac-bb74-36a0-b5af-c546699a9053 | -6.08289 | -39.26234 | 2025-01-04 04:08:00 | NPP-375D | ACOPIARA | CEARÁ | Brasil | 2300309 | 23 | 33 | nan | nan | nan | Caatinga | 1.8 |
| d0373c7d-4be7-3d87-ae2c-c2c75c2cfc52 | -11.13611 | -41.55738 | 2025-01-04 04:08:00 | NPP-375D | JOÃO DOURADO | BAHIA | Brasil | 2918357 | 29 | 33 | nan | nan | nan | Caatinga | 0.6 |
| 4c2306dd-4d53-3f71-816b-f5dd73d78c97 | -8.20084 | -37.66837 | 2025-01-04 04:08:00 | NPP-375D | CUSTÓDIA | PERNAMBUCO | Brasil | 2605103 | 26 | 33 | nan | nan | nan | Caatinga | 2.6 |
| c61eb1bd-0979-36fd-b96a-c55683f2eb47 | -10.50232 | -37.92982 | 2025-01-04 04:08:00 | NPP-375D | ADUSTINA | BAHIA | Brasil | 2900355 | 29 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 750592d9-75b8-3069-b115-254d6920695d | -9.98375 | -36.39017 | 2025-01-04 04:08:00 | NPP-375D | TEOTÔNIO VILELA | ALAGOAS | Brasil | 2709152 | 27 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| c530684a-621a-3c0b-9471-18e1f0bcd715 | -9.48528 | -35.99282 | 2025-01-04 04:08:00 | NPP-375D | ATALAIA | ALAGOAS | Brasil | 2700409 | 27 | 33 | nan | nan | nan | Mata Atlântica | 2.3 |
| d9095817-9357-3976-8794-41cd134d88c2 | -10.2872 | -36.36273 | 2025-01-04 04:08:00 | NPP-375D | FELIZ DESERTO | ALAGOAS | Brasil | 2702702 | 27 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 1e8a7c99-9adf-39ff-b54c-0c1918d7709c | -10.61218 | -44.33601 | 2025-01-04 04:08:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 49.7 |
| d52979a5-fcb5-3be2-9405-22ff4902552e | -8.83676 | -49.90298 | 2025-01-04 04:08:00 | NPP-375D | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 5a63c15e-5741-364a-928b-b192e27bd4a4 | -10.61339 | -44.32858 | 2025-01-04 04:08:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 8ebcfa79-ae33-36b1-8577-e0a1381952cb | -10.00133 | -48.49798 | 2025-01-04 04:08:00 | NPP-375D | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 07483393-2f2d-3e5b-be26-43a8ad7ca1bc | -8.84245 | -49.90852 | 2025-01-04 04:08:00 | NPP-375D | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| baee0143-dc83-39cb-b0d1-3c2902a69002 | -8.8406 | -49.90917 | 2025-01-04 04:08:00 | NPP-375D | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 29487307-b789-3cf7-afbf-1e8352d5e805 | -7.59557 | -39.05101 | 2025-01-04 04:08:00 | NPP-375D | PORTEIRAS | CEARÁ | Brasil | 2311108 | 23 | 33 | nan | nan | nan | Caatinga | 1.7 |
| ee86bec7-a985-3cdf-87c1-382224e35b7d | -8.43455 | -40.66455 | 2025-01-04 04:08:00 | NPP-375D | DORMENTES | PERNAMBUCO | Brasil | 2605152 | 26 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 8a99450a-5477-3d30-9573-850c11f68182 | -9.84681 | -37.12447 | 2025-01-04 04:08:00 | NPP-375D | BELO MONTE | ALAGOAS | Brasil | 2700904 | 27 | 33 | nan | nan | nan | Caatinga | 3.0 |
| 31c4f57b-4e16-3306-8fc3-4e3c094ca27c | -3.89597 | -41.03118 | 2025-01-04 04:08:00 | NPP-375D | UBAJARA | CEARÁ | Brasil | 2313609 | 23 | 33 | nan | nan | nan | Caatinga | 0.5 |
| 56f4b11c-1f39-364a-8455-cc2399ad6cdd | -5.71427 | -41.4091 | 2025-01-04 04:08:00 | NPP-375D | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 4.4 |
| 6af44ce2-5ee7-39ca-a50d-a577375f16dd | -5.98793 | -45.39198 | 2025-01-04 04:08:00 | NPP-375D | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 6d95e48f-64c1-3073-ab8b-78a645bf2bd1 | -5.59621 | -41.38346 | 2025-01-04 04:08:00 | NPP-375D | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 59aae2da-ebbe-3b2d-baf2-3a3153af9155 | -10.61499 | -44.34031 | 2025-01-04 04:08:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 2311ad4b-226a-360e-a97c-b080119e6e5c | -7.21592 | -38.63564 | 2025-01-04 04:08:00 | NPP-375D | BARRO | CEARÁ | Brasil | 2302008 | 23 | 33 | nan | nan | nan | Caatinga | 3.7 |
| d64d4c4c-02de-3bb1-bd41-e8f06a82393f | -6.97681 | -40.00861 | 2025-01-04 04:08:00 | NPP-375D | ASSARÉ | CEARÁ | Brasil | 2301604 | 23 | 33 | nan | nan | nan | Caatinga | 6.2 |
| 2e5d109c-8c11-31dc-8d86-6a9571040884 | -3.48517 | -51.18744 | 2025-01-04 04:08:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 67dd217f-2aac-3d32-b2ef-be5b48a79312 | -10.61279 | -44.33229 | 2025-01-04 04:08:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 6c7fd215-7b3c-3627-bd7a-b2ceec3fc0b4 | -6.98704 | -43.27346 | 2025-01-04 04:08:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 2c8434a8-2a8f-3c48-ac66-b2364ad676ab | -10.85095 | -44.3073 | 2025-01-04 04:08:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 0.6 |
| eeedc56b-15e6-3862-9414-a63a25633c49 | -6.66499 | -47.60452 | 2025-01-04 04:08:00 | NPP-375D | PALMEIRAS DO TOCANTINS | TOCANTINS | Brasil | 1713809 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 6dcd1cd9-3304-3083-86e4-029ad3db4429 | -7.99414 | -35.22377 | 2025-01-04 04:08:00 | NPP-375D | CHÃ DE ALEGRIA | PERNAMBUCO | Brasil | 2604403 | 26 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 0382a9de-55cf-3ca1-bc83-121a922eed21 | -6.98024 | -40.00914 | 2025-01-04 04:08:00 | NPP-375D | ASSARÉ | CEARÁ | Brasil | 2301604 | 23 | 33 | nan | nan | nan | Caatinga | 6.2 |
| f82772dd-de62-30e8-8dbf-fc7cafafed02 | -8.60053 | -39.54178 | 2025-01-04 04:08:00 | NPP-375D | OROCÓ | PERNAMBUCO | Brasil | 2609808 | 26 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 81ad3184-9e06-308a-b1e9-3dfd433cb95a | -10.21651 | -44.766 | 2025-01-04 04:08:00 | NPP-375D | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 72a57994-ecf0-37f5-af45-304985f31815 | -8.83857 | -49.90229 | 2025-01-04 04:08:00 | NPP-375D | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 413dcaea-2915-3c7b-b8e2-217eae3352bc | -6.99043 | -43.27401 | 2025-01-04 04:08:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 4289c30b-8c6e-3344-9cf1-af7653d98f7f | -7.56537 | -39.00869 | 2025-01-04 04:08:00 | NPP-375D | BREJO SANTO | CEARÁ | Brasil | 2302503 | 23 | 33 | nan | nan | nan | Caatinga | 0.9 |
| db919277-22fb-3a96-bf95-88bcfa2ff9e6 | -6.91603 | -38.20262 | 2025-01-04 04:08:00 | NPP-375D | SÃO JOSÉ DA LAGOA TAPADA | PARAÍBA | Brasil | 2514206 | 25 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 4e1ad295-773a-37a9-972e-01934b94e61c | -7.18261 | -39.65994 | 2025-01-04 04:08:00 | NPP-375D | SANTANA DO CARIRI | CEARÁ | Brasil | 2312106 | 23 | 33 | nan | nan | nan | Caatinga | 0.5 |
| 2b73ecf4-7d38-3697-9178-9d7d2e5c9f4d | -8.50856 | -40.8387 | 2025-01-04 04:08:00 | NPP-375D | DORMENTES | PERNAMBUCO | Brasil | 2605152 | 26 | 33 | nan | nan | nan | Caatinga | 0.6 |
| 05cdbd16-cbe1-3052-a17a-fdf294566edc | -10.56686 | -37.0373 | 2025-01-04 04:08:00 | NPP-375D | CAPELA | SERGIPE | Brasil | 2801306 | 28 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| e28e743e-fcff-3fd0-af10-97d21dd3d764 | -5.50313 | -44.82776 | 2025-01-04 04:08:00 | NPP-375D | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| c3d26f78-b6af-3cd1-83c5-90cf7aa199cb | -4.82244 | -37.75238 | 2025-01-04 04:08:00 | NPP-375D | JAGUARUANA | CEARÁ | Brasil | 2307007 | 23 | 33 | nan | nan | nan | Caatinga | 1.9 |
| b8912015-4422-3b9f-8888-fe1e7175a19f | -5.3337 | -41.22128 | 2025-01-04 04:08:00 | NPP-375D | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 29e911c6-d9dd-31f5-a019-b4c448cee819 | -7.18076 | -39.66042 | 2025-01-04 04:08:00 | NPP-375D | NOVA OLINDA | CEARÁ | Brasil | 2309201 | 23 | 33 | nan | nan | nan | Caatinga | 0.5 |
| 36ee47a2-307b-3780-b778-eaab58153093 | -11.2211 | -40.12872 | 2025-01-04 04:08:00 | NPP-375D | JACOBINA | BAHIA | Brasil | 2917508 | 29 | 33 | nan | nan | nan | Caatinga | 1.5 |
| cfd7f9a4-0046-3945-85d1-d554bf97f34a | -9.28309 | -43.05021 | 2025-01-04 04:08:00 | NPP-375D | ANÍSIO DE ABREU | PIAUÍ | Brasil | 2200707 | 22 | 33 | nan | nan | nan | Caatinga | 2.5 |
| 414bb6a2-5591-3d26-ac2d-1fe1c33a8266 | -5.50331 | -44.29903 | 2025-01-04 04:08:00 | NPP-375D | SÃO DOMINGOS DO MARANHÃO | MARANHÃO | Brasil | 2110708 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| bd3efc64-1215-389c-8a34-f5c1bbdeaf95 | -9.85094 | -37.12503 | 2025-01-04 04:08:00 | NPP-375D | BELO MONTE | ALAGOAS | Brasil | 2700904 | 27 | 33 | nan | nan | nan | Caatinga | 7.3 |
| 2708fbe7-6a5b-36bd-8d61-2136b14a5d4e | -9.85507 | -37.12556 | 2025-01-04 04:08:00 | NPP-375D | BELO MONTE | ALAGOAS | Brasil | 2700904 | 27 | 33 | nan | nan | nan | Caatinga | 7.3 |
| f8ef18f0-04a1-35c7-b67a-73cd2b6a8fef | -5.72129 | -39.50903 | 2025-01-04 04:08:00 | NPP-375D | MOMBAÇA | CEARÁ | Brasil | 2308500 | 23 | 33 | nan | nan | nan | Caatinga | 1.1 |
| c0789961-5db8-3f29-8c95-87b681e10c31 | -10.60755 | -44.34289 | 2025-01-04 04:08:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 25.4 |
| 2b4680d2-8f23-3a7d-a802-f730f1b162ea | -5.33424 | -41.21782 | 2025-01-04 04:08:00 | NPP-375D | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 1d10fd4c-7f1c-352e-94ee-130a829e0588 | -10.53822 | -44.67962 | 2025-01-04 04:08:00 | NPP-375D | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 2.8 |
| b876ac8f-4dcc-3f17-b3b8-920b26281846 | -6.98651 | -40.01396 | 2025-01-04 04:08:00 | NPP-375D | ASSARÉ | CEARÁ | Brasil | 2301604 | 23 | 33 | nan | nan | nan | Caatinga | 3.7 |
| d3aa8e05-1546-33d3-ae45-32f74f75d8d6 | -6.97967 | -40.01285 | 2025-01-04 04:08:00 | NPP-375D | ASSARÉ | CEARÁ | Brasil | 2301604 | 23 | 33 | nan | nan | nan | Caatinga | 6.2 |
| 12793255-2656-36d2-abc7-02fb6247a556 | -4.1647 | -42.02714 | 2025-01-04 04:08:00 | NPP-375D | BATALHA | PIAUÍ | Brasil | 2201507 | 22 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 69bcfb54-0713-313a-95a0-e0f2f92f714d | -5.09292 | -40.58495 | 2025-01-04 04:08:00 | NPP-375D | CRATEÚS | CEARÁ | Brasil | 2304103 | 23 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 7915d8bd-c38a-3804-b31e-e47fe4743ac5 | -5.41465 | -46.86448 | 2025-01-04 04:08:00 | NPP-375D | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 58a599fd-41a4-3e21-9029-ff4a259f6d8a | -7.21955 | -38.63622 | 2025-01-04 04:08:00 | NPP-375D | BARRO | CEARÁ | Brasil | 2302008 | 23 | 33 | nan | nan | nan | Caatinga | 3.7 |
| 98cd9edd-cc0d-3d4b-8af6-f6216c19c4dc | -5.50268 | -44.8261 | 2025-01-04 04:08:00 | NPP-375D | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 7a23e22a-4b6a-33eb-8f91-4b616b22da09 | -8.27342 | -41.08113 | 2025-01-04 04:08:00 | NPP-375D | ACAUÃ | PIAUÍ | Brasil | 2200053 | 22 | 33 | nan | nan | nan | Caatinga | 7.3 |
| 9972a915-9efc-3bdb-ba1b-a45bfed6a0cc | -7.592 | -39.05045 | 2025-01-04 04:08:00 | NPP-375D | PORTEIRAS | CEARÁ | Brasil | 2311108 | 23 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 3dee89ea-90de-3dd4-be6b-653faadb702e | -7.99808 | -35.22893 | 2025-01-04 04:08:00 | NPP-375D | CHÃ DE ALEGRIA | PERNAMBUCO | Brasil | 2604403 | 26 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 26a2259f-920c-3418-ac43-b33f4d4645ea | -4.82178 | -37.75674 | 2025-01-04 04:08:00 | NPP-375D | JAGUARUANA | CEARÁ | Brasil | 2307007 | 23 | 33 | nan | nan | nan | Caatinga | 1.9 |
| e0f10b83-edc6-3b66-98cf-c10f31c8b688 | -8.51194 | -40.83923 | 2025-01-04 04:08:00 | NPP-375D | DORMENTES | PERNAMBUCO | Brasil | 2605152 | 26 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 42108fb1-b885-358e-8f41-145b7b070f0d | -10.60816 | -44.33916 | 2025-01-04 04:08:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 49.7 |
| a5e05433-336d-3ff5-a029-ed5de9420a51 | -11.23581 | -39.40973 | 2025-01-04 04:08:00 | NPP-375D | SANTALUZ | BAHIA | Brasil | 2928000 | 29 | 33 | nan | nan | nan | Caatinga | 0.6 |
| d4400068-beff-3f03-9fc8-905a277de0b2 | -6.94995 | -38.10342 | 2025-01-04 04:08:00 | NPP-375D | SÃO JOSÉ DA LAGOA TAPADA | PARAÍBA | Brasil | 2514206 | 25 | 33 | nan | nan | nan | Caatinga | 2.0 |
| f5df3410-f197-39ba-91e3-d1d290c658cf | -9.98432 | -36.38602 | 2025-01-04 04:08:00 | NPP-375D | TEOTÔNIO VILELA | ALAGOAS | Brasil | 2709152 | 27 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| 004054d4-2cc4-3341-9c69-7deda1babbcc | -11.20549 | -41.83326 | 2025-01-04 04:08:00 | NPP-375D | SÃO GABRIEL | BAHIA | Brasil | 2929255 | 29 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 92bd9e6e-e0f2-359f-8761-5614d877e30a | -10.61559 | -44.33658 | 2025-01-04 04:08:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 60556f01-4605-3283-b4c1-35496aa73128 | -9.19488 | -43.15956 | 2025-01-04 04:08:00 | NPP-375D | JUREMA | PIAUÍ | Brasil | 2205532 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| f4f54aba-36e9-3ac5-ada9-3260c2a5e3fd | -3.48449 | -51.19137 | 2025-01-04 04:08:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 0148d2ff-1dcd-314f-966e-919a40d96e5f | -8.22799 | -42.87737 | 2025-01-04 04:08:00 | NPP-375D | BREJO DO PIAUÍ | PIAUÍ | Brasil | 2201988 | 22 | 33 | nan | nan | nan | Caatinga | 0.5 |
| 6c4144c5-090c-3614-822a-f0cfad7626c4 | -9.8629 | -37.09978 | 2025-01-04 04:08:00 | NPP-375D | TRAIPU | ALAGOAS | Brasil | 2709202 | 27 | 33 | nan | nan | nan | Caatinga | 1.0 |
| c19b5c38-f1bd-3619-ad39-69ef884cbebe | -10.61097 | -44.34346 | 2025-01-04 04:08:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 25.4 |
| 9fc3b4c9-1e9e-33d2-a8cf-73178bf556b3 | -6.98309 | -40.0134 | 2025-01-04 04:08:00 | NPP-375D | ASSARÉ | CEARÁ | Brasil | 2301604 | 23 | 33 | nan | nan | nan | Caatinga | 3.7 |
| 65d784ab-9cb4-3e05-9552-80bf4e44e87e | -9.31684 | -43.16096 | 2025-01-04 04:08:00 | NPP-375D | JUREMA | PIAUÍ | Brasil | 2205532 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| fe06b33e-cf4a-397e-83c7-e77f5ca10c6b | -9.32076 | -43.15796 | 2025-01-04 04:08:00 | NPP-375D | JUREMA | PIAUÍ | Brasil | 2205532 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| d138ed06-c9cd-3f9d-af5a-da2d37b5ab2e | -10.54167 | -44.68021 | 2025-01-04 04:08:00 | NPP-375D | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 4731587c-8732-3b01-8253-46eaf86f36ba | -8.83376 | -49.90141 | 2025-01-04 04:08:00 | NPP-375D | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| dcdb710c-63b0-324d-9c4f-67c6122c1a28 | -8.83773 | -49.89772 | 2025-01-04 04:08:00 | NPP-375D | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 835bf5bd-004a-3289-9cc2-1a7b3f61afab | -6.76454 | -38.99049 | 2025-01-04 04:08:00 | NPP-375D | LAVRAS DA MANGABEIRA | CEARÁ | Brasil | 2307502 | 23 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 0c8252d3-6082-3356-bfcc-8933e99e5ae6 | -10.60536 | -44.33487 | 2025-01-04 04:08:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 0.6 |


[Clique aqui para ver as próximas entradas](README6.md)
