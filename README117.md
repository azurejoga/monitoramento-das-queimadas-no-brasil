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

## Dados Diários - Página 117

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 21fc95cc-fb2b-3c4d-a8e8-5f43316dde0f | -16.96919 | -56.13953 | 2024-10-06 05:14:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.9 |
| d2c886f3-40fd-3165-9ad7-23ef22694096 | -16.96858 | -56.14405 | 2024-10-06 05:14:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.9 |
| cb4ddd34-28b3-36cc-bbd5-d86b03973169 | -16.96619 | -56.14084 | 2024-10-06 05:14:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 2.0 |
| faba3831-8f40-3338-a55a-2c868e8757cd | -16.96556 | -56.14536 | 2024-10-06 05:14:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 2.0 |
| e95af1eb-2a85-31eb-9c17-c48a2241dbf6 | -16.93631 | -55.83597 | 2024-10-06 05:14:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 2.7 |
| cc79a51c-1b1f-3845-b063-3463f93778ec | -16.93568 | -55.84066 | 2024-10-06 05:14:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 2.7 |
| baabca85-efd4-3b80-ad3f-3c8cdd988337 | -16.93504 | -55.84533 | 2024-10-06 05:14:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 4.1 |
| cb0df443-5924-34d6-b0be-92b34b967d37 | -16.9332 | -55.83072 | 2024-10-06 05:14:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 2.4 |
| 82c171aa-3a30-3945-a88a-6faa396ae594 | -16.93257 | -55.83541 | 2024-10-06 05:14:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 2.7 |
| 23f422ad-e7f9-39c0-bac7-68ba4934c389 | -16.93193 | -55.8401 | 2024-10-06 05:14:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 2.7 |
| 3bab9ed7-225d-3459-8f27-517077525a60 | -16.93072 | -55.82077 | 2024-10-06 05:14:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 2.7 |
| e5d1d16e-9246-3496-8cd1-ea6400342410 | -16.93009 | -55.82547 | 2024-10-06 05:14:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 5.0 |
| 5265d388-adb1-397f-83a0-a82d57626a89 | -16.92945 | -55.83017 | 2024-10-06 05:14:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 5.0 |
| dbce3dc0-fda3-3aa6-98cb-f805ceccf10f | -16.92882 | -55.83486 | 2024-10-06 05:14:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.9 |
| a3804f60-b147-3f61-b7bd-8805f7ae5899 | -16.92698 | -55.82021 | 2024-10-06 05:14:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 2.7 |
| e6765c37-23e8-3c83-888c-ec571fdd3274 | -16.92634 | -55.82491 | 2024-10-06 05:14:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 5.0 |
| 0b940375-ef0b-3718-828a-4cebb3bd6d88 | -16.92571 | -55.82961 | 2024-10-06 05:14:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 5.0 |
| 8f006fc6-a55b-3d98-b262-bae5cfcaa728 | -16.92508 | -55.83428 | 2024-10-06 05:14:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.9 |
| cd4ab922-0788-3bde-a73c-4649df177327 | -16.92445 | -55.83895 | 2024-10-06 05:14:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.9 |
| edd10e08-1a04-39e1-97e8-97b9627fe484 | -16.9226 | -55.82435 | 2024-10-06 05:14:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.4 |
| 730a3f6b-faf0-335b-954f-1c577b5067e4 | -16.92196 | -55.82904 | 2024-10-06 05:14:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.4 |
| ef0ad1be-312c-3a01-a16e-19f5a938b66c | -16.91885 | -55.82378 | 2024-10-06 05:14:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.4 |
| cb82013e-e493-3dfd-b1a5-acbe2c89cd1b | -16.91822 | -55.82847 | 2024-10-06 05:14:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.4 |
| c29725e1-e82b-382a-9919-191795c1f8aa | -17.15095 | -56.4761 | 2024-10-06 05:14:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 2.4 |
| 078f4bb5-7ddb-3f31-bbd2-ca2c4279a517 | -17.14732 | -56.47554 | 2024-10-06 05:14:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 2.4 |
| ecbef71e-f887-3e0e-b545-dfa20131298b | -17.0885 | -56.67633 | 2024-10-06 05:14:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 12.5 |
| ab65aed6-7e85-3005-8cbb-8e9fdbb97673 | -17.06576 | -56.68158 | 2024-10-06 05:14:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 5.2 |
| ab8c8d35-2c3f-3d04-a895-9957e40c3833 | -17.06217 | -56.68103 | 2024-10-06 05:14:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 5.2 |
| f75ec26b-5b32-3ded-9639-43a01a151332 | -17.02868 | -56.68461 | 2024-10-06 05:14:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 12.2 |
| 36744640-0b64-3ae3-992e-4cc20705fa9f | -17.02092 | -56.68777 | 2024-10-06 05:14:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 5.9 |
| e25ad85f-d832-3a52-a404-015e138ed9cc | -17.01256 | -56.69522 | 2024-10-06 05:14:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 6.6 |
| 8b4e9021-a52a-3301-90c7-859114209440 | -17.01016 | -56.68612 | 2024-10-06 05:14:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 10.8 |
| da29ec2d-3d38-3235-8bfa-674ed65429c2 | -16.95939 | -56.61476 | 2024-10-06 05:14:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 6.8 |
| 47a003a7-1cb4-3bdc-b3fe-5203a943925c | -16.87462 | -55.85829 | 2024-10-06 05:14:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 5.8 |
| 8c09d84d-e3c0-3949-8ad3-cc65d686e010 | -16.87153 | -55.85307 | 2024-10-06 05:14:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 4.1 |
| 8fe9e29c-9c5b-3325-9a1d-0051ebca2582 | -16.86779 | -55.85252 | 2024-10-06 05:14:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 4.1 |
| 04caa6a6-9987-386b-a676-3bc63d66da8b | -16.85211 | -55.88337 | 2024-10-06 05:14:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 3.5 |
| ca5839b1-6ec6-3f5f-9e84-8a88a6fd6b06 | -16.8272 | -55.89858 | 2024-10-06 05:14:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.7 |
| bc540605-f8f1-3928-b356-4b6afcabcb23 | -16.82347 | -55.89802 | 2024-10-06 05:14:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.7 |
| 94c1e1e0-eeb8-3f66-8426-5739e7efac4e | -16.82285 | -55.90264 | 2024-10-06 05:14:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.7 |
| ecefd4ce-dc85-3769-9ec7-3a5c378ff9fb | -16.81602 | -55.89688 | 2024-10-06 05:14:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 5.2 |
| 75189726-7130-331c-89f0-3452866ebab3 | -16.69796 | -55.91464 | 2024-10-06 05:14:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 3.6 |
| c199cde9-6673-3442-9e7b-9905d7bef576 | -16.69733 | -55.91925 | 2024-10-06 05:14:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 3.8 |
| c06a1d67-8985-37ef-9575-43d6e74ac724 | -16.6973 | -55.94737 | 2024-10-06 05:14:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 2.2 |
| 813da8f5-f7c6-3a4f-a83e-281bf8923cd4 | -16.69671 | -55.92386 | 2024-10-06 05:14:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 3.8 |
| 6a0dd64e-d9bf-3f33-9561-05c70c61a9e8 | -16.69424 | -55.91407 | 2024-10-06 05:14:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 4.9 |
| 0969e507-1a2e-345e-9e47-0a66e7af6338 | -16.69359 | -55.94682 | 2024-10-06 05:14:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 2.2 |
| 19028f54-f72e-3980-8fcd-cbe811580066 | -16.69302 | -55.89507 | 2024-10-06 05:14:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 4.0 |
| 3c585091-49f7-3b3d-9185-11ea9964b272 | -16.69179 | -55.87602 | 2024-10-06 05:14:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 4.1 |
| ea6dc2af-4a46-3975-8586-5c3f63385fb9 | -16.69115 | -55.90891 | 2024-10-06 05:14:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 4.9 |
| fa22af2b-b276-3d53-8e1c-945dcf1f4382 | -16.69053 | -55.91351 | 2024-10-06 05:14:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 4.9 |
| be21d11b-86cd-3cb1-8449-e01fe98d6499 | -16.6893 | -55.89451 | 2024-10-06 05:14:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 4.1 |
| 5ec4a411-4514-38a9-8ae3-7b75336096c8 | -16.68868 | -55.89913 | 2024-10-06 05:14:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 5.4 |
| 3bfe2e08-12ca-3ae8-ae43-02e100fc4709 | -16.68805 | -55.90375 | 2024-10-06 05:14:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 5.4 |
| 4cd87da9-a89f-3cfc-9afb-ca018731bf60 | -16.68743 | -55.90835 | 2024-10-06 05:14:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 5.7 |
| ce080a23-f1de-3335-b9af-c1fe85e9e99b | -16.68664 | -55.87263 | 2024-10-06 05:14:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 3.3 |
| 9bc47606-ca2c-3d43-ac50-efc8308ac35a | -16.68646 | -55.90087 | 2024-10-06 05:14:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 4.3 |
| 81f0fece-924e-3134-bdd0-317389f778db | -16.68617 | -55.94571 | 2024-10-06 05:14:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 4.2 |
| af854697-b624-3151-918b-eb63fbae022b | -16.68581 | -55.90547 | 2024-10-06 05:14:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 4.3 |
| dcee9337-9d80-37f6-b97c-b6ec2bf23d90 | -16.68497 | -55.87026 | 2024-10-06 05:14:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 3.6 |
| 531cf777-49ed-3449-a2fd-07934753405f | -16.68433 | -55.90318 | 2024-10-06 05:14:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 5.4 |
| 3fe54124-7033-3676-97ea-f570f65f36eb | -16.68357 | -55.86744 | 2024-10-06 05:14:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 2.8 |
| 78fe844f-e591-3118-a9bf-cdb35ed4e1f5 | -16.68292 | -55.87207 | 2024-10-06 05:14:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 2.6 |
| fb9699db-acf5-37da-87da-e7ed876f3fd7 | -16.68274 | -55.9003 | 2024-10-06 05:14:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 4.3 |
| 202a3f15-f4f1-37ab-9383-b92ad30a7056 | -16.68227 | -55.87669 | 2024-10-06 05:14:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 2.6 |
| aac670e3-7e1f-3800-a2f0-6e0692e29b07 | -16.68209 | -55.90491 | 2024-10-06 05:14:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 4.3 |
| 722123c4-2464-358c-9008-18ceec9159d9 | -16.68186 | -55.89338 | 2024-10-06 05:14:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 4.1 |
| d5885931-b197-3711-b6cf-eda5007f812d | -16.68124 | -55.86969 | 2024-10-06 05:14:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 3.6 |
| 29aa1605-583d-3766-82b3-2e5bee4d14ed | -16.68062 | -55.90261 | 2024-10-06 05:14:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 5.4 |
| 5b3a5934-b9d3-3e4c-a078-885924747cc5 | -16.68062 | -55.87432 | 2024-10-06 05:14:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 3.6 |
| cf39ad91-9456-38a0-a73b-ea7e3a670876 | -16.68 | -55.87896 | 2024-10-06 05:14:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 3.5 |
| 85e761ee-5ddb-36dd-9a3b-79c296c9a624 | -16.67968 | -55.89514 | 2024-10-06 05:14:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 4.2 |
| 86894246-52e0-3362-b791-46baa6beb7aa | -16.6792 | -55.87151 | 2024-10-06 05:14:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 2.6 |
| 8cd3b946-a85d-3b60-969d-e5eb941c5b4a | -16.67903 | -55.89974 | 2024-10-06 05:14:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 4.5 |
| 6305bd3a-fba6-3ae7-995c-1ee162145852 | -16.67854 | -55.87613 | 2024-10-06 05:14:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 2.6 |
| 29f344d4-f70e-351a-89b7-7cffdf3687c9 | -16.67838 | -55.90434 | 2024-10-06 05:14:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 4.5 |
| 2bfc0132-6fd0-3d19-829e-b28d3ac2b0a9 | -16.67752 | -55.89743 | 2024-10-06 05:14:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 5.4 |
| 13da0e8a-582e-35fc-b8d5-15b2b162d4b2 | -16.6769 | -55.90205 | 2024-10-06 05:14:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 5.4 |
| d342ca7b-54d6-339a-80b4-5a9cdf2f03fa | -16.67628 | -55.90665 | 2024-10-06 05:14:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 4.6 |
| 3f7557a5-bfd6-380b-a9bb-00547c429462 | -16.67531 | -55.89918 | 2024-10-06 05:14:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 4.5 |
| eeb5d026-e5ce-386f-a42c-3d67579935c1 | -16.67482 | -55.87557 | 2024-10-06 05:14:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 3.7 |
| 48b8487c-d817-3494-9e44-bbc1cc8d23b1 | -16.67466 | -55.90378 | 2024-10-06 05:14:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 4.5 |
| cb1beb81-429a-3a93-8fa4-092be99bd4c7 | -16.67418 | -55.88019 | 2024-10-06 05:14:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 3.4 |
| 30d9bc8d-dfab-3b00-8d49-b0f48920ea2d | -16.6711 | -55.875 | 2024-10-06 05:14:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 3.7 |
| 0018d979-8887-3ba0-a327-b97af2660d86 | -16.72163 | -56.42292 | 2024-10-06 05:14:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.3 |
| 72b7db0c-4953-32db-be2b-8d6e84e149fc | -17.09148 | -56.68117 | 2024-10-06 05:14:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 12.5 |
| c8c937e9-3e77-39ef-89c1-bee26a80a61b | -17.09087 | -56.68545 | 2024-10-06 05:14:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 43.8 |
| c717ae6d-7fee-3ab7-9fe9-ef1b8430a3d5 | -17.08789 | -56.68061 | 2024-10-06 05:14:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 12.5 |
| 109e80c4-dea0-3166-97a7-6da6ebc6cb12 | -17.01973 | -56.69632 | 2024-10-06 05:14:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.4 |
| 318dc672-344f-3b93-ba51-1406232760a7 | -17.01793 | -56.68295 | 2024-10-06 05:14:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 5.9 |
| 46163d93-1d6d-37b9-8c5d-cbe858004d73 | -17.01315 | -56.69094 | 2024-10-06 05:14:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 6.6 |
| 9a286e21-d8ab-31b3-b3d2-5a2a1e345ab2 | -17.00898 | -56.69466 | 2024-10-06 05:14:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 6.6 |
| ae28e5ec-0c02-393b-9cba-727a25136b99 | -16.95519 | -56.6185 | 2024-10-06 05:14:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 6.8 |
| 5a92eb31-a4d9-3965-8df5-0df808f63f98 | -16.95459 | -56.62279 | 2024-10-06 05:14:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.5 |
| ba96b843-733c-3009-9958-f8b6f8ba0013 | -16.95039 | -56.62653 | 2024-10-06 05:14:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.4 |
| ab5a6d9b-8689-3cf4-b3bb-064417c19251 | -16.9468 | -56.62598 | 2024-10-06 05:14:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 2.4 |
| 24c8da56-3e1c-38a6-bb57-2280efaa0441 | -16.94441 | -56.61684 | 2024-10-06 05:14:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 3.6 |
| 94191c79-f46d-341a-9ae2-94faa8765cc1 | -16.94021 | -56.62058 | 2024-10-06 05:14:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 2.8 |
| 878eeea6-4f3c-3635-bc69-a2ba3054a337 | -16.93962 | -56.62487 | 2024-10-06 05:14:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.8 |
| 8112f764-e605-3827-94ec-74562bd53edb | -16.65544 | -55.9056 | 2024-10-06 05:14:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.6 |


[Clique aqui para ver as próximas entradas](README118.md)
