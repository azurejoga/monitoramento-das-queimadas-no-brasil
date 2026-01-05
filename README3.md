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

## Dados Diários - Página 3

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 2c47fb7c-6d54-3491-9225-33d900d603ce | -4.59862 | -46.74337 | 2026-01-05 04:21:00 | NOAA-21 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| f51f5e5f-5184-3ae4-9b43-6628d8e107a6 | -5.06315 | -49.9335 | 2026-01-05 04:21:00 | NOAA-21 | ITUPIRANGA | PARÁ | Brasil | 1503705 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| a1b30eb1-872c-352f-9a7f-294929dc6a73 | -2.44829 | -47.78916 | 2026-01-05 04:21:00 | NOAA-21 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 8.3 |
| 9bdf5b50-e052-3753-9bf6-e8f197301274 | -3.88171 | -50.96875 | 2026-01-05 04:21:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 3bc940d2-2983-3583-bfe5-670c57109f08 | -4.39892 | -43.57474 | 2026-01-05 04:21:00 | NOAA-21 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 97cc2cbb-719f-38df-bf57-d1e3ffd63d48 | -4.68618 | -46.41701 | 2026-01-05 04:21:00 | NOAA-21 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 3e8b7d68-e6d2-3ee3-8a86-84ddb5be6222 | -4.41608 | -43.7273 | 2026-01-05 04:21:00 | NOAA-21 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 40257ad7-e4be-38a6-aa6f-7230d1ff64c2 | -4.69303 | -46.41808 | 2026-01-05 04:21:00 | NOAA-21 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 9fd45256-ee71-3ef2-bb76-9aeec98d559b | -5.35385 | -46.78625 | 2026-01-05 04:21:00 | NOAA-21 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| ac02e3e2-548e-34db-827d-10892f659b44 | -0.26062 | -48.78632 | 2026-01-05 04:21:00 | NOAA-21 | SOURE | PARÁ | Brasil | 1507904 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| b319d894-a7e4-3524-8c6d-b32599d8d128 | -4.68842 | -46.42501 | 2026-01-05 04:21:00 | NOAA-21 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| d4a0b826-e4db-3f42-8e46-cac4fb4fc3f2 | -7.74455 | -40.26678 | 2026-01-05 04:21:00 | NOAA-21 | TRINDADE | PERNAMBUCO | Brasil | 2615607 | 26 | 33 | nan | nan | nan | Caatinga | 2.5 |
| a588020a-f84f-3fdd-93f0-ec2cc99c2ce3 | -2.51131 | -49.06569 | 2026-01-05 04:21:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 226839fd-8bfa-3ea6-a927-455fe7d50504 | -2.45125 | -48.63611 | 2026-01-05 04:21:00 | NOAA-21 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 64f1a659-e605-3e6c-9204-4a975b7ccbd2 | -3.97324 | -47.04351 | 2026-01-05 04:21:00 | NOAA-21 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 5e8adfe1-920c-3d60-b5c7-7f4cb58623c8 | -2.48947 | -45.31737 | 2026-01-05 04:21:00 | NOAA-21 | PRESIDENTE SARNEY | MARANHÃO | Brasil | 2109270 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 1fb6757d-123d-37db-bb76-325eed904d11 | -4.69244 | -46.42181 | 2026-01-05 04:21:00 | NOAA-21 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 7a60c5a5-c9df-32aa-b619-5280c4726598 | -2.458 | -47.77668 | 2026-01-05 04:21:00 | NOAA-21 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 7fc29e7e-b6ab-3fab-b8c1-e2a6d3c27fe0 | -4.2239 | -46.86356 | 2026-01-05 04:21:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 37028f9a-c802-39c8-9d01-d5486bb97eed | -2.80573 | -53.00999 | 2026-01-05 04:21:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 1f45a1ef-2478-3f21-9be1-d337ffd89b32 | -1.48996 | -45.96026 | 2026-01-05 04:21:00 | NOAA-21 | LUÍS DOMINGUES | MARANHÃO | Brasil | 2106201 | 21 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 602290ae-0657-3d30-b47e-45eafb709711 | -1.31828 | -46.10995 | 2026-01-05 04:21:00 | NOAA-21 | CARUTAPERA | MARANHÃO | Brasil | 2102903 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| dd984cb3-df24-3469-91b9-5a7a03908618 | -2.91583 | -54.11958 | 2026-01-05 04:21:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 432094bd-77ea-3ce6-aa5f-8a73d3c2a385 | -4.68389 | -43.24885 | 2026-01-05 04:21:00 | NOAA-21 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 93d43827-26bd-37d0-b872-06d9ed89d844 | -2.8814 | -45.22276 | 2026-01-05 04:21:00 | NOAA-21 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 58912440-509e-3f10-94bf-94e933fffc8a | -1.59657 | -46.0191 | 2026-01-05 04:21:00 | NOAA-21 | AMAPÁ DO MARANHÃO | MARANHÃO | Brasil | 2100550 | 21 | 33 | nan | nan | nan | Amazônia | 2.1 |
| a551b602-ce31-3245-93e9-50196aae07ce | -4.68961 | -46.41754 | 2026-01-05 04:21:00 | NOAA-21 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 75b2b862-b253-342a-a46d-f4780afefa27 | -3.17448 | -52.8698 | 2026-01-05 04:21:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 1564cb21-7d62-3cdd-a52d-24bf2a993931 | -4.88033 | -47.92381 | 2026-01-05 04:21:00 | NOAA-21 | CIDELÂNDIA | MARANHÃO | Brasil | 2103257 | 21 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 3284192a-6d6a-3d4d-916e-bcc3dacfce50 | -2.45935 | -45.75776 | 2026-01-05 04:21:00 | NOAA-21 | SANTA LUZIA DO PARUÁ | MARANHÃO | Brasil | 2110039 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| b67d16e8-a731-371b-8556-53b25f5230f3 | -2.80151 | -53.0028 | 2026-01-05 04:21:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 953338ab-f5b1-3cc9-b827-2e396b2dc2bb | -2.51189 | -49.0621 | 2026-01-05 04:21:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| e4c9d2ee-85ef-3e45-8abb-ad7211cc389b | -3.92636 | -46.51477 | 2026-01-05 04:21:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| c43b61bb-475b-37a2-b0eb-4a9158786712 | -2.74153 | -42.59723 | 2026-01-05 04:21:00 | NOAA-21 | PAULINO NEVES | MARANHÃO | Brasil | 2108058 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| e8e01eff-d5e0-395a-a97c-c108ca64ad94 | -2.58042 | -44.9952 | 2026-01-05 04:21:00 | NOAA-21 | PERI MIRIM | MARANHÃO | Brasil | 2108405 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 41c7298c-5e28-3626-bfa1-781a9d2625b4 | -2.83368 | -48.65939 | 2026-01-05 04:21:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 4940afc5-b995-3696-96be-88446465fc6b | -4.50453 | -48.5181 | 2026-01-05 04:21:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 2bc46578-96b8-3141-811c-6c004cdbbcdc | -2.33411 | -45.81707 | 2026-01-05 04:21:00 | NOAA-21 | PRESIDENTE MÉDICI | MARANHÃO | Brasil | 2109239 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| ba584844-2c48-3937-8095-2e3d49848516 | -0.08786 | -51.27718 | 2026-01-05 04:21:00 | NOAA-21 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 10.4 |
| fd048ec2-5e3c-3fb8-a638-3436b82e6f52 | -2.43384 | -46.89582 | 2026-01-05 04:21:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 1ec9a378-73e2-353d-8a5a-4e3daf3953da | -5.40608 | -45.2018 | 2026-01-05 04:21:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 5fcfad13-ca88-3385-b9a7-b2a02e2f21c2 | -0.94073 | -46.92435 | 2026-01-05 04:21:00 | NOAA-21 | TRACUATEUA | PARÁ | Brasil | 1508035 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| c09f31ce-ddf4-3159-ba39-ca8d6e8bf5b2 | -4.29569 | -47.09211 | 2026-01-05 04:21:00 | NOAA-21 | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 20bd5497-efb5-3f90-9121-bc0bf94b84b0 | -4.68506 | -43.26353 | 2026-01-05 04:21:00 | NOAA-21 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 8dd6d888-fab3-3ffc-baee-9e23d67bc6d6 | -4.68335 | -43.2524 | 2026-01-05 04:21:00 | NOAA-21 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| a0164dfa-16e1-316f-8f36-65ac4dd22bda | -2.8343 | -48.65724 | 2026-01-05 04:21:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 230dfc5b-c692-3457-b18e-8e902349fbd6 | -2.461 | -47.78185 | 2026-01-05 04:21:00 | NOAA-21 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 21dd625f-32c1-34dd-bcba-4a2721dc95f7 | -1.33274 | -49.4094 | 2026-01-05 04:21:00 | NOAA-21 | MUANÁ | PARÁ | Brasil | 1504901 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| ad63a7e2-55ec-3121-aad8-f172ccb98537 | -4.87422 | -48.15041 | 2026-01-05 04:21:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| a8b8f529-911c-3769-959e-3ae31a56e781 | -3.9229 | -46.51423 | 2026-01-05 04:21:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| ff67e52b-cd26-3056-92d2-bcbddf3696c1 | -4.08472 | -46.59772 | 2026-01-05 04:21:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.7 |
| ac5bacfd-5bf1-37fe-9220-46ee4a00052b | -4.75238 | -46.59586 | 2026-01-05 04:21:00 | NOAA-21 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 81486a77-bf8f-3b8f-9606-06830251da67 | -4.8767 | -48.14911 | 2026-01-05 04:21:00 | NOAA-21 | VILA NOVA DOS MARTÍRIOS | MARANHÃO | Brasil | 2112852 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| fe80cef8-0220-3450-9887-6b86cb34bcfc | -2.03719 | -45.96229 | 2026-01-05 04:21:00 | NOAA-21 | MARACAÇUMÉ | MARANHÃO | Brasil | 2106326 | 21 | 33 | nan | nan | nan | Amazônia | 0.6 |
| da5d3422-24de-3718-8357-af440f29e896 | -3.17396 | -52.87294 | 2026-01-05 04:21:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| d3408499-6097-3b93-a137-87b4f673c805 | -3.97613 | -47.04802 | 2026-01-05 04:21:00 | NOAA-21 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 1da23f7c-8cb5-3020-b1a2-5fd931dd322b | -2.33128 | -45.81286 | 2026-01-05 04:21:00 | NOAA-21 | PRESIDENTE MÉDICI | MARANHÃO | Brasil | 2109239 | 21 | 33 | nan | nan | nan | Amazônia | 0.5 |
| d9b1a98a-838a-31d7-bb7c-1714075d503f | -5.56054 | -45.45139 | 2026-01-05 04:21:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 24c4f4a5-e691-3412-84d5-8d0f0d41657e | -1.32788 | -49.41264 | 2026-01-05 04:21:00 | NOAA-21 | MUANÁ | PARÁ | Brasil | 1504901 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 37e048d4-8f0e-382c-9bab-73aaad88e6fa | -2.45277 | -47.7852 | 2026-01-05 04:21:00 | NOAA-21 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 8.3 |
| 77ae1822-1bea-35c2-951b-90161616c4a7 | -4.73809 | -45.57598 | 2026-01-05 04:21:00 | NOAA-21 | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| a9f282d4-63aa-3991-9536-dd6fd86193a8 | -3.69478 | -47.22118 | 2026-01-05 04:21:00 | NOAA-21 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 9d5ee9be-49d4-34bc-9ff1-01dc870b6a24 | -3.88048 | -50.96494 | 2026-01-05 04:21:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 5f1d5264-bf38-3d75-ad4c-cad879546094 | -2.2525 | -44.78905 | 2026-01-05 04:21:00 | NOAA-21 | CENTRAL DO MARANHÃO | MARANHÃO | Brasil | 2103125 | 21 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 72c9471e-2aa5-3676-a764-f2bbc535e10a | -2.801 | -53.00585 | 2026-01-05 04:21:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| dd33ff45-5a1d-3772-b388-219170580588 | -6.95875 | -46.22331 | 2026-01-05 04:21:00 | NOAA-21 | FORTALEZA DOS NOGUEIRAS | MARANHÃO | Brasil | 2104107 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| c8ac391c-673b-3166-854e-5a39af2a2ac1 | -2.91789 | -54.12306 | 2026-01-05 04:21:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 3a55ff13-bbe4-302b-b59b-f6f31a81df5f | -4.68902 | -46.42126 | 2026-01-05 04:21:00 | NOAA-21 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 9c4e678d-b454-3b6b-ba43-005d108f1705 | -4.69113 | -43.24634 | 2026-01-05 04:21:00 | NOAA-21 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 9c164e6f-e415-3ee7-b3bd-4dd021433d54 | -4.59515 | -46.74283 | 2026-01-05 04:21:00 | NOAA-21 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 3.2 |
| ade2e0d7-d702-3e85-ba8a-e2eecd7836bc | -2.75718 | -54.2176 | 2026-01-05 04:21:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 8d04b303-1a69-3591-b35f-7014ce066cc6 | -2.72014 | -54.5491 | 2026-01-05 04:21:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 74bf0666-b5ff-33e4-ba3a-a62d2407e6e6 | -7.07883 | -39.13493 | 2026-01-05 04:21:00 | NOAA-21 | CARIRIAÇU | CEARÁ | Brasil | 2303204 | 23 | 33 | nan | nan | nan | Caatinga | 4.0 |
| 094e8529-437a-3501-91e0-97f4f99fc68a | -4.68172 | -43.26302 | 2026-01-05 04:21:00 | NOAA-21 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 70061b8e-066c-3c6a-8e17-c6bcb21aaf92 | -2.88531 | -45.21974 | 2026-01-05 04:21:00 | NOAA-21 | SÃO BENTO | MARANHÃO | Brasil | 2110500 | 21 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 7c37110c-8469-326f-bff0-5ae6bc14d3af | -4.57712 | -46.5958 | 2026-01-05 04:21:00 | NOAA-21 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 4cf191fb-2291-3a1c-ad42-ef11ae9092e4 | -4.82503 | -47.34081 | 2026-01-05 04:21:00 | NOAA-21 | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 5.6 |
| e5a228f5-529c-396b-913e-f5cbb4d0f879 | -3.97549 | -47.05197 | 2026-01-05 04:21:00 | NOAA-21 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 9b31e7d4-64ca-3c9f-882f-ae1e830a1971 | -4.7314 | -45.57496 | 2026-01-05 04:21:00 | NOAA-21 | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 1a648e96-eb1a-3c36-869e-22a3d921ab30 | -4.7353 | -45.57196 | 2026-01-05 04:21:00 | NOAA-21 | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 000e8cb1-8283-3aa2-b80d-b53abef5d11c | -2.45203 | -47.78975 | 2026-01-05 04:21:00 | NOAA-21 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 8.3 |
| d2f1df48-98b5-326c-ae34-ecb757d36059 | -0.94138 | -46.92013 | 2026-01-05 04:21:00 | NOAA-21 | TRACUATEUA | PARÁ | Brasil | 1508035 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 26842639-9644-3f63-95aa-7085b6648ffd | -2.9152 | -54.12347 | 2026-01-05 04:21:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 4b26a1f2-af44-3f67-925a-942742e7eafa | -2.45206 | -48.63112 | 2026-01-05 04:21:00 | NOAA-21 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| c9a4a052-9f24-3fc3-85a9-b6bc29f95939 | -5.63262 | -46.34237 | 2026-01-05 04:21:00 | NOAA-21 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| d505076b-1cac-3d4f-ad32-336386507d21 | -7.74169 | -40.26781 | 2026-01-05 04:21:00 | NOAA-21 | TRINDADE | PERNAMBUCO | Brasil | 2615607 | 26 | 33 | nan | nan | nan | Caatinga | 3.4 |
| 95faeb51-edd0-31fa-926f-9ee42abf4990 | -6.98089 | -40.95127 | 2026-01-05 04:21:00 | NOAA-21 | ALAGOINHA DO PIAUÍ | PIAUÍ | Brasil | 2200251 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| a756f827-9f04-31c4-b3a8-3907dbcbc682 | -2.44903 | -47.7846 | 2026-01-05 04:21:00 | NOAA-21 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 8.3 |
| f1d90690-131f-37e7-9799-3a50898d94e4 | -0.94132 | -46.92387 | 2026-01-05 04:21:00 | NOAA-21 | TRACUATEUA | PARÁ | Brasil | 1508035 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| f862e078-843c-3aff-9647-67249984a6e7 | -2.80726 | -53.00084 | 2026-01-05 04:21:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| e665fe72-ba6c-38b8-ac9a-48225310db36 | -2.57987 | -44.99871 | 2026-01-05 04:21:00 | NOAA-21 | PERI MIRIM | MARANHÃO | Brasil | 2108405 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 604f5464-a882-36d5-b932-21359f6ba0df | -2.33694 | -45.82129 | 2026-01-05 04:21:00 | NOAA-21 | PRESIDENTE MÉDICI | MARANHÃO | Brasil | 2109239 | 21 | 33 | nan | nan | nan | Amazônia | 0.3 |
| 32e903d3-ce43-37d7-8ff3-29ea1fa7cbc5 | -1.96132 | -46.62806 | 2026-01-05 04:21:00 | NOAA-21 | VISEU | PARÁ | Brasil | 1508308 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 5561b4ac-2c04-34f0-90e1-afba4cfaf6fa | -3.78027 | -47.4838 | 2026-01-05 04:21:00 | NOAA-21 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 5aa65b3f-6a80-3b50-94f9-8a7482b61cbf | -2.80625 | -53.00689 | 2026-01-05 04:21:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| a107eccd-7ba7-3506-9b73-98339c0fd93e | -3.17344 | -52.87604 | 2026-01-05 04:21:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 31054b52-dfd8-31ca-ab0d-2485e86141e8 | -9.80579 | -35.95161 | 2026-01-05 04:23:00 | NOAA-21 | BARRA DE SÃO MIGUEL | ALAGOAS | Brasil | 2700607 | 27 | 33 | nan | nan | nan | Mata Atlântica | 2.3 |
| c841bee6-dddc-3234-a36d-9bcfe2727c0d | -17.64947 | -56.44477 | 2026-01-05 04:23:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.7 |
| 89523bd1-18f0-3a5c-a400-442ef021d3a5 | -9.81973 | -36.15698 | 2026-01-05 04:23:00 | NOAA-21 | SÃO MIGUEL DOS CAMPOS | ALAGOAS | Brasil | 2708600 | 27 | 33 | nan | nan | nan | Mata Atlântica | 2.7 |
| f3436b49-12a0-353d-a92a-2ebaef15e7b4 | -18.82459 | -51.61509 | 2026-01-05 04:23:00 | NOAA-21 | ITAJÁ | GOIÁS | Brasil | 5210802 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |


[Clique aqui para ver as próximas entradas](README4.md)
