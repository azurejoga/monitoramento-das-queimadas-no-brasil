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

## Dados Diários - Página 125

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| fa4b8ce4-1b2f-3bee-838c-f90d3d0a81f1 | -4.70179 | -40.13343 | 2024-10-25 15:33:00 | NPP-375 | CATUNDA | CEARÁ | Brasil | 2303659 | 23 | 33 | nan | nan | nan | Caatinga | 6.9 |
| da8abcbd-6a3a-34f9-abc4-fa525afa3495 | -4.69969 | -40.13734 | 2024-10-25 15:33:00 | NPP-375 | CATUNDA | CEARÁ | Brasil | 2303659 | 23 | 33 | nan | nan | nan | Caatinga | 7.2 |
| 143d513e-58cd-3dbd-8b0e-a4ae0adcd9a5 | -4.69924 | -40.13431 | 2024-10-25 15:33:00 | NPP-375 | CATUNDA | CEARÁ | Brasil | 2303659 | 23 | 33 | nan | nan | nan | Caatinga | 8.1 |
| 7ea6deb8-e8cf-3d22-bb70-b3599f5b78dc | -4.32899 | -40.15224 | 2024-10-25 15:33:00 | NPP-375 | SANTA QUITÉRIA | CEARÁ | Brasil | 2312205 | 23 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 0f0f5851-bf62-3bfa-9648-53490f7f3d06 | -4.32413 | -40.48829 | 2024-10-25 15:33:00 | NPP-375 | HIDROLÂNDIA | CEARÁ | Brasil | 2305209 | 23 | 33 | nan | nan | nan | Caatinga | 5.3 |
| 50226901-de52-3a3d-9d01-8187a0839ec7 | -4.32391 | -40.1529 | 2024-10-25 15:33:00 | NPP-375 | SANTA QUITÉRIA | CEARÁ | Brasil | 2312205 | 23 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 51db2bee-0bad-3db9-aa76-708fa3d38f12 | -4.32389 | -40.49033 | 2024-10-25 15:33:00 | NPP-375 | HIDROLÂNDIA | CEARÁ | Brasil | 2305209 | 23 | 33 | nan | nan | nan | Caatinga | 2.8 |
| aa021eb6-92f1-3da8-a1f5-2e45b9ab133f | -4.32343 | -40.4872 | 2024-10-25 15:33:00 | NPP-375 | HIDROLÂNDIA | CEARÁ | Brasil | 2305209 | 23 | 33 | nan | nan | nan | Caatinga | 2.8 |
| aa856a16-52b5-3375-8574-efa2a68b02d6 | -4.30181 | -40.41173 | 2024-10-25 15:33:00 | NPP-375 | HIDROLÂNDIA | CEARÁ | Brasil | 2305209 | 23 | 33 | nan | nan | nan | Caatinga | 1.8 |
| ff0d576b-7e89-396b-a225-60c27e79ba80 | -4.64864 | -40.97493 | 2024-10-25 15:33:00 | NPP-375 | IPUEIRAS | CEARÁ | Brasil | 2305902 | 23 | 33 | nan | nan | nan | Caatinga | 5.7 |
| d0c15e1b-0cb6-345a-a6c9-731c23cfd5ed | -4.41611 | -40.91502 | 2024-10-25 15:33:00 | NPP-375 | CROATÁ | CEARÁ | Brasil | 2304236 | 23 | 33 | nan | nan | nan | Caatinga | 7.5 |
| 1d0fafe2-41e5-3cf2-853e-135a2b48a74c | -5.16588 | -40.5903 | 2024-10-25 15:33:00 | NPP-375 | CRATEÚS | CEARÁ | Brasil | 2304103 | 23 | 33 | nan | nan | nan | Caatinga | 1.9 |
| ea9ef150-ded7-3525-99f3-eae12b25035b | -5.86597 | -41.53539 | 2024-10-25 15:33:00 | NPP-375 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 9.0 |
| 88c8ae60-91b1-36bb-8bcf-66118bdb4915 | -5.8687 | -41.53879 | 2024-10-25 15:33:00 | NPP-375 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 3.3 |
| 7b544762-67db-352d-9506-6dc7d8442ae2 | -5.86819 | -41.535 | 2024-10-25 15:33:00 | NPP-375 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 3.4 |
| b9e910af-5e65-3751-8bf2-78d42753354f | -5.86247 | -41.53563 | 2024-10-25 15:33:00 | NPP-375 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 6.4 |
| 2ddedb56-5943-3ac1-9db2-42a34cfc9b12 | -5.57568 | -41.18965 | 2024-10-25 15:33:00 | NPP-375 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 6.2 |
| 4984a7f8-5570-3965-a308-a20c25108c40 | -5.39729 | -41.11409 | 2024-10-25 15:33:00 | NPP-375 | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | 12.5 |
| d33430a1-7b4c-3b3e-8b4d-e060b03bc0e6 | -5.39679 | -41.11047 | 2024-10-25 15:33:00 | NPP-375 | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | 28.3 |
| d7e9d27d-420f-3d0c-845a-94521d29b0a6 | -5.39179 | -41.11487 | 2024-10-25 15:33:00 | NPP-375 | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | 11.1 |
| f03f3e9a-3b3d-364a-8f7a-1c1d9797735f | -5.3913 | -41.11127 | 2024-10-25 15:33:00 | NPP-375 | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | 8.5 |
| 115f8128-c383-3ab6-9644-a57b2494b206 | -5.38782 | -41.12688 | 2024-10-25 15:33:00 | NPP-375 | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 7d4dcc08-a9d4-3212-b3b4-e2a8ab57de10 | -5.38763 | -41.1276 | 2024-10-25 15:33:00 | NPP-375 | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 609a5c84-8af0-36a4-86f3-4b4fa81319ac | -5.38629 | -41.11566 | 2024-10-25 15:33:00 | NPP-375 | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | 11.1 |
| 7ca8f657-73e4-39d6-a4ae-2dadc9724898 | -5.38601 | -41.11638 | 2024-10-25 15:33:00 | NPP-375 | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | 8.5 |
| 2faee907-9a04-3e48-8148-9eb1851b6e59 | -5.38581 | -41.1121 | 2024-10-25 15:33:00 | NPP-375 | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | 8.5 |
| 903ccb44-bd5c-398e-89e1-54083cf29407 | -5.3855 | -41.11282 | 2024-10-25 15:33:00 | NPP-375 | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | 5.7 |
| 33774a94-0f2b-348f-8b4e-fecb898ee096 | -5.26152 | -40.98988 | 2024-10-25 15:33:00 | NPP-375 | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | 5.6 |
| 539fa55b-9243-3b44-b2db-aa7b8bffccd5 | -5.2569 | -40.99102 | 2024-10-25 15:33:00 | NPP-375 | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | 11.7 |
| 9e4bf46e-7e6a-37a1-a9ef-aa8f4d746e3f | -5.25657 | -40.99405 | 2024-10-25 15:33:00 | NPP-375 | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | 5.6 |
| 8ade3ac6-d384-3c20-9ff1-7ef8bde0c7e4 | -5.25605 | -40.99041 | 2024-10-25 15:33:00 | NPP-375 | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | 5.6 |
| 379d2f49-8835-3bc5-bdd4-ddc2721f5bb7 | -5.25242 | -40.9989 | 2024-10-25 15:33:00 | NPP-375 | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | 7.1 |
| 4c58b3ca-42a7-355f-974c-26b08a402fe6 | -5.25193 | -40.99526 | 2024-10-25 15:33:00 | NPP-375 | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | 11.7 |
| 013392ce-7071-3ec4-9ced-ca474ff3995b | -5.25163 | -40.99827 | 2024-10-25 15:33:00 | NPP-375 | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | 8.1 |
| ba8cc489-9ba3-3589-bd32-e88d5e40c2ea | -5.25143 | -40.99162 | 2024-10-25 15:33:00 | NPP-375 | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | 11.7 |
| 56cd510b-8d3e-3514-a831-56673fa7cb80 | -5.25111 | -40.99464 | 2024-10-25 15:33:00 | NPP-375 | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | 17.7 |
| 8c3c206b-5faa-3cfd-87f8-268be40a35ec | -5.24955 | -41.17941 | 2024-10-25 15:33:00 | NPP-375 | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | 12.2 |
| c9f51c6c-253b-3a82-8b68-a9fe4580de68 | -5.24903 | -41.17571 | 2024-10-25 15:33:00 | NPP-375 | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | 12.4 |
| 89af0b2c-68b6-3454-bfb5-b13dd22aafa7 | -5.24353 | -41.17653 | 2024-10-25 15:33:00 | NPP-375 | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | 55.5 |
| ba98ce72-da4e-31b9-b904-a77b58f79f69 | -5.96185 | -40.98706 | 2024-10-25 15:33:00 | NPP-375 | ASSUNÇÃO DO PIAUÍ | PIAUÍ | Brasil | 2201051 | 22 | 33 | nan | nan | nan | Caatinga | 22.7 |
| bbcfc1a5-677c-3122-a70a-c904663e915a | -5.86651 | -41.5392 | 2024-10-25 15:33:00 | NPP-375 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 7.2 |
| cc8c3ba0-88db-3bbc-9cf2-82257ceab19c | -7.09609 | -41.14461 | 2024-10-25 15:33:00 | NPP-375 | FRANCISCO SANTOS | PIAUÍ | Brasil | 2204204 | 22 | 33 | nan | nan | nan | Caatinga | 6.7 |
| c7e0bc87-b740-371d-a353-b06f75520005 | -7.0046 | -41.30331 | 2024-10-25 15:33:00 | NPP-375 | SANTO ANTÔNIO DE LISBOA | PIAUÍ | Brasil | 2209401 | 22 | 33 | nan | nan | nan | Caatinga | 7.3 |
| 0e340c6f-4b04-3e84-9492-357f2b5bd352 | -6.86519 | -41.72305 | 2024-10-25 15:33:00 | NPP-375 | IPIRANGA DO PIAUÍ | PIAUÍ | Brasil | 2204808 | 22 | 33 | nan | nan | nan | Caatinga | 4.9 |
| 4bd230e9-acaa-3b73-891b-8c705b7d61c0 | -6.8339 | -41.65853 | 2024-10-25 15:33:00 | NPP-375 | IPIRANGA DO PIAUÍ | PIAUÍ | Brasil | 2204808 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 5441ddec-3f83-38fe-86d3-2bc4cedfab05 | -6.65134 | -41.9614 | 2024-10-25 15:33:00 | NPP-375 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 139.7 |
| ee54d672-e1fb-3300-ae70-9d27cecdd31e | -7.32945 | -42.17676 | 2024-10-25 15:33:00 | NPP-375 | COLÔNIA DO PIAUÍ | PIAUÍ | Brasil | 2202778 | 22 | 33 | nan | nan | nan | Caatinga | 3.6 |
| 24383c33-f9b1-3409-b441-40ee4100005e | -7.32901 | -42.17833 | 2024-10-25 15:33:00 | NPP-375 | COLÔNIA DO PIAUÍ | PIAUÍ | Brasil | 2202778 | 22 | 33 | nan | nan | nan | Caatinga | 4.0 |
| 5fc5f55a-b825-3525-8c69-0a3ba7f52d76 | -6.71213 | -41.10816 | 2024-10-25 15:33:00 | NPP-375 | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 2.2 |
| eb4dafff-6eea-3e1f-a9ae-74dd6259ec31 | -6.65406 | -41.95805 | 2024-10-25 15:33:00 | NPP-375 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 53.6 |
| 5a5d2f25-6f1d-388d-91ae-18be7e387bd1 | -6.65188 | -41.96534 | 2024-10-25 15:33:00 | NPP-375 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 44.4 |
| 9c77b0b5-d325-3174-b145-a52b2cf938c6 | -6.64855 | -41.96201 | 2024-10-25 15:33:00 | NPP-375 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 29.5 |
| 18ecdbd5-7386-39dd-aa51-bd34bd998edf | -6.45908 | -41.76982 | 2024-10-25 15:33:00 | NPP-375 | VALENÇA DO PIAUÍ | PIAUÍ | Brasil | 2211308 | 22 | 33 | nan | nan | nan | Caatinga | 14.1 |
| a40775e8-d9b3-397c-b42c-0ccfe3059627 | -6.9594 | -41.32222 | 2024-10-25 15:33:00 | NPP-375 | BOCAINA | PIAUÍ | Brasil | 2201804 | 22 | 33 | nan | nan | nan | Caatinga | 11.7 |
| fec801ef-71c9-39fa-846e-098d2ea53e31 | -6.83301 | -41.65861 | 2024-10-25 15:33:00 | NPP-375 | IPIRANGA DO PIAUÍ | PIAUÍ | Brasil | 2204808 | 22 | 33 | nan | nan | nan | Caatinga | 2.4 |
| b03d9229-7447-340e-910d-87ff7e9fb67d | -6.65454 | -41.96173 | 2024-10-25 15:33:00 | NPP-375 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 53.6 |
| b3736c41-7820-39de-a401-11bd0a770c84 | -6.45961 | -41.77375 | 2024-10-25 15:33:00 | NPP-375 | VALENÇA DO PIAUÍ | PIAUÍ | Brasil | 2211308 | 22 | 33 | nan | nan | nan | Caatinga | 14.1 |
| 34a0a467-3346-39e5-a3fa-4634976d550a | -6.45381 | -41.77476 | 2024-10-25 15:33:00 | NPP-375 | VALENÇA DO PIAUÍ | PIAUÍ | Brasil | 2211308 | 22 | 33 | nan | nan | nan | Caatinga | 14.1 |
| 1457e276-ef72-3a83-8903-3b5d2f4106ca | -6.45328 | -41.7708 | 2024-10-25 15:33:00 | NPP-375 | VALENÇA DO PIAUÍ | PIAUÍ | Brasil | 2211308 | 22 | 33 | nan | nan | nan | Caatinga | 14.1 |
| 053df063-b15b-3400-8473-6a0d9c114244 | -7.98242 | -41.03246 | 2024-10-25 15:33:00 | NPP-375 | PAULISTANA | PIAUÍ | Brasil | 2207801 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| c5833829-2b26-34fb-8aaa-fdca11be6fec | -7.41679 | -41.79522 | 2024-10-25 15:33:00 | NPP-375 | FLORESTA DO PIAUÍ | PIAUÍ | Brasil | 2203859 | 22 | 33 | nan | nan | nan | Caatinga | 2.9 |
| bd7bef99-8a00-3b12-b9e0-0738b8420445 | -7.00329 | -41.30366 | 2024-10-25 15:33:00 | NPP-375 | SANTO ANTÔNIO DE LISBOA | PIAUÍ | Brasil | 2209401 | 22 | 33 | nan | nan | nan | Caatinga | 7.9 |
| ed2e1f4e-d103-34ed-8e34-f7fa882fe560 | -8.54998 | -41.14166 | 2024-10-25 15:33:00 | NPP-375 | AFRÂNIO | PERNAMBUCO | Brasil | 2600203 | 26 | 33 | nan | nan | nan | Caatinga | 4.1 |
| 5a388f96-5745-3529-bb52-fd869cb4a253 | -8.43811 | -40.90466 | 2024-10-25 15:33:00 | NPP-375 | AFRÂNIO | PERNAMBUCO | Brasil | 2600203 | 26 | 33 | nan | nan | nan | Caatinga | 9.2 |
| 0a2c949a-2160-302c-ba9a-2d28bc1703d9 | -9.21255 | -42.32273 | 2024-10-25 15:33:00 | NPP-375 | DIRCEU ARCOVERDE | PIAUÍ | Brasil | 2203354 | 22 | 33 | nan | nan | nan | Caatinga | 6.9 |
| e84618e2-69e3-3607-ae7e-1e598fd65bf2 | -9.17371 | -41.41887 | 2024-10-25 15:33:00 | NPP-375 | CASA NOVA | BAHIA | Brasil | 2907202 | 29 | 33 | nan | nan | nan | Caatinga | 7.8 |
| 470f0491-d963-3135-a35a-e89a1505cf34 | -8.87955 | -41.04732 | 2024-10-25 15:33:00 | NPP-375 | CASA NOVA | BAHIA | Brasil | 2907202 | 29 | 33 | nan | nan | nan | Caatinga | 4.7 |
| efe9382d-c308-36b1-8067-203b49fa740e | -8.85352 | -41.39454 | 2024-10-25 15:33:00 | NPP-375 | CASA NOVA | BAHIA | Brasil | 2907202 | 29 | 33 | nan | nan | nan | Caatinga | 6.1 |
| 0ad6bc48-4529-3f1d-b44d-dede3d9b6ff0 | -8.81026 | -41.09983 | 2024-10-25 15:33:00 | NPP-375 | CASA NOVA | BAHIA | Brasil | 2907202 | 29 | 33 | nan | nan | nan | Caatinga | 8.7 |
| 0bec3029-7a90-3f5c-bb94-df90666a2fa7 | -8.77762 | -42.17244 | 2024-10-25 15:33:00 | NPP-375 | CORONEL JOSÉ DIAS | PIAUÍ | Brasil | 2202851 | 22 | 33 | nan | nan | nan | Caatinga | 5.3 |
| 01591d7d-2f2d-36e8-8122-ce0f664cb441 | -8.75577 | -41.32114 | 2024-10-25 15:33:00 | NPP-375 | CASA NOVA | BAHIA | Brasil | 2907202 | 29 | 33 | nan | nan | nan | Caatinga | 2.6 |
| c966e652-bd85-3643-ab7e-e68c681e6615 | -8.7499 | -41.32163 | 2024-10-25 15:33:00 | NPP-375 | CASA NOVA | BAHIA | Brasil | 2907202 | 29 | 33 | nan | nan | nan | Caatinga | 2.6 |
| 0ee1329b-5aad-38b0-8f35-8f486e4330a3 | -8.5512 | -41.14373 | 2024-10-25 15:33:00 | NPP-375 | AFRÂNIO | PERNAMBUCO | Brasil | 2600203 | 26 | 33 | nan | nan | nan | Caatinga | 3.9 |
| 3152eff7-9bcf-3440-8787-f02fa531be7c | -8.44185 | -40.9046 | 2024-10-25 15:33:00 | NPP-375 | AFRÂNIO | PERNAMBUCO | Brasil | 2600203 | 26 | 33 | nan | nan | nan | Caatinga | 5.6 |
| 4e80420f-0a98-3cf9-90c5-bb0217f1a54c | -8.10581 | -41.21186 | 2024-10-25 15:33:00 | NPP-375 | PAULISTANA | PIAUÍ | Brasil | 2207801 | 22 | 33 | nan | nan | nan | Caatinga | 9.2 |
| e348e5c1-2fe0-39c9-b494-662c34c5e2d7 | -7.9999 | -42.35339 | 2024-10-25 15:33:00 | NPP-375 | PEDRO LAURENTINO | PIAUÍ | Brasil | 2207934 | 22 | 33 | nan | nan | nan | Caatinga | 4.1 |
| 90e91d6a-5fa6-3bb2-8094-128f134a9516 | -7.89123 | -42.09471 | 2024-10-25 15:33:00 | NPP-375 | SIMPLÍCIO MENDES | PIAUÍ | Brasil | 2210805 | 22 | 33 | nan | nan | nan | Caatinga | 3.0 |
| 968db14d-502f-357b-9a5f-306030559690 | -7.88516 | -42.09556 | 2024-10-25 15:33:00 | NPP-375 | SIMPLÍCIO MENDES | PIAUÍ | Brasil | 2210805 | 22 | 33 | nan | nan | nan | Caatinga | 3.0 |
| cf46c2be-8403-3f2d-b9fa-f5c5ec7f3417 | -8.87993 | -41.04707 | 2024-10-25 15:33:00 | NPP-375 | CASA NOVA | BAHIA | Brasil | 2907202 | 29 | 33 | nan | nan | nan | Caatinga | 3.2 |
| e5d4a974-a24d-338f-bac9-064505e46475 | -8.82732 | -41.00486 | 2024-10-25 15:33:00 | NPP-375 | AFRÂNIO | PERNAMBUCO | Brasil | 2600203 | 26 | 33 | nan | nan | nan | Caatinga | 3.0 |
| cd657640-8a07-322f-b00e-a1469493ba31 | -8.77188 | -41.49389 | 2024-10-25 15:33:00 | NPP-375 | LAGOA DO BARRO DO PIAUÍ | PIAUÍ | Brasil | 2205565 | 22 | 33 | nan | nan | nan | Caatinga | 2.6 |
| 6e5ce5c3-0c48-3b0c-b5f1-f18d35aa1731 | -8.5505 | -41.14558 | 2024-10-25 15:33:00 | NPP-375 | AFRÂNIO | PERNAMBUCO | Brasil | 2600203 | 26 | 33 | nan | nan | nan | Caatinga | 2.9 |
| d056d27d-d2b7-346b-a114-e68e001cc8af | -8.43616 | -40.90516 | 2024-10-25 15:33:00 | NPP-375 | AFRÂNIO | PERNAMBUCO | Brasil | 2600203 | 26 | 33 | nan | nan | nan | Caatinga | 5.6 |
| 122b8109-bef1-3d79-be1e-767406b8f9ac | -9.94864 | -42.47193 | 2024-10-25 15:33:00 | NPP-375 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Caatinga | 4.2 |
| d89fbac3-d2e0-3a92-b5a6-0f53c37b4899 | -10.51265 | -42.39663 | 2024-10-25 15:33:00 | NPP-375 | XIQUE-XIQUE | BAHIA | Brasil | 2933604 | 29 | 33 | nan | nan | nan | Caatinga | 8.1 |
| c6ce4dbb-e90c-3a5a-9a7c-ff7e9f8a9820 | -10.51211 | -42.39952 | 2024-10-25 15:33:00 | NPP-375 | XIQUE-XIQUE | BAHIA | Brasil | 2933604 | 29 | 33 | nan | nan | nan | Caatinga | 8.9 |
| 8020bb1f-342a-3ed2-9451-cc7a2c040449 | -10.29757 | -42.41178 | 2024-10-25 15:33:00 | NPP-375 | XIQUE-XIQUE | BAHIA | Brasil | 2933604 | 29 | 33 | nan | nan | nan | Caatinga | 9.1 |
| 1970c275-2928-35ad-ab4b-2a0d5c6ee4c0 | -10.29619 | -42.40991 | 2024-10-25 15:33:00 | NPP-375 | XIQUE-XIQUE | BAHIA | Brasil | 2933604 | 29 | 33 | nan | nan | nan | Caatinga | 10.9 |
| 38c5d976-f07d-3cda-8492-6cef11a2c4a7 | -10.29578 | -42.39621 | 2024-10-25 15:33:00 | NPP-375 | XIQUE-XIQUE | BAHIA | Brasil | 2933604 | 29 | 33 | nan | nan | nan | Caatinga | 9.2 |
| 407a3c7c-4dfd-3a0a-89c2-1bb0061490c8 | -10.29492 | -42.39956 | 2024-10-25 15:33:00 | NPP-375 | XIQUE-XIQUE | BAHIA | Brasil | 2933604 | 29 | 33 | nan | nan | nan | Caatinga | 15.8 |
| c462ba07-d83a-3d43-a541-01748a3a3785 | -10.28999 | -42.40216 | 2024-10-25 15:33:00 | NPP-375 | XIQUE-XIQUE | BAHIA | Brasil | 2933604 | 29 | 33 | nan | nan | nan | Caatinga | 7.7 |
| c8931921-1047-3f6f-b25d-2f431e8e479c | -10.28854 | -42.4003 | 2024-10-25 15:33:00 | NPP-375 | XIQUE-XIQUE | BAHIA | Brasil | 2933604 | 29 | 33 | nan | nan | nan | Caatinga | 5.5 |
| da840a0c-d857-37bd-937b-0959787e9a0a | -10.16344 | -42.45442 | 2024-10-25 15:33:00 | NPP-375 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Caatinga | 9.6 |
| 1c2d04c1-d2d5-3bc2-a80b-0f584de78ad3 | -10.16282 | -42.44922 | 2024-10-25 15:33:00 | NPP-375 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Caatinga | 10.4 |
| 15bd0179-37e9-33b6-a844-cad44331c155 | -10.04147 | -42.69432 | 2024-10-25 15:33:00 | NPP-375 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Caatinga | 4.4 |
| 2ddbfae5-51f4-3624-b2d6-dc4ce73fd609 | -10.04142 | -42.69708 | 2024-10-25 15:33:00 | NPP-375 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Caatinga | 6.3 |
| c5bd86e5-cbad-3928-86ea-002855a23034 | -12.09739 | -42.24532 | 2024-10-25 15:33:00 | NPP-375 | BROTAS DE MACAÚBAS | BAHIA | Brasil | 2904506 | 29 | 33 | nan | nan | nan | Caatinga | 14.1 |
| 7a22fd53-44f3-3f9c-a10f-a3f434df2bb1 | -12.05829 | -42.86648 | 2024-10-25 15:33:00 | NPP-375 | OLIVEIRA DOS BREJINHOS | BAHIA | Brasil | 2923209 | 29 | 33 | nan | nan | nan | Caatinga | 8.8 |
| a251aaed-8728-39ee-9423-0c35e7caac2d | -11.87966 | -42.59026 | 2024-10-25 15:33:00 | NPP-375 | IPUPIARA | BAHIA | Brasil | 2914109 | 29 | 33 | nan | nan | nan | Caatinga | 3.8 |
| 6d6bc7b2-6136-3cb5-a3b7-377c3edf3dbd | -11.84107 | -41.85584 | 2024-10-25 15:33:00 | NPP-375 | BARRO ALTO | BAHIA | Brasil | 2903235 | 29 | 33 | nan | nan | nan | Caatinga | 4.6 |


[Clique aqui para ver as próximas entradas](README126.md)
