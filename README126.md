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
| bf721114-b76e-3923-8fae-7f96281bc21e | -17.99745 | -57.33887 | 2024-10-14 05:12:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.7 |
| cee8a4f3-ca05-3e40-b298-674f5cb7b45b | -17.99703 | -57.34016 | 2024-10-14 05:12:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.1 |
| 4a070a8f-9d4f-3464-b597-bf321091b5c5 | -17.99687 | -57.34298 | 2024-10-14 05:12:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 12.3 |
| 52702388-8fd8-322e-8ff7-dc9a582c5ed9 | -17.99352 | -57.33961 | 2024-10-14 05:12:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.8 |
| 2b895eec-414f-383f-9103-aee21ce8e8b0 | -17.99292 | -57.34372 | 2024-10-14 05:12:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 28.6 |
| d809dafa-47e8-3779-8b90-64ba6f69c70a | -17.99 | -57.33906 | 2024-10-14 05:12:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.8 |
| def8d1d4-c9dd-3086-98a2-306a9788cf78 | -17.9894 | -57.34317 | 2024-10-14 05:12:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 28.6 |
| 5078e519-da76-331e-b363-44ee2a808bd2 | -17.98648 | -57.33852 | 2024-10-14 05:12:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.7 |
| aed6058e-a2a1-3c59-993f-0f76c4fc687d | -17.98296 | -57.33797 | 2024-10-14 05:12:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.7 |
| 288b6a91-5581-302a-b1cd-cf2910d07701 | -17.98241 | -57.31687 | 2024-10-14 05:12:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.0 |
| 3d1165ec-f40b-317c-a053-7557084cd725 | -17.98182 | -57.32098 | 2024-10-14 05:12:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.0 |
| 2a6bcbc3-414a-3d73-b622-32c1ec17216e | -17.98126 | -57.29986 | 2024-10-14 05:12:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.1 |
| 27cbab70-f308-388a-a890-8ae42510429a | -17.98122 | -57.3251 | 2024-10-14 05:12:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.7 |
| eb516135-9b08-3df5-90cf-0d02cbbe4397 | -17.98011 | -57.28281 | 2024-10-14 05:12:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 0.1 |
| 4cf1fadd-9cc9-39c5-bc0e-c48fcc078566 | -17.98008 | -57.30809 | 2024-10-14 05:12:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.5 |
| 9eb72948-f6dc-34db-a0ab-a808755f50bb | -17.98004 | -57.33332 | 2024-10-14 05:12:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.0 |
| 8c3479b6-2bad-3089-885f-89736be42d88 | -17.97952 | -57.28694 | 2024-10-14 05:12:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 0.1 |
| 3f3bf8b1-8a7f-314d-a58f-667989610a16 | -17.97948 | -57.31221 | 2024-10-14 05:12:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.5 |
| 679d2ccd-20e8-3c2a-a948-50f32cae16a8 | -17.97944 | -57.33742 | 2024-10-14 05:12:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.0 |
| 99992e41-6ca9-3216-853f-8493a78ddca6 | -17.97889 | -57.31633 | 2024-10-14 05:12:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.0 |
| 916a594c-28dc-37e2-a19c-e7c61fffbba6 | -17.97885 | -57.34153 | 2024-10-14 05:12:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 5.2 |
| efda32e9-9b4e-389d-9685-982d287290b2 | -17.9783 | -57.32044 | 2024-10-14 05:12:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.0 |
| 6ca74b96-1efc-3478-91f3-aadef3e50841 | -17.97774 | -57.29932 | 2024-10-14 05:12:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 0.9 |
| 39992412-950c-314d-a26f-41e846b35df6 | -17.97771 | -57.32455 | 2024-10-14 05:12:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.7 |
| 1ade3c60-543d-3439-ada1-a4507b290646 | -17.97711 | -57.32867 | 2024-10-14 05:12:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.7 |
| cd7bdfee-33e5-3eff-8fe4-2bd32734ebbe | -17.97652 | -57.33276 | 2024-10-14 05:12:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.0 |
| c7d467fc-5294-3ef8-8955-ecfc24fb0861 | -17.97596 | -57.31166 | 2024-10-14 05:12:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.8 |
| f9721688-b30f-3da5-a5f3-73f614162372 | -17.97593 | -57.33688 | 2024-10-14 05:12:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.0 |
| 5951d593-e0fd-3ea3-9f9d-9114b8b09f50 | -17.97537 | -57.31578 | 2024-10-14 05:12:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.8 |
| 2b2229e9-767f-3572-87c6-e727c3dd6229 | -17.97533 | -57.34099 | 2024-10-14 05:12:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 5.2 |
| fcfd9242-7a30-318f-add8-2df23d00a05d | -17.97481 | -57.29465 | 2024-10-14 05:12:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 0.7 |
| dc568d6f-1307-3566-9e87-6fb10678effe | -17.97425 | -57.27345 | 2024-10-14 05:12:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.0 |
| 9e32b326-af35-3769-86dc-46d1b715497b | -17.97422 | -57.29877 | 2024-10-14 05:12:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 0.9 |
| 8fdbd105-e9aa-3a05-a12e-2d2fd6bd4da5 | -17.97366 | -57.27758 | 2024-10-14 05:12:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.0 |
| 0c54ea32-1d68-3a1f-97c7-37ccdad61309 | -17.97359 | -57.32812 | 2024-10-14 05:12:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 0.8 |
| cfd61a06-00e7-3a89-81a0-39cebaea6f72 | -17.97306 | -57.28172 | 2024-10-14 05:12:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.1 |
| d55d2732-645f-396c-801a-edfbfb2a8677 | -17.973 | -57.33223 | 2024-10-14 05:12:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.8 |
| 069feade-5617-36a6-9e9f-26b802822125 | -17.97247 | -57.28585 | 2024-10-14 05:12:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.1 |
| 9a357fc0-0ff3-359f-822e-0e5fd84f85e7 | -17.97244 | -57.31111 | 2024-10-14 05:12:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.8 |
| 3b6de388-e7d5-3b6c-a531-846c6006a95b | -17.97241 | -57.33634 | 2024-10-14 05:12:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.8 |
| f3ee5c7b-a273-3ea8-83ed-f49fad0ee018 | -17.97182 | -57.34044 | 2024-10-14 05:12:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.2 |
| 182923aa-f1f8-3f7a-bc0c-bd248d67aeb5 | -17.97128 | -57.2941 | 2024-10-14 05:12:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.3 |
| f24e504b-c28e-3976-91a0-8b150ca74f75 | -17.97122 | -57.34455 | 2024-10-14 05:12:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.2 |
| e63a44d5-cebb-3d48-ad7e-323af159b39c | -17.9701 | -57.30234 | 2024-10-14 05:12:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 5.8 |
| d707deb7-27f6-3db7-bdc4-06a7376f7b30 | -17.96951 | -57.30645 | 2024-10-14 05:12:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.3 |
| 7b2d37a5-c51e-33cd-9608-4a36d6020876 | -17.96948 | -57.33168 | 2024-10-14 05:12:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.8 |
| 1e8450c2-87a0-3ca8-bad0-abc95606bf23 | -17.96894 | -57.2853 | 2024-10-14 05:12:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.1 |
| 1b6fcac4-863b-3517-9a6c-dbcf3e14fa56 | -17.96892 | -57.31057 | 2024-10-14 05:12:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.3 |
| 9b0e7b4c-cb6b-37ca-9332-97ee6d37ebf0 | -17.96889 | -57.33578 | 2024-10-14 05:12:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.8 |
| e3128bdf-2de5-3045-958e-dd0b78d4be8e | -17.96835 | -57.28943 | 2024-10-14 05:12:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.3 |
| 6bea288a-a964-345e-b413-f640733eddd4 | -17.9683 | -57.3399 | 2024-10-14 05:12:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.2 |
| 5928cd3b-39ab-3c01-91b1-a8892c0eacea | -17.15502 | -56.84681 | 2024-10-14 05:12:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 0.6 |
| 47df4132-27e6-3ed0-8b62-64d34214fbc9 | -17.14729 | -56.84993 | 2024-10-14 05:12:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 0.7 |
| a3ec2d77-f784-3028-b98d-213eaaa454b5 | -17.14431 | -56.87093 | 2024-10-14 05:12:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.2 |
| f69f958a-f24b-37c1-8583-b0201bd327b0 | -17.14254 | -56.85779 | 2024-10-14 05:12:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.0 |
| 9dfe8631-c846-3725-961a-cd96a48078ae | -17.13897 | -56.85724 | 2024-10-14 05:12:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 0.6 |
| d0d81c21-db27-39b6-b86f-6307adc84104 | -17.13838 | -56.86145 | 2024-10-14 05:12:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 0.6 |
| 42e367c6-be02-385d-8888-6ba1a5aca03e | -17.13363 | -56.86929 | 2024-10-14 05:12:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 0.8 |
| 364a135b-e31e-3a2e-9d57-889e626e4a18 | -17.13303 | -56.87349 | 2024-10-14 05:12:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 0.7 |
| 92097dc9-08d9-3b17-968d-58bd643f24b2 | -17.12769 | -56.8598 | 2024-10-14 05:12:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 0.7 |
| 46f1f9a9-2c26-30e3-8fd5-ad8ec041a23f | -17.12651 | -56.86819 | 2024-10-14 05:12:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 0.6 |
| 2e720d3a-5f61-3403-af7b-12e507913687 | -17.12354 | -56.86345 | 2024-10-14 05:12:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.0 |
| a082c98a-6483-3d95-aa47-2a13c5d3eade | -17.12295 | -56.86765 | 2024-10-14 05:12:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.0 |
| df5e0b97-8930-3224-93ea-029c8408c7f1 | -17.11641 | -56.86236 | 2024-10-14 05:12:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.0 |
| 91336ced-c4e5-3c45-9db7-7f3a49194e02 | -17.02087 | -56.8496 | 2024-10-14 05:12:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.0 |
| b5715d7e-361e-3200-b7d7-fdcb6bd0d949 | -17.20115 | -57.47552 | 2024-10-14 05:12:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 4.4 |
| 1358af33-4fb7-3f81-9a8b-0512e0d482e6 | -17.19828 | -57.44653 | 2024-10-14 05:12:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.9 |
| bf4ccebb-1b5e-344b-82cd-5048380587e6 | -17.19826 | -57.47099 | 2024-10-14 05:12:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.6 |
| 85cfc27b-6f8a-3329-9a6d-ad5417c1f16f | -17.19768 | -57.47498 | 2024-10-14 05:12:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 4.4 |
| 7656a38a-c51a-3ac0-807f-9ffe65c0ab71 | -17.19709 | -57.47895 | 2024-10-14 05:12:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 4.4 |
| 90f10fa2-cb35-314a-9398-43daee3fa22d | -17.1948 | -57.44599 | 2024-10-14 05:12:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.9 |
| 3d509a28-4081-333c-a370-a08980a60c5d | -17.19479 | -57.47045 | 2024-10-14 05:12:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.0 |
| a18cc953-7fe5-3bb3-b569-abd28d67c93a | -17.19422 | -57.44998 | 2024-10-14 05:12:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 4.6 |
| 7b61153c-3616-3a01-8030-b6e8a80f02cf | -17.1942 | -57.47443 | 2024-10-14 05:12:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.4 |
| 68a5976f-30f7-35a2-85ad-63b7ed0f0398 | -17.19364 | -57.45397 | 2024-10-14 05:12:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 4.6 |
| cdc2015d-c179-3dd0-86ad-7ee540049fcc | -17.19362 | -57.4784 | 2024-10-14 05:12:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.4 |
| 8d7e2665-08b0-3919-9c5e-286f538c04c1 | -17.19307 | -57.43346 | 2024-10-14 05:12:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 4.7 |
| 48330e89-a048-3fd7-953e-65b0174fff8b | -17.19306 | -57.45795 | 2024-10-14 05:12:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.7 |
| 180693d2-3dea-34c4-8635-c26cc3fb0b3b | -17.19191 | -57.44145 | 2024-10-14 05:12:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 5.4 |
| 77f636a8-0f8d-356a-9711-2654a18c4751 | -17.19133 | -57.44544 | 2024-10-14 05:12:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 5.4 |
| e2e26fc5-713f-33a0-9479-4719e3e0ba41 | -17.19017 | -57.42893 | 2024-10-14 05:12:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.6 |
| e2b91e53-8d8d-3194-acf6-bb538231acc1 | -17.19016 | -57.45342 | 2024-10-14 05:12:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.0 |
| c11680c9-263e-324e-8310-dafaa79f41c5 | -17.19015 | -57.47787 | 2024-10-14 05:12:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.4 |
| 957a54f6-d5c7-3692-b199-942937569c13 | -17.18843 | -57.44091 | 2024-10-14 05:12:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 5.4 |
| 0659f4a2-3b89-311e-914a-99dc9c352cbc | -17.18785 | -57.4449 | 2024-10-14 05:12:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 5.4 |
| 51c3ca61-aea1-3dff-93ae-c8d53d4ca43e | -17.18669 | -57.45289 | 2024-10-14 05:12:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.0 |
| c0c7e16c-5a44-3bf8-9fb2-fab61ee54f27 | -17.18612 | -57.43238 | 2024-10-14 05:12:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.0 |
| 327ca265-2330-32dd-81be-76ad505ce815 | -17.18264 | -57.43183 | 2024-10-14 05:12:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.0 |
| 3fbab73f-775e-3c62-8467-4a5b67070c7a | -17.18206 | -57.43583 | 2024-10-14 05:12:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.0 |
| f9419027-a684-3236-8c10-8516940fc896 | -17.18148 | -57.41531 | 2024-10-14 05:12:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 0.6 |
| 90038299-c73b-3c47-bf85-0ce9c9b2ec95 | -17.17453 | -57.48763 | 2024-10-14 05:12:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.1 |
| e2d93f6a-6720-3e77-80e0-b5accdef297c | -17.17395 | -57.4916 | 2024-10-14 05:12:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.1 |
| b9df4927-3d78-30c5-b09b-639511bc2310 | -17.17163 | -57.4831 | 2024-10-14 05:12:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.4 |
| f7ac8a9f-8740-32ca-a470-12a418e17282 | -17.17105 | -57.48708 | 2024-10-14 05:12:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.5 |
| b1c18125-60ad-39a4-bc20-05ae8b2c32ce | -17.16874 | -57.47858 | 2024-10-14 05:12:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.4 |
| 7ec5d4b3-e3e3-3f03-8b37-3fda982ce777 | -17.86677 | -57.3919 | 2024-10-14 05:12:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 7.4 |
| d0bba5af-3d1c-3ce5-913f-2b5d0a80f577 | -17.16816 | -57.48256 | 2024-10-14 05:12:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.4 |
| 82f615ec-fed7-36d9-a741-291ed5762d35 | -17.16584 | -57.47406 | 2024-10-14 05:12:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 0.8 |
| cceae3a1-eec9-3493-9009-23f6c29fe22b | -17.02692 | -57.44111 | 2024-10-14 05:12:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.0 |
| fe549b50-0387-37d7-a62b-229557b3a67a | -17.02516 | -57.42863 | 2024-10-14 05:12:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.2 |


[Clique aqui para ver as próximas entradas](README127.md)
