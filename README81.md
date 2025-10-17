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

## Dados Diários - Página 81

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| cdefa621-fa05-3f58-9b2a-33f874d220b1 | -6.29333 | -45.50331 | 2025-10-17 04:49:00 | NPP-375D | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| ca31bcca-827b-31c1-b022-e49b4c18252f | -6.49265 | -47.22534 | 2025-10-17 04:49:00 | NPP-375D | PORTO FRANCO | MARANHÃO | Brasil | 2109007 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 6e3a94db-29a2-30f0-bbd4-ed8f6f424e19 | -6.47082 | -41.85099 | 2025-10-17 04:49:00 | NPP-375D | VALENÇA DO PIAUÍ | PIAUÍ | Brasil | 2211308 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| a7472374-3861-378a-8ecf-6ade34d723ae | -5.13894 | -44.96145 | 2025-10-17 04:49:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 43d8c02e-5e45-36d5-85ba-15a89797b04c | -4.21789 | -48.35929 | 2025-10-17 04:49:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 0062bcdc-78db-3c66-af92-34102631e1e3 | -5.85696 | -42.3427 | 2025-10-17 04:49:00 | NPP-375D | PASSAGEM FRANCA DO PIAUÍ | PIAUÍ | Brasil | 2207751 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 1a35823b-fda8-3e96-a041-4199ea263eaf | -3.52772 | -50.30784 | 2025-10-17 04:49:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 0c892484-be26-3d55-894d-fb4a7fee5bbf | -7.90418 | -44.98248 | 2025-10-17 04:49:00 | NPP-375D | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 4.2 |
| cfee4436-1f9a-32ee-81ca-e0478ebedc5f | -5.83531 | -40.81169 | 2025-10-17 04:49:00 | NPP-375D | QUITERIANÓPOLIS | CEARÁ | Brasil | 2311264 | 23 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 9232fa0b-aa7e-370f-b07a-1fbe06b1a427 | -7.45513 | -42.15453 | 2025-10-17 04:49:00 | NPP-375D | SANTO INÁCIO DO PIAUÍ | PIAUÍ | Brasil | 2209500 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| ea8ae069-bfd1-3ede-bf49-774d39ac1806 | -5.41377 | -44.25254 | 2025-10-17 04:49:00 | NPP-375D | GRAÇA ARANHA | MARANHÃO | Brasil | 2104701 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 3ffbe513-d222-3fd6-8180-3618c52a0529 | -3.34908 | -49.25083 | 2025-10-17 04:49:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 31109ff8-48c7-358c-881b-c4a417415d86 | -3.5031 | -52.49252 | 2025-10-17 04:49:00 | NPP-375D | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 5.7 |
| d5d2e2bb-a98a-30b7-8920-89421455f1c4 | -7.28081 | -41.95116 | 2025-10-17 04:49:00 | NPP-375D | WALL FERRAZ | PIAUÍ | Brasil | 2211704 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 8ec15b9c-d305-3d93-bffe-82d1a1bc0346 | -2.74526 | -49.38834 | 2025-10-17 04:49:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 11.8 |
| d24c02c9-cdc7-3150-a660-465e0377bc91 | -6.32031 | -40.94175 | 2025-10-17 04:49:00 | NPP-375D | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 2.5 |
| cb283a2d-a61b-374c-babf-616434f895d2 | -7.04531 | -42.73919 | 2025-10-17 04:49:00 | NPP-375D | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 15a3246c-e0ad-397c-9b44-1fa3275289e6 | -6.94916 | -47.71906 | 2025-10-17 04:49:00 | NPP-375D | BABAÇULÂNDIA | TOCANTINS | Brasil | 1703008 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 098d1ccd-5225-3b60-b385-41a4e8a45183 | -7.02856 | -41.82436 | 2025-10-17 04:49:00 | NPP-375D | SÃO JOÃO DA VARJOTA | PIAUÍ | Brasil | 2209955 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 2cf0e00b-c777-31cf-ad60-730a5b7026ef | -5.26181 | -44.21387 | 2025-10-17 04:49:00 | NPP-375D | GONÇALVES DIAS | MARANHÃO | Brasil | 2104404 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 5ea72105-7cbf-32b1-ad8b-105ae55b9392 | -7.66746 | -42.59332 | 2025-10-17 04:49:00 | NPP-375D | RIBEIRA DO PIAUÍ | PIAUÍ | Brasil | 2208874 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 44eadd42-4b2b-3ac5-9399-b0a2aba2d74e | -6.03589 | -41.91104 | 2025-10-17 04:49:00 | NPP-375D | SANTA CRUZ DOS MILAGRES | PIAUÍ | Brasil | 2209153 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 1d1af3a1-c505-3d64-a63f-3fffdb3176d7 | -5.48031 | -48.654 | 2025-10-17 04:49:00 | NPP-375D | SÃO JOÃO DO ARAGUAIA | PARÁ | Brasil | 1507508 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| b37938ee-2f9f-3b2c-97f2-56d70436a557 | -3.23076 | -45.9638 | 2025-10-17 04:49:00 | NPP-375D | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 973e9a48-73c7-329a-88f9-66edb8846c6f | -7.95436 | -44.11668 | 2025-10-17 04:49:00 | NPP-375D | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 6.1 |
| 2a1fcaf7-976c-3eb5-8af0-5c1b24a34a12 | -5.84496 | -43.88807 | 2025-10-17 04:49:00 | NPP-375D | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| b9623190-4d79-3d2c-aeae-9c429fb50782 | -7.34745 | -43.863 | 2025-10-17 04:49:00 | NPP-375D | LANDRI SALES | PIAUÍ | Brasil | 2205607 | 22 | 33 | nan | nan | nan | Cerrado | 15.8 |
| 772c4170-ec59-365c-b127-7ebb6369c9b0 | -1.7028 | -55.68564 | 2025-10-17 04:49:00 | NPP-375D | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| d9cbdda9-83ec-306f-95fd-485aa3f399be | -5.10185 | -56.15292 | 2025-10-17 04:49:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 873df149-81ca-3ec4-9362-cc0d12b93aaa | -7.46634 | -42.65865 | 2025-10-17 04:49:00 | NPP-375D | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 3.2 |
| 7c392728-6d4e-3cd3-beca-7110d647a12a | -4.7227 | -46.15645 | 2025-10-17 04:49:00 | NPP-375D | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 53fd1916-3bc8-3f9f-ac2b-9080e0f1ff99 | -5.15664 | -46.2703 | 2025-10-17 04:49:00 | NPP-375D | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Amazônia | 1.7 |
| bb76facc-00fb-38cc-a9f4-fa1264b79530 | -3.9292 | -49.4276 | 2025-10-17 04:49:00 | NPP-375D | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 5cb25ed5-0820-33b5-ac0c-dd0142b03012 | -5.03641 | -49.21894 | 2025-10-17 04:49:00 | NPP-375D | NOVA IPIXUNA | PARÁ | Brasil | 1504976 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 5b68d557-e400-3755-a15d-c30d0055d4f5 | -3.97775 | -42.49191 | 2025-10-17 04:49:00 | NPP-375D | CAMPO LARGO DO PIAUÍ | PIAUÍ | Brasil | 2202174 | 22 | 33 | nan | nan | nan | Caatinga | 5.1 |
| 2a342cb0-4542-3476-8bce-3de857c4c85d | -5.91291 | -43.94275 | 2025-10-17 04:49:00 | NPP-375D | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 78738c5a-2abd-32a6-a7c1-873be9e2b13a | -6.03635 | -41.9078 | 2025-10-17 04:49:00 | NPP-375D | SANTA CRUZ DOS MILAGRES | PIAUÍ | Brasil | 2209153 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| e0be84fa-4fec-3ead-9051-9709135db786 | -6.30195 | -45.53162 | 2025-10-17 04:49:00 | NPP-375D | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| db360393-8789-3273-9d29-e7e033a436f8 | -7.45897 | -42.67336 | 2025-10-17 04:49:00 | NPP-375D | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| d3747be3-b07e-3e30-80b2-1e0a7b8df55b | -6.74891 | -44.37798 | 2025-10-17 04:49:00 | NPP-375D | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 258a2064-ad74-3156-a1d6-382a0861ce50 | -7.82638 | -44.13121 | 2025-10-17 04:49:00 | NPP-375D | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 5.4 |
| adb30850-11a9-3014-887b-f3a03198f1bc | -7.16005 | -44.99669 | 2025-10-17 04:49:00 | NPP-375D | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 17edef99-043f-36ce-8499-c8e23ba6bce6 | -5.90108 | -44.7394 | 2025-10-17 04:49:00 | NPP-375D | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 8f180f94-98e3-3ab5-8569-f4ba7ebfab25 | -5.25344 | -44.20805 | 2025-10-17 04:49:00 | NPP-375D | GONÇALVES DIAS | MARANHÃO | Brasil | 2104404 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| fc58cd4b-f0a6-3771-956c-fd315b36b38a | -4.72663 | -46.15708 | 2025-10-17 04:49:00 | NPP-375D | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 21f4bf57-856f-3078-ad8c-38f3c1d6e101 | -1.67358 | -55.81894 | 2025-10-17 04:49:00 | NPP-375D | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| f7999b02-9ac2-3e66-93b9-b58d542dd643 | -7.27912 | -42.3211 | 2025-10-17 04:49:00 | NPP-375D | COLÔNIA DO PIAUÍ | PIAUÍ | Brasil | 2202778 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 824386e0-8a1e-31a4-b52a-6fb2853c9986 | -3.66188 | -50.26859 | 2025-10-17 04:49:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 29474b8c-26c0-3811-9e1a-a43cd2a03b87 | -6.21392 | -47.87872 | 2025-10-17 04:49:00 | NPP-375D | LUZINÓPOLIS | TOCANTINS | Brasil | 1712454 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 3cb7a239-9fee-3943-97cd-b73338026638 | -3.51532 | -50.21385 | 2025-10-17 04:49:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| ebeb5527-f712-301d-aad0-31f15814ac0f | -6.26145 | -43.90694 | 2025-10-17 04:49:00 | NPP-375D | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 517e0c9e-2e2f-3e86-8e6c-0179c94c1c9c | -6.68801 | -40.87851 | 2025-10-17 04:49:00 | NPP-375D | PIO IX | PIAUÍ | Brasil | 2208205 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| b3eafdb7-a1dd-376b-88bf-0a6f8ce3ad6f | -6.21608 | -41.54466 | 2025-10-17 04:49:00 | NPP-375D | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 2ab366c0-aa4f-344f-b2da-71455ebfcf5a | -2.74581 | -49.38483 | 2025-10-17 04:49:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| e18b47ea-7adf-372f-8469-53f80190ddd8 | -7.22374 | -47.86955 | 2025-10-17 04:49:00 | NPP-375D | BABAÇULÂNDIA | TOCANTINS | Brasil | 1703008 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 3ffd3f45-bd41-3da8-b390-acd05c41f3ff | -6.05704 | -44.52457 | 2025-10-17 04:49:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 2dfc7add-94e3-312c-82f5-53f1bd1a909b | -4.343 | -48.67389 | 2025-10-17 04:49:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 7323b70c-3750-38a4-abc5-fb814b23fa56 | -1.89301 | -51.01525 | 2025-10-17 04:49:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| be4a4bfe-6a5d-3b79-8649-06ac65f24f20 | -3.92786 | -53.80971 | 2025-10-17 04:49:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 51694415-d67b-3037-801e-c06d7cec0b7b | -6.30241 | -45.58552 | 2025-10-17 04:49:00 | NPP-375D | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| c4e9bfa6-6a97-33d2-817a-a6206b733ef5 | -3.84929 | -41.57405 | 2025-10-17 04:49:00 | NPP-375D | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 2.4 |
| 8ba40618-5157-3ee2-987b-fcdac6dbf61d | -3.83845 | -47.41298 | 2025-10-17 04:49:00 | NPP-375D | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 3f3b7c1c-6890-36e0-ae73-6ddac5b4a0dc | -8.18957 | -42.35469 | 2025-10-17 04:49:00 | NPP-375D | SÃO JOÃO DO PIAUÍ | PIAUÍ | Brasil | 2210003 | 22 | 33 | nan | nan | nan | Caatinga | 0.4 |
| 99b28878-873c-3b30-8928-74b50d604a00 | -6.14036 | -41.72697 | 2025-10-17 04:49:00 | NPP-375D | AROAZES | PIAUÍ | Brasil | 2200905 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| b2a18de1-23f6-3f6e-bf1d-44d6c979d710 | -3.51001 | -52.4936 | 2025-10-17 04:49:00 | NPP-375D | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 9ed44305-0389-3bfd-bc4a-4a5779639812 | -5.80871 | -43.08118 | 2025-10-17 04:49:00 | NPP-375D | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 3.1 |
| ca9fd592-eb37-3e45-a8fa-9d6f7d7301da | -8.18485 | -43.96091 | 2025-10-17 04:49:00 | NPP-375D | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| f26baa79-60fd-3155-bb30-f01a5f133317 | -7.1833 | -42.3569 | 2025-10-17 04:49:00 | NPP-375D | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 048ef85e-bedd-3345-9a64-cc6d08964d89 | -6.42838 | -44.03869 | 2025-10-17 04:49:00 | NPP-375D | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 80381d7e-43c0-30d0-9f7d-a0585c65bd22 | -7.76063 | -42.4548 | 2025-10-17 04:49:00 | NPP-375D | SOCORRO DO PIAUÍ | PIAUÍ | Brasil | 2210904 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| db163292-a8b6-3b21-916e-9d459a55ea11 | -7.20984 | -43.83955 | 2025-10-17 04:49:00 | NPP-375D | LANDRI SALES | PIAUÍ | Brasil | 2205607 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 954d1fdf-f035-36e3-8c42-529bed1436a1 | -5.72061 | -44.51019 | 2025-10-17 04:49:00 | NPP-375D | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| e471601a-1e41-3f4b-8a0d-dc9b9149e0d9 | -2.7442 | -48.30527 | 2025-10-17 04:49:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 6e8f92ad-e297-378b-9984-5dbea7780555 | -4.81436 | -45.73107 | 2025-10-17 04:49:00 | NPP-375D | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 4ab21a90-8d39-32c9-ba05-70781d13699a | -7.22439 | -47.86523 | 2025-10-17 04:49:00 | NPP-375D | BABAÇULÂNDIA | TOCANTINS | Brasil | 1703008 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 67ec6c43-32cc-3d60-8539-448d227bcdb3 | -5.87792 | -43.85779 | 2025-10-17 04:49:00 | NPP-375D | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| c15fbf0c-769a-3155-8e60-6e3d4034dfbc | -4.41987 | -43.40421 | 2025-10-17 04:49:00 | NPP-375D | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 2020fac4-b8ac-37d7-bb63-9477dc95b6f7 | -5.31366 | -42.94139 | 2025-10-17 04:49:00 | NPP-375D | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 00f4cbdc-82b6-369b-8b8a-3c810ba37bc4 | -8.19494 | -42.3554 | 2025-10-17 04:49:00 | NPP-375D | SÃO JOÃO DO PIAUÍ | PIAUÍ | Brasil | 2210003 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| d28aca27-a243-3f9a-aa3c-f0911c7ac55f | -5.9172 | -44.74802 | 2025-10-17 04:49:00 | NPP-375D | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 8.5 |
| 6a01b1b5-8762-352b-a3b6-bdcf333beea2 | -6.03053 | -41.91033 | 2025-10-17 04:49:00 | NPP-375D | SANTA CRUZ DOS MILAGRES | PIAUÍ | Brasil | 2209153 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 24173405-ce21-312c-9788-0ed26fe49592 | -6.31281 | -40.94243 | 2025-10-17 04:49:00 | NPP-375D | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 4de78db2-cff1-31e9-a140-3fa6a19958cd | -5.09509 | -45.4322 | 2025-10-17 04:49:00 | NPP-375D | ITAIPAVA DO GRAJAÚ | MARANHÃO | Brasil | 2105351 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 0049562a-44a4-315f-bc41-ff856080a4e2 | -7.48884 | -47.03418 | 2025-10-17 04:49:00 | NPP-375D | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 887d7222-d579-3f9f-837c-5e88b03c100b | -1.73567 | -54.43662 | 2025-10-17 04:49:00 | NPP-375D | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 28093685-bc6f-3c8d-ab41-90f895d2cc77 | -6.75607 | -42.36142 | 2025-10-17 04:49:00 | NPP-375D | CAJAZEIRAS DO PIAUÍ | PIAUÍ | Brasil | 2202075 | 22 | 33 | nan | nan | nan | Caatinga | 2.8 |
| 9e43a5d8-c1c8-305c-b55f-3364d87efed1 | -5.71487 | -44.5181 | 2025-10-17 04:49:00 | NPP-375D | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 114cb5f8-b2b5-36f1-a652-edb3f2d51b11 | -6.58936 | -47.07026 | 2025-10-17 04:49:00 | NPP-375D | SÃO JOÃO DO PARAÍSO | MARANHÃO | Brasil | 2111052 | 21 | 33 | nan | nan | nan | Cerrado | 8.0 |
| 7e09ed6c-08a0-3e45-990f-335296ed1ad6 | -7.94558 | -44.11038 | 2025-10-17 04:49:00 | NPP-375D | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 3.1 |
| f064529e-6372-3185-b538-a8b0bd06585d | -5.86998 | -43.91213 | 2025-10-17 04:49:00 | NPP-375D | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 576a4dcc-f2c4-3fa1-87ed-d30988ede9bf | -3.69175 | -51.17154 | 2025-10-17 04:49:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 34aa475f-3662-399f-980a-977867a0b7f5 | -1.89747 | -51.00875 | 2025-10-17 04:49:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| ee428077-0156-3cff-9972-3f96b0472a35 | -3.24569 | -45.97317 | 2025-10-17 04:49:00 | NPP-375D | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 13.4 |
| 429d9489-a760-3e54-ba3b-03a22a301480 | -5.84637 | -43.87827 | 2025-10-17 04:49:00 | NPP-375D | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| b276a5e0-6212-3291-b95d-d6ddc19433a1 | -5.64473 | -46.58352 | 2025-10-17 04:49:00 | NPP-375D | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 4c83323f-defd-3304-a2e1-6a6599e38dc4 | -5.86537 | -43.91121 | 2025-10-17 04:49:00 | NPP-375D | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 480587f8-eebd-34f3-8a13-25ff3c4d3d50 | -5.14193 | -46.28835 | 2025-10-17 04:49:00 | NPP-375D | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Amazônia | 2.3 |
| ae480f8e-af2e-3a3e-b73d-1352838a0ff2 | -2.64775 | -48.38512 | 2025-10-17 04:49:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 2dadb9c0-d54e-3b68-954b-979df8e5347b | -6.37232 | -41.47566 | 2025-10-17 04:49:00 | NPP-375D | LAGOA DO SÍTIO | PIAUÍ | Brasil | 2205599 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 9dfde8bd-5cfe-3035-a4f6-b003c3111fc3 | -2.73242 | -49.38275 | 2025-10-17 04:49:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |


[Clique aqui para ver as próximas entradas](README82.md)
