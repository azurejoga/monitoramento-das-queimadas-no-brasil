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

## Dados Diários - Página 20

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 73db2bca-794e-3755-988c-7121ca75cb10 | -12.46763 | -54.32364 | 2025-11-02 04:50:00 | NPP-375D | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| aad94927-a776-30c7-91da-ab3bc3d3b030 | -7.04651 | -55.43678 | 2025-11-02 04:50:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| b1af58fd-a664-33e0-86b1-0d025ffd5e67 | -13.3189 | -43.46331 | 2025-11-02 04:50:00 | NPP-375D | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 3.6 |
| bbfd516c-a92c-3aee-be77-4eaeda2b9808 | -6.37198 | -52.69843 | 2025-11-02 04:50:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 29f4899c-14c5-3149-a2e0-428790bcf64e | -10.73968 | -46.22932 | 2025-11-02 04:50:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 60ca85dd-0be4-3c83-bab2-49ac49f546ad | -9.06584 | -48.83159 | 2025-11-02 04:50:00 | NPP-375D | GOIANORTE | TOCANTINS | Brasil | 1708304 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 0ea6087b-b7c5-3b00-9c1e-5fe073a3b63d | -13.9807 | -51.5048 | 2025-11-02 04:50:00 | NPP-375D | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 460dd6fc-a0b7-3642-8f6d-1e47735970b0 | -9.06227 | -48.83104 | 2025-11-02 04:50:00 | NPP-375D | GOIANORTE | TOCANTINS | Brasil | 1708304 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 8b639f6e-7299-38d0-a867-01ced342deb0 | -10.73323 | -46.24467 | 2025-11-02 04:50:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 82b9b867-f119-39ba-854e-f10d41282067 | -14.61164 | -46.65309 | 2025-11-02 04:50:00 | NPP-375D | ALVORADA DO NORTE | GOIÁS | Brasil | 5200803 | 52 | 33 | nan | nan | nan | Cerrado | 0.5 |
| fd2508b1-1698-365e-9eae-f58d7ac3831f | -6.31934 | -52.61177 | 2025-11-02 04:50:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 0cef63d1-95d9-312f-b22d-e1402071c3be | -14.15001 | -44.27155 | 2025-11-02 04:50:00 | NPP-375D | FEIRA DA MATA | BAHIA | Brasil | 2910776 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| dc23a123-f090-3dd7-8132-3e9de1d39ae6 | -6.31993 | -52.60814 | 2025-11-02 04:50:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 9d03c7c9-2bdd-3ac8-98b8-a02b7a32c256 | -11.73193 | -59.3056 | 2025-11-02 04:50:00 | NPP-375D | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 64b5c694-5f1e-39e2-bd21-a3955aca6d49 | -7.6946 | -43.10447 | 2025-11-02 04:50:00 | NPP-375D | RIO GRANDE DO PIAUÍ | PIAUÍ | Brasil | 2209005 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 59379986-7e7d-37ef-a795-cb1afa1e4c2d | -7.23067 | -46.03631 | 2025-11-02 04:50:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 4c61528b-ccf9-37d3-a704-3df9108ebf58 | -11.20191 | -53.83482 | 2025-11-02 04:50:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 3d412ec5-56fc-3cfa-81aa-dd2cd8dd1c2e | -10.74189 | -46.21332 | 2025-11-02 04:50:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 7.9 |
| 153e134e-6aa6-3013-871c-8684530d74ee | -10.99546 | -54.00802 | 2025-11-02 04:50:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 27fbe534-5866-3378-a9f1-67b85943d912 | -10.73952 | -46.26182 | 2025-11-02 04:50:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 2685fa04-4cdd-3f1e-a2bd-327bd88c1174 | -8.59922 | -54.65625 | 2025-11-02 04:50:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| bbdfc527-313e-3926-951e-f31ca629a2aa | -10.61535 | -52.18451 | 2025-11-02 04:50:00 | NPP-375D | PORTO ALEGRE DO NORTE | MATO GROSSO | Brasil | 5106778 | 51 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 96db8a84-c6d3-383e-a57f-103b34a8c98a | -13.77281 | -48.8665 | 2025-11-02 04:50:00 | NPP-375D | FORMOSO | GOIÁS | Brasil | 5208103 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 81edb7ba-7fc3-3d82-8336-5a2911fd5584 | -10.72897 | -46.24406 | 2025-11-02 04:50:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| a34b682f-85cd-3a8e-8adc-9591ff4fcf48 | -10.73172 | -46.22413 | 2025-11-02 04:50:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 5be5357e-3252-3aa5-ae36-0bb956ab57cb | -14.59737 | -46.65987 | 2025-11-02 04:50:00 | NPP-375D | ALVORADA DO NORTE | GOIÁS | Brasil | 5200803 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 98e0155a-5e21-3d15-a743-eeac4821e69e | -14.01873 | -43.48232 | 2025-11-02 04:50:00 | NPP-375D | MALHADA | BAHIA | Brasil | 2920205 | 29 | 33 | nan | nan | nan | Cerrado | 11.5 |
| 77f63b3b-4eaa-34b7-b24b-d93cec88e64e | -14.66159 | -46.61514 | 2025-11-02 04:50:00 | NPP-375D | ALVORADA DO NORTE | GOIÁS | Brasil | 5200803 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| f985f292-9219-3291-b5d7-705dd518e49f | -12.24315 | -54.39191 | 2025-11-02 04:50:00 | NPP-375D | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 6b4b39a5-b951-39d5-8d74-aaec1a24b2df | -12.15681 | -56.77027 | 2025-11-02 04:50:00 | NPP-375D | ITANHANGÁ | MATO GROSSO | Brasil | 5104542 | 51 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 7a5b1b58-86b0-3ab7-a3f4-91f791efec17 | -10.62199 | -52.18559 | 2025-11-02 04:50:00 | NPP-375D | PORTO ALEGRE DO NORTE | MATO GROSSO | Brasil | 5106778 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| eec41398-9f37-3dfe-b77f-110f5347988b | -14.29947 | -43.83561 | 2025-11-02 04:50:00 | NPP-375D | CARINHANHA | BAHIA | Brasil | 2907103 | 29 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 4cf62052-9846-303b-87dc-3aa44cddb32e | -10.78387 | -56.8175 | 2025-11-02 04:50:00 | NPP-375D | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 4.9 |
| d43f3c45-2e40-3559-8e4b-66a035d91ce1 | -8.60643 | -54.65744 | 2025-11-02 04:50:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 2f58646e-c3b2-3302-82ff-61010c9bd5fe | -10.99265 | -54.00366 | 2025-11-02 04:50:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| a76a2e96-f95e-31b5-9de4-0c018a87046a | -10.73583 | -46.25723 | 2025-11-02 04:50:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 915ec742-356d-3b49-a944-ebf0ee5d199c | -13.72339 | -51.45681 | 2025-11-02 04:50:00 | NPP-375D | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| a99b1f94-56fc-3896-a9ad-80b925690c65 | -10.78199 | -56.81574 | 2025-11-02 04:50:00 | NPP-375D | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| b9411d3a-202a-396b-90e2-ded3c001868d | -10.99669 | -54.00047 | 2025-11-02 04:50:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| e7682494-d065-399d-877f-bd7940ed4a0f | -8.85915 | -49.88001 | 2025-11-02 04:50:00 | NPP-375D | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| ad77712f-b2e3-32c0-8dee-90b96dd482c7 | -11.36508 | -54.30994 | 2025-11-02 04:50:00 | NPP-375D | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 636c1c40-d7a6-325b-ba0b-173e7b17e27b | -8.82555 | -50.05203 | 2025-11-02 04:50:00 | NPP-375D | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 1425cd1a-414a-3c87-a82b-8a44fbeed4f4 | -11.57123 | -47.08285 | 2025-11-02 04:50:00 | NPP-375D | PORTO ALEGRE DO TOCANTINS | TOCANTINS | Brasil | 1718006 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| d6d5d29f-5a0d-3630-9c3f-f592024627f8 | -12.51618 | -45.73248 | 2025-11-02 04:50:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| b9fb7cd9-ed9c-377c-8890-0e89d42b0eb8 | -8.60575 | -54.66158 | 2025-11-02 04:50:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| ca9541f6-75a7-3b32-bf9e-ce390df8f454 | -12.86724 | -50.87016 | 2025-11-02 04:50:00 | NPP-375D | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 2.5 |
| f942c1a3-0b46-3780-b0a9-08438ac8018b | -8.15651 | -44.48819 | 2025-11-02 04:50:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 3d59530e-fa57-3ed4-92ad-ba84ac433231 | -12.8521 | -43.76707 | 2025-11-02 04:50:00 | NPP-375D | SERRA DOURADA | BAHIA | Brasil | 2930303 | 29 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 7a62767e-dbd3-352c-968e-4263da3fcf93 | -14.61106 | -46.6574 | 2025-11-02 04:50:00 | NPP-375D | ALVORADA DO NORTE | GOIÁS | Brasil | 5200803 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 6c386f3d-9862-3ff9-a4d3-3d5a2c667d84 | -14.6583 | -46.60611 | 2025-11-02 04:50:00 | NPP-375D | ALVORADA DO NORTE | GOIÁS | Brasil | 5200803 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 58082458-9d04-3c30-83ec-7fa20e877f6a | -9.14062 | -51.30243 | 2025-11-02 04:50:00 | NPP-375D | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 66553992-bff2-3738-bd52-52de6df5d243 | -10.30294 | -53.77614 | 2025-11-02 04:50:00 | NPP-375D | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 3.5 |
| b9263ba0-f51b-351f-8cc0-647cc9b8d967 | -13.83672 | -49.52323 | 2025-11-02 04:50:00 | NPP-375D | AMARALINA | GOIÁS | Brasil | 5200829 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| dac7ce47-74ca-3fbc-8321-ac1b8fc938f4 | -12.24378 | -54.38809 | 2025-11-02 04:50:00 | NPP-375D | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| f3c0ef74-844d-3f93-987e-8d510396dcd5 | -14.20189 | -47.8039 | 2025-11-02 04:50:00 | NPP-375D | ALTO PARAÍSO DE GOIÁS | GOIÁS | Brasil | 5200605 | 52 | 33 | nan | nan | nan | Cerrado | 3.2 |
| b22e0b40-0885-3ff1-ab86-0575b7da1d9c | -10.63803 | -51.75997 | 2025-11-02 04:50:00 | NPP-375D | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 722a99f9-d970-389c-92f7-6d9d98370618 | -10.73158 | -46.25661 | 2025-11-02 04:50:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| c8b2cc28-5e76-30cb-8621-876a83a0965f | -14.02369 | -43.48643 | 2025-11-02 04:50:00 | NPP-375D | MALHADA | BAHIA | Brasil | 2920205 | 29 | 33 | nan | nan | nan | Cerrado | 18.2 |
| 26bf0cf2-4079-3e54-938e-f1e38f1de9d4 | -12.87123 | -50.8899 | 2025-11-02 04:50:00 | NPP-375D | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 22.6 |
| 0f5b474c-c357-3065-b555-abc50efa0b09 | -9.15392 | -51.30455 | 2025-11-02 04:50:00 | NPP-375D | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| a3794c02-fd9d-3dab-8895-101f0f79d6f9 | -11.73186 | -59.30804 | 2025-11-02 04:50:00 | NPP-375D | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 3f9382d1-45b3-3bec-9a27-943ebc6ff990 | -13.68954 | -49.48528 | 2025-11-02 04:50:00 | NPP-375D | MUTUNÓPOLIS | GOIÁS | Brasil | 5214101 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| aa68e766-d33d-328c-8a56-6b76118759e8 | -7.2365 | -44.94112 | 2025-11-02 04:50:00 | NPP-375D | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| aececddb-fb93-3d30-b51d-1f0f11d121d8 | -10.62144 | -52.1891 | 2025-11-02 04:50:00 | NPP-375D | PORTO ALEGRE DO NORTE | MATO GROSSO | Brasil | 5106778 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 4e992794-31e4-32e9-b220-c5af76c8ce95 | -9.31421 | -41.07056 | 2025-11-02 04:50:00 | NPP-375D | CASA NOVA | BAHIA | Brasil | 2907202 | 29 | 33 | nan | nan | nan | Caatinga | 1.8 |
| e93266ee-8c15-36f6-8270-8ef0bb21143c | -13.76889 | -48.86771 | 2025-11-02 04:50:00 | NPP-375D | FORMOSO | GOIÁS | Brasil | 5208103 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| c412c803-c455-30a2-806e-ed376a40a6e5 | -10.73598 | -46.22472 | 2025-11-02 04:50:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| ca1868f2-e232-3a05-90ac-7919dbcbdb46 | -10.50682 | -51.88293 | 2025-11-02 04:50:00 | NPP-375D | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 7b2f28af-5038-3ff9-a8db-6f761971fdc1 | -13.97958 | -51.51215 | 2025-11-02 04:50:00 | NPP-375D | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 9e31f703-e3b0-3ce9-ab8e-5b424975d273 | -11.28951 | -53.95967 | 2025-11-02 04:50:00 | NPP-375D | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| bffc02c6-a0a2-34b1-9b6c-58ed09d75d07 | -14.61184 | -46.65518 | 2025-11-02 04:50:00 | NPP-375D | ALVORADA DO NORTE | GOIÁS | Brasil | 5200803 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 336c3f2e-3a91-38d7-a103-34824613c702 | -12.86839 | -50.88563 | 2025-11-02 04:50:00 | NPP-375D | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 4.3 |
| beba63d4-a6d4-3321-8bc9-119aad786b3e | -12.88451 | -54.75805 | 2025-11-02 04:50:00 | NPP-375D | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 9ada6776-7acb-3e86-b344-db53afd2086f | -7.55382 | -56.15657 | 2025-11-02 04:50:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 144ec42c-655d-3069-a25d-13dbfa99612d | -13.01829 | -44.106 | 2025-11-02 04:50:00 | NPP-375D | SANTANA | BAHIA | Brasil | 2928208 | 29 | 33 | nan | nan | nan | Cerrado | 0.3 |
| 4e10ff07-2c03-312b-a57b-f12340cc08a9 | -11.73101 | -59.31277 | 2025-11-02 04:50:00 | NPP-375D | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| d7024a0a-d4eb-37e4-913b-c21e067be577 | -13.58946 | -51.03019 | 2025-11-02 04:50:00 | NPP-375D | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 7f7f5fc2-44cb-335a-9508-e39d61236ae0 | -10.73913 | -46.23332 | 2025-11-02 04:50:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| b7327139-0de9-31b4-b8fa-0bbe286e3580 | -11.27817 | -45.49076 | 2025-11-02 04:50:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.6 |
| cf04f49e-6b55-33da-9285-c9c7d07a3db8 | -10.99607 | -54.00424 | 2025-11-02 04:50:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 0f44596e-d94d-3b90-b6d1-80876da29972 | -12.42233 | -54.49155 | 2025-11-02 04:50:00 | NPP-375D | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 2146382b-2bb1-3a6c-b1b9-8f97624facd6 | -12.86895 | -50.88189 | 2025-11-02 04:50:00 | NPP-375D | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 9c8849e0-b9ba-3910-bed0-88908fb3d667 | -10.74008 | -46.25784 | 2025-11-02 04:50:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 481edeef-1831-33bb-aaca-5c6e49682890 | -9.78515 | -43.6133 | 2025-11-02 04:50:00 | NPP-375D | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 0773b981-c225-35e3-8623-79cd183a3ebd | -10.6159 | -52.18101 | 2025-11-02 04:50:00 | NPP-375D | PORTO ALEGRE DO NORTE | MATO GROSSO | Brasil | 5106778 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| eec9b41f-5a18-3074-a909-44c4abceae38 | -11.36854 | -54.31053 | 2025-11-02 04:50:00 | NPP-375D | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| c75196db-1dbf-3408-bf45-3a08b0f2f09a | -10.97356 | -54.25006 | 2025-11-02 04:50:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 4.4 |
| d1bf3573-3430-317d-a2f2-082852e97865 | -14.66213 | -46.61099 | 2025-11-02 04:50:00 | NPP-375D | ALVORADA DO NORTE | GOIÁS | Brasil | 5200803 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 3e0c13e7-11ed-39f7-a3dc-3fd673c7301b | -10.73858 | -46.23731 | 2025-11-02 04:50:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| e530b2f0-3dca-3736-96e4-8767b2bab09a | -14.01831 | -43.48576 | 2025-11-02 04:50:00 | NPP-375D | MALHADA | BAHIA | Brasil | 2920205 | 29 | 33 | nan | nan | nan | Cerrado | 11.5 |
| 0afa943c-ad71-30e5-b3b8-1dde9900ef7b | -14.02411 | -43.48299 | 2025-11-02 04:50:00 | NPP-375D | MALHADA | BAHIA | Brasil | 2920205 | 29 | 33 | nan | nan | nan | Cerrado | 18.2 |
| e9ebb23c-b0c2-3330-a9e9-8c218a520180 | -9.60428 | -55.102 | 2025-11-02 04:50:00 | NPP-375D | NOVO MUNDO | MATO GROSSO | Brasil | 5106265 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 4a805551-bd88-3383-a07e-9b6e78de20fb | -12.86952 | -50.87816 | 2025-11-02 04:50:00 | NPP-375D | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 26c06eea-21f1-3a2b-8adf-379536ed0d15 | -12.86783 | -50.88935 | 2025-11-02 04:50:00 | NPP-375D | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 20.2 |
| 06be403a-21ce-3d58-bcc1-fd51004cd7d3 | -11.72735 | -59.30478 | 2025-11-02 04:50:00 | NPP-375D | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 7728a192-16b5-3734-8961-054fac2482d5 | -11.36446 | -54.31376 | 2025-11-02 04:50:00 | NPP-375D | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 0a393628-eca1-3dbe-ab2c-448301853541 | -13.9762 | -51.5116 | 2025-11-02 04:50:00 | NPP-375D | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 2e150e29-1029-3b4f-a366-0861579170b8 | -10.72599 | -44.06174 | 2025-11-02 04:50:00 | NPP-375D | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| e23472c6-615c-372f-8950-716e7b7003f9 | -9.06523 | -48.83565 | 2025-11-02 04:50:00 | NPP-375D | GOIANORTE | TOCANTINS | Brasil | 1708304 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 171ee7da-ed63-320e-9f6a-a1219bd6bfec | -9.44825 | -43.20091 | 2025-11-02 04:50:00 | NPP-375D | CAMPO ALEGRE DE LOURDES | BAHIA | Brasil | 2905909 | 29 | 33 | nan | nan | nan | Caatinga | 1.9 |


[Clique aqui para ver as próximas entradas](README21.md)
