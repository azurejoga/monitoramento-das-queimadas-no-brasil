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

## Dados Diários - Página 54

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 0ddfe93c-8789-3186-bd56-cca19d4da31b | -10.6334 | -49.91362 | 2024-09-28 04:21:00 | NOAA-21 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 7e72e1da-af9b-3a73-aa0e-728d988356a6 | -10.6326 | -49.91842 | 2024-09-28 04:21:00 | NOAA-21 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| efb399cd-46f0-39b8-9a0b-eaf292921583 | -10.63186 | -49.91578 | 2024-09-28 04:21:00 | NOAA-21 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 9aed16d8-e933-3847-a5dc-6b309a2ec0ba | -10.49025 | -50.2632 | 2024-09-28 04:21:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 0b7ccd5c-5404-3a2d-a691-e028c83c9899 | -9.94662 | -50.09428 | 2024-09-28 04:21:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 8ab83cf8-1e27-3e21-96f1-c027043ce016 | -9.8989 | -50.1357 | 2024-09-28 04:21:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 4.0 |
| a690135f-c5cb-3a8d-859e-c8b6c2fcab71 | -9.89499 | -50.13503 | 2024-09-28 04:21:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 96eac6eb-8b56-387e-bb6f-30765d7e1570 | -9.77307 | -50.07036 | 2024-09-28 04:21:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| c4a3cdbc-0aa0-3eb1-9cdf-d5757570a090 | -9.75943 | -49.11624 | 2024-09-28 04:21:00 | NOAA-21 | DIVINÓPOLIS DO TOCANTINS | TOCANTINS | Brasil | 1707108 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 476f0290-a4b4-3218-8153-5d84aed5d0bb | -9.72821 | -49.18918 | 2024-09-28 04:21:00 | NOAA-21 | DIVINÓPOLIS DO TOCANTINS | TOCANTINS | Brasil | 1707108 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 51a9e57a-5023-3c54-9206-14f9094c0273 | -9.60777 | -50.09371 | 2024-09-28 04:21:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 3ac030b2-7ea0-30fb-a904-db1f4c1a71d1 | -9.57033 | -50.12384 | 2024-09-28 04:21:00 | NOAA-21 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 7.0 |
| cc920a52-fbcf-37f8-bcf4-fb41f915805a | -9.56947 | -50.12893 | 2024-09-28 04:21:00 | NOAA-21 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 10.3 |
| a3f896da-88ce-357e-b16a-ac752ba9a73d | -9.56806 | -50.06609 | 2024-09-28 04:21:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 206b4c9f-9c6c-3eff-b896-768edd86a052 | -9.56693 | -50.19157 | 2024-09-28 04:21:00 | NOAA-21 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| bf3eb2bb-a7ee-3fbf-9216-58b7d67f1f73 | -9.56606 | -50.1967 | 2024-09-28 04:21:00 | NOAA-21 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| baae2b94-7013-33cf-9a9e-ecb0e6ebc602 | -9.56553 | -50.12825 | 2024-09-28 04:21:00 | NOAA-21 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 95d28b4e-b582-3a9f-912d-0537e13ba1f3 | -9.56298 | -50.19089 | 2024-09-28 04:21:00 | NOAA-21 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| e006cbcb-b791-3a96-bc54-ba9e7742246b | -9.56211 | -50.19602 | 2024-09-28 04:21:00 | NOAA-21 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 9ab39709-09fd-363a-8f5e-55b8f788759e | -9.55816 | -50.19535 | 2024-09-28 04:21:00 | NOAA-21 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 01887a34-4f48-3a8e-bc41-89dfa5aa4ade | -9.54718 | -50.18818 | 2024-09-28 04:21:00 | NOAA-21 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 3156c828-445b-3bd0-a952-e99d96bb92f1 | -9.54454 | -50.2036 | 2024-09-28 04:21:00 | NOAA-21 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 69cc4907-7a0b-3955-9add-d20e4613dbd3 | -9.54366 | -50.20874 | 2024-09-28 04:21:00 | NOAA-21 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| f2317a35-c8e4-3898-986a-1e72095194e7 | -9.43554 | -50.06208 | 2024-09-28 04:21:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 86d44d93-609f-37d9-8ea4-a24520bc0ed4 | -9.42089 | -50.03054 | 2024-09-28 04:21:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 54dc8b7c-9f62-3fee-91e3-7e2a5d38bb80 | -9.4203 | -50.03349 | 2024-09-28 04:21:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 5.1 |
| b9498f0c-36c9-335f-ba90-96b892c57cfe | -9.42005 | -50.03559 | 2024-09-28 04:21:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 8.3 |
| 46c5c011-4321-3bc4-9fd8-e4b27a1e9676 | -9.41942 | -50.03853 | 2024-09-28 04:21:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 5.1 |
| d02c500f-925f-36c0-94a5-d49e0a7cf910 | -9.4155 | -50.03785 | 2024-09-28 04:21:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| e3fce8e4-942a-337a-bead-6d6939dfadfa | -9.41158 | -50.03717 | 2024-09-28 04:21:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| fa8c4aa1-77af-30df-93b2-1776471f0077 | -9.38732 | -50.01439 | 2024-09-28 04:21:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 11.7 |
| 5e9a64f0-d04c-3583-955a-00bb35dd9755 | -9.38647 | -50.01942 | 2024-09-28 04:21:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 12.2 |
| 299e7501-60ae-374f-a6e4-d9a31b77dc08 | -9.3834 | -50.01372 | 2024-09-28 04:21:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 26.3 |
| 2bd6b2f8-4ad7-36a1-ad79-9f0bc3896c85 | -9.38255 | -50.01876 | 2024-09-28 04:21:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 6.8 |
| cb084d21-70ce-3aec-bcaa-4abca76a2f41 | -9.3817 | -50.0238 | 2024-09-28 04:21:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 6.8 |
| f5d273ca-f414-3a5d-b8f8-958acbe2b15c | -9.37948 | -50.01306 | 2024-09-28 04:21:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 26.3 |
| 7a9ab5c2-ae4b-390d-a148-c8fb390863ec | -9.37863 | -50.01808 | 2024-09-28 04:21:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 6.8 |
| 16ad8df2-6970-33cc-a989-d3c993428c95 | -9.37778 | -50.02312 | 2024-09-28 04:21:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 6.8 |
| 0efc2534-b389-3b98-9c66-d980e3d7cc67 | -9.37556 | -50.01239 | 2024-09-28 04:21:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 3c0eb49e-09e1-392a-a71c-3890f1924383 | -9.37471 | -50.01742 | 2024-09-28 04:21:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| fb7f62be-876b-358a-af49-817b9ee6b665 | -9.37386 | -50.02245 | 2024-09-28 04:21:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 71de17ab-b3aa-39ff-8b1d-ad11a662f1b6 | -9.36381 | -50.01038 | 2024-09-28 04:21:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 0165c998-34fd-3d3e-a5ba-00971d408237 | -9.36295 | -50.01542 | 2024-09-28 04:21:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| ee311cd1-7005-3344-875d-2b7718eea3a4 | -10.19083 | -49.95635 | 2024-09-28 04:21:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 7aa904ae-a40d-36e5-9a94-b656690f26e4 | -10.18922 | -49.9534 | 2024-09-28 04:21:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 0c9a0e9e-5767-3778-9d93-70d2494d9cb7 | -10.15252 | -49.9951 | 2024-09-28 04:21:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 5cb0a72f-8ee1-3d37-ba11-5b4fa92c062e | -10.14395 | -49.99869 | 2024-09-28 04:21:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 5a275f77-c5d1-3015-b748-178366159ae7 | -10.14312 | -50.00359 | 2024-09-28 04:21:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 3.8 |
| e989fe7d-99a0-3b41-8ddd-8fb8c0c39355 | -10.11131 | -50.00319 | 2024-09-28 04:21:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 291124e2-ce2d-3a3c-b420-dacd48f18a27 | -10.11046 | -50.00811 | 2024-09-28 04:21:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| ebeb8c87-ed3d-35ee-a9af-7aaeacb0f947 | -10.10659 | -50.00745 | 2024-09-28 04:21:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 8fbcba0b-a5ad-31d0-8e69-1d0b974d5dcb | -10.09799 | -50.01104 | 2024-09-28 04:21:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 3b5394e6-e547-3f19-831d-0edbe7a516b3 | -10.09412 | -50.01038 | 2024-09-28 04:21:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 78321965-345f-354f-b8db-300a5610c049 | -10.08305 | -50.16743 | 2024-09-28 04:21:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 7979eed5-c424-36e0-a7de-86c4142b4dd3 | -11.83301 | -49.62922 | 2024-09-28 04:21:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 43263b3f-e28c-33cd-8b23-b110010c463b | -11.82931 | -49.62859 | 2024-09-28 04:21:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 4.2 |
| c287d908-b730-383f-b78f-26a6be7e4650 | -11.75723 | -49.89262 | 2024-09-28 04:21:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 69c8494c-5ae8-34dc-bb96-85ae3054dfb1 | -11.18421 | -50.21518 | 2024-09-28 04:21:00 | NOAA-21 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 644b5b83-ceed-359d-aea7-66ce617619f6 | -11.14059 | -49.72042 | 2024-09-28 04:21:00 | NOAA-21 | DUERÉ | TOCANTINS | Brasil | 1707306 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 2a115708-7ad6-3f60-bb2c-a1dd27c51378 | -11.02297 | -50.18664 | 2024-09-28 04:21:00 | NOAA-21 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 2afce56d-1e4f-3870-875d-560fa1a506cd | -11.021 | -50.18427 | 2024-09-28 04:21:00 | NOAA-21 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 544c8d3d-195f-3388-aa93-e9f65b063ab2 | -11.02014 | -50.18918 | 2024-09-28 04:21:00 | NOAA-21 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 3.7 |
| c54db3f2-3305-301f-91bd-93aa15aeb8ff | -11.01911 | -50.18596 | 2024-09-28 04:21:00 | NOAA-21 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 3dba64d3-29e8-34e2-9be5-d15bdde5f8fa | -11.01828 | -50.19088 | 2024-09-28 04:21:00 | NOAA-21 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 4f3f9a79-d439-38e4-a3d7-2e1d0b102ad9 | -11.01628 | -50.18851 | 2024-09-28 04:21:00 | NOAA-21 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| dacef8c7-aae7-3107-af54-d6cce6d393f7 | -11.01442 | -50.1902 | 2024-09-28 04:21:00 | NOAA-21 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 1557c967-d2ca-3867-8b70-1c3e84a7648d | -11.01241 | -50.18784 | 2024-09-28 04:21:00 | NOAA-21 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 21998c14-d2e0-3f31-9426-2fd883c15416 | -11.01155 | -50.19275 | 2024-09-28 04:21:00 | NOAA-21 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 01c79d01-b2cc-3aad-9148-bbc741430ba8 | -11.01056 | -50.18953 | 2024-09-28 04:21:00 | NOAA-21 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| b177cbbe-332f-3d98-bf34-32e6b92aa85e | -11.00972 | -50.19445 | 2024-09-28 04:21:00 | NOAA-21 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| ca4ce6dd-e5b9-38df-aba5-d6aab0226909 | -10.98988 | -50.17075 | 2024-09-28 04:21:00 | NOAA-21 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 18.0 |
| d5f694e6-8087-308d-b19e-aacf628736a6 | -10.98905 | -50.17566 | 2024-09-28 04:21:00 | NOAA-21 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 766323b4-253d-398c-a724-f69e3dc0272a | -10.98435 | -50.17989 | 2024-09-28 04:21:00 | NOAA-21 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 1bcca43a-721a-3bda-8315-7fde88c8a17f | -10.98351 | -50.1848 | 2024-09-28 04:21:00 | NOAA-21 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 4.1 |
| bf609059-307f-3950-9d57-82c31cd50f60 | -10.9542 | -50.12422 | 2024-09-28 04:21:00 | NOAA-21 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 8fccf041-988a-3008-b91f-1559e0de4910 | -10.94734 | -50.11801 | 2024-09-28 04:21:00 | NOAA-21 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 5c46848f-3b9d-31b5-b026-8e36c205f324 | -10.94649 | -50.12288 | 2024-09-28 04:21:00 | NOAA-21 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 0d900a32-d99c-3961-909d-136467699e45 | -10.88251 | -50.46679 | 2024-09-28 04:21:00 | NOAA-21 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 4341639c-9b68-3833-8139-864ee074abab | -10.87947 | -50.46098 | 2024-09-28 04:21:00 | NOAA-21 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 9b082d9f-7043-363c-9256-e59bdd748437 | -12.70903 | -50.96482 | 2024-09-28 04:21:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 0a46ab61-9278-37ae-aa56-95f06eb4288e | -12.70508 | -50.96411 | 2024-09-28 04:21:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 87ef0edf-e31e-3d4f-9409-5a5bb9d7299e | -12.69933 | -50.97375 | 2024-09-28 04:21:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 058683e7-4764-3b65-af97-248a90a295c7 | -12.53324 | -50.62933 | 2024-09-28 04:21:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 7.0 |
| 7d8c2984-70cd-364f-b4cf-1a748a57001a | -12.53238 | -50.63431 | 2024-09-28 04:21:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 3.7 |
| e9743d76-e92b-3e22-ad9e-1b39410540d3 | -12.53151 | -50.63929 | 2024-09-28 04:21:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 64fc849b-07e6-3316-bc40-49478f613aec | -12.52937 | -50.62864 | 2024-09-28 04:21:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 3.6 |
| de8d7d33-3804-3756-b466-aa8b524a34a3 | -12.5285 | -50.63362 | 2024-09-28 04:21:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| d3d79329-88bd-337a-8911-b9de5c7e452d | -12.52763 | -50.63861 | 2024-09-28 04:21:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| cfacae48-4b10-3b3a-8de8-67a8b7d9ad66 | -12.43896 | -50.95939 | 2024-09-28 04:21:00 | NOAA-21 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| b8e404c4-e130-3a20-8193-f9eac3f38945 | -12.435 | -50.95868 | 2024-09-28 04:21:00 | NOAA-21 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| eb2f0d56-a1ad-3ac5-acf2-eae49f7612ef | -12.29482 | -50.65472 | 2024-09-28 04:21:00 | NOAA-21 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 2.2 |
| e2b3ebcb-ed8c-3597-8654-a5f3620c8826 | -12.27887 | -50.6312 | 2024-09-28 04:21:00 | NOAA-21 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 3.9 |
| a5142aba-9dbf-38bb-895e-d0a9ef6bdba3 | -12.27799 | -50.6362 | 2024-09-28 04:21:00 | NOAA-21 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 94820a08-c6e8-321c-8117-880c14ec7ebd | -12.24543 | -50.65851 | 2024-09-28 04:21:00 | NOAA-21 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 177d76d7-e8ed-360f-bfda-e22bbcf27107 | -12.24537 | -50.66153 | 2024-09-28 04:21:00 | NOAA-21 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 09fd7fee-5fa8-3f85-b90b-f0c1f10723e4 | -12.24153 | -50.65781 | 2024-09-28 04:21:00 | NOAA-21 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 297ea9b3-21c8-39a8-b886-12b039e417d5 | -12.39796 | -50.46074 | 2024-09-28 04:21:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 4.8 |
| f6fdb377-4b82-3340-befd-9fb12f020152 | -12.3971 | -50.46563 | 2024-09-28 04:21:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 4114cf4e-9dfd-3b7d-99a1-5b09434925c3 | -12.39649 | -50.45814 | 2024-09-28 04:21:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 4.2 |
| d0807dba-e70c-33b6-b15b-1bae068863f3 | -12.39623 | -50.47052 | 2024-09-28 04:21:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |


[Clique aqui para ver as próximas entradas](README55.md)
