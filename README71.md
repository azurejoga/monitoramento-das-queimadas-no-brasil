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

## Dados Diários - Página 71

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| f518a260-91a3-3e46-bc3e-6887d8bd280d | -3.26822 | -54.00596 | 2026-10-07 05:04:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| f59699e4-1a84-336b-9944-85a05d971e0c | -1.37989 | -52.66812 | 2026-10-07 05:04:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| b1256436-9a13-3ea1-a6e7-5ca75087c2c7 | -4.06028 | -54.31539 | 2026-10-07 05:04:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| f842b97e-b84b-35d9-b5d1-a212b7a3c2a1 | -2.4172 | -46.03584 | 2026-10-07 05:04:00 | NOAA-21 | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 46b8a2e5-38ab-3aab-8cfb-d557bdfaeaa7 | 1.03414 | -59.45236 | 2026-10-07 05:04:00 | NOAA-21 | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 2.0 |
| fed84967-efa8-3b82-9275-b7c555b33c60 | -3.52666 | -54.64063 | 2026-10-07 05:04:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| ccbea3f3-922a-3bcb-8e78-823f283aa73a | -3.29783 | -54.03586 | 2026-10-07 05:04:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 7.6 |
| 0923b5e6-1b95-3507-9f44-a2bb4bc5a87b | -4.52521 | -54.98056 | 2026-10-07 05:04:00 | NOAA-21 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 57b030af-e1c0-3cb1-9aa0-623d20736810 | -2.52999 | -58.09724 | 2026-10-07 05:04:00 | NOAA-21 | SÃO SEBASTIÃO DO UATUMÃ | AMAZONAS | Brasil | 1303957 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 8d29adbb-93ad-38ea-881e-01676ab0b1bd | -2.88133 | -54.13038 | 2026-10-07 05:04:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 1848ed11-c615-386c-b925-04de60ecca11 | -1.4594 | -54.78585 | 2026-10-07 05:04:00 | NOAA-21 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| c19f63cd-7415-3159-b052-ca5d72f45f4f | -5.68032 | -53.49302 | 2026-10-07 05:04:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 8cbaf6a9-51c0-359b-aadc-ff1bd79c1386 | -3.68413 | -45.8411 | 2026-10-07 05:04:00 | NOAA-21 | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 44892149-b830-34de-9c51-858b5f49df91 | -3.04829 | -53.93201 | 2026-10-07 05:04:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| afdc762c-3149-35e9-8c73-1fb3d61f8163 | -3.10622 | -54.17197 | 2026-10-07 05:04:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| cbe0118d-40b1-3cef-a937-0e16f2484c9b | -3.05269 | -54.14577 | 2026-10-07 05:04:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| f5ee0b16-d3ce-3da0-9c77-f2a7793380c3 | -2.54366 | -56.42321 | 2026-10-07 05:04:00 | NOAA-21 | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| deb5d7d4-4a80-31e1-a593-acb8968cfa27 | -3.12774 | -53.76523 | 2026-10-07 05:04:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| b586864d-725a-35e9-a5fa-d6c5d0482d23 | -2.13241 | -56.69695 | 2026-10-07 05:04:00 | NOAA-21 | FARO | PARÁ | Brasil | 1503002 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 78af55ee-b03d-3eb0-a09d-e587cb99cf13 | -3.01208 | -54.12155 | 2026-10-07 05:04:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| deba1f4b-187b-301e-a213-83ef3381912f | -5.99575 | -53.51549 | 2026-10-07 05:04:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| ee0f3e84-2418-3828-88cf-14a635e2ad7d | -3.10167 | -53.74306 | 2026-10-07 05:04:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 09b89b44-90f5-3f05-9af2-1dd6f0170081 | -1.26086 | -49.05769 | 2026-10-07 05:04:00 | NOAA-21 | PONTA DE PEDRAS | PARÁ | Brasil | 1505700 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| c1853e14-d388-39d8-9cab-794239070ee0 | -2.10775 | -52.06031 | 2026-10-07 05:04:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 973d340a-906d-3bfb-be59-eba38e763932 | -2.60644 | -48.26155 | 2026-10-07 05:04:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| c1586c7f-1339-3d30-bec1-66088eddda07 | -4.16172 | -55.15287 | 2026-10-07 05:04:00 | NOAA-21 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| ef5c352e-91b9-3f9f-a475-303e3e63769c | -3.61036 | -55.30516 | 2026-10-07 05:04:00 | NOAA-21 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 03c53eb5-2e74-34bb-a2e7-d287a896766b | -2.70994 | -56.88267 | 2026-10-07 05:04:00 | NOAA-21 | PARINTINS | AMAZONAS | Brasil | 1303403 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 6e26be95-21d6-35c8-8fd9-db3c53d56d96 | -3.10379 | -54.27555 | 2026-10-07 05:04:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 76eef4c8-70b6-37f1-9f93-6f87d6eff203 | -1.32388 | -56.40931 | 2026-10-07 05:04:00 | NOAA-21 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| af03e28b-f2dc-3d1b-914f-3bac53ff48b2 | -3.02246 | -53.87711 | 2026-10-07 05:04:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 454a8a30-583a-3f31-979f-0875e7f82ef7 | -3.65107 | -54.05735 | 2026-10-07 05:04:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 94c745a3-ffee-3743-bb9f-489b6665cca4 | -5.9969 | -53.50779 | 2026-10-07 05:04:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| b667bb0a-eb48-3427-b522-0d32ea59208c | -6.15005 | -51.75312 | 2026-10-07 05:04:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 3d0892aa-8bdd-301e-a6c7-2b32a0dc288e | -3.08771 | -54.26948 | 2026-10-07 05:04:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 4e97a323-7626-3a3a-9c97-a30c194ac77b | -8.69425 | -45.21762 | 2026-10-07 05:04:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 183bab7d-31fc-36a1-9bd8-959c863ae0f8 | -3.27758 | -50.40968 | 2026-10-07 05:04:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 0d07166b-6f36-31c4-a58c-51dc2d2bd400 | -4.96953 | -50.90159 | 2026-10-07 05:04:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| ddf2164a-f1b2-328f-9743-0abe0b1abfa2 | -6.89465 | -43.68102 | 2026-10-07 05:04:00 | NOAA-21 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 70b97b33-4083-32e3-964e-fe4cd38783eb | -3.58049 | -54.31735 | 2026-10-07 05:04:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 029f2fd1-849e-388e-b994-f43a9e645c31 | -1.14581 | -54.21992 | 2026-10-07 05:04:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 20081e12-7c8d-3d5a-a26e-831d82995b7d | -3.3639 | -43.39251 | 2026-10-07 05:04:00 | NOAA-21 | URBANO SANTOS | MARANHÃO | Brasil | 2112605 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 7568a38e-89bf-3e09-ba2a-7c0c591457d0 | -3.74807 | -59.28946 | 2026-10-07 05:04:00 | NOAA-21 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 41e59bb3-9b10-3015-abc5-7c7776ad32b4 | -3.50795 | -54.65192 | 2026-10-07 05:04:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 5236c999-76c8-300f-bf4a-ac92e25f0964 | -1.25782 | -49.04914 | 2026-10-07 05:04:00 | NOAA-21 | PONTA DE PEDRAS | PARÁ | Brasil | 1505700 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| bec9b6d7-09f0-349d-8366-6100bdc6baa3 | -3.05589 | -54.21088 | 2026-10-07 05:04:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| c9c32ccc-8f1e-3fab-aeba-83f18e9e757a | -1.50572 | -54.83501 | 2026-10-07 05:04:00 | NOAA-21 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| d5871178-611c-3d01-8d1a-085ef81225f3 | -2.98324 | -54.13147 | 2026-10-07 05:04:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 11815087-b2d4-3d6c-8e60-7c7d5a7bd65b | -3.51242 | -54.66678 | 2026-10-07 05:04:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 2e7c289a-8506-3c51-8b88-d7f915d7d75a | -3.28059 | -54.05857 | 2026-10-07 05:04:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 541eb3c9-ca60-392c-86fd-60a584893d38 | -2.87405 | -54.1113 | 2026-10-07 05:04:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| dbfc3ac6-2989-3de8-9f4e-a8bdd6f8eaa5 | -4.12898 | -54.42024 | 2026-10-07 05:04:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 4254c3b7-0d8d-32c2-a0ac-1832593a3f7f | -4.09849 | -52.07247 | 2026-10-07 05:04:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 2838bacb-c38c-3dee-b856-268c13077d44 | -4.76953 | -50.81525 | 2026-10-07 05:04:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 5d51c77b-2c2c-396c-80c2-1f3bf1898e69 | -3.12437 | -53.76471 | 2026-10-07 05:04:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 3bb6ccb3-14fc-3897-aa54-9e3f055de22b | -3.26996 | -54.03885 | 2026-10-07 05:04:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 38.8 |
| e2ded039-bed6-3401-bad5-1477f9c4b5f0 | -2.71529 | -57.47404 | 2026-10-07 05:04:00 | NOAA-21 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| eda4e8ea-f8eb-3566-a29f-198fcc06949a | -3.62695 | -58.93974 | 2026-10-07 05:04:00 | NOAA-21 | NOVA OLINDA DO NORTE | AMAZONAS | Brasil | 1303106 | 13 | 33 | nan | nan | nan | Amazônia | 3.4 |
| ca85c0e8-88ae-3b13-9964-b7a601800407 | -2.9664 | -54.08572 | 2026-10-07 05:04:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 6fdcaf59-2a10-3511-85e0-e39c285b0e4c | -3.54217 | -50.09505 | 2026-10-07 05:04:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 5.6 |
| e15553a0-a615-37db-b9cb-f9d57e37ebad | -5.95927 | -55.3424 | 2026-10-07 05:04:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| d58b4c77-112f-3ba8-8faf-c5165a3d125d | -3.28021 | -53.86215 | 2026-10-07 05:04:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| b02daf4f-6b86-39b9-ae09-9bd89b0ffb14 | -3.04494 | -53.93149 | 2026-10-07 05:04:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 62020ede-74c0-3c89-b354-c1fd062e6fc7 | -3.08214 | -54.26147 | 2026-10-07 05:04:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 128720b4-fd52-365b-b858-12b37442325c | -2.80228 | -54.09259 | 2026-10-07 05:04:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| f0cfd865-be3c-3e0f-8ca0-3a4641378d61 | -3.51396 | -54.63512 | 2026-10-07 05:04:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 6493554c-8aa0-3031-8e6d-e5fbef88765b | -3.18389 | -50.5478 | 2026-10-07 05:04:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 7.3 |
| 63cade5d-a752-3609-9ca5-02b775027982 | -2.93797 | -54.13909 | 2026-10-07 05:04:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 0b6f5137-2e7c-3fd5-b4dc-76f086b6d5ca | -2.97703 | -54.10535 | 2026-10-07 05:04:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 1998534e-b742-33a3-a118-a85b5f3c8c75 | -3.5618 | -59.48266 | 2026-10-07 05:04:00 | NOAA-21 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 6.0 |
| c4545468-c1e9-3106-808d-bfe7f7b66446 | -2.99371 | -54.10792 | 2026-10-07 05:04:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 867c1af6-9efc-39f0-be40-561bd793030b | -3.28508 | -54.0737 | 2026-10-07 05:04:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 5.6 |
| 68afd57f-c31d-3579-b0b2-612bd4bd00d9 | -3.13397 | -54.36586 | 2026-10-07 05:04:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 83d399d7-1a56-37e9-89a9-ab8161c1efea | -5.22616 | -48.39695 | 2026-10-07 05:04:00 | NOAA-21 | SÃO SEBASTIÃO DO TOCANTINS | TOCANTINS | Brasil | 1720309 | 17 | 33 | nan | nan | nan | Amazônia | 2.3 |
| af31183d-da30-3c3e-8644-cd3668d95add | -1.46377 | -54.77953 | 2026-10-07 05:04:00 | NOAA-21 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 72e02df7-61ea-33ba-84a2-ce8aa6674aeb | -4.13967 | -50.44376 | 2026-10-07 05:04:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| d7a01c9c-2f26-33ab-82a2-fc6cd1e80a7e | -4.24176 | -49.97591 | 2026-10-07 05:04:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| bd63229b-393e-3a8a-8a9f-08a5fe21840b | -2.88188 | -54.12688 | 2026-10-07 05:04:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| cdb621bf-eb17-3098-83a3-9f1fe9382ab9 | -3.73897 | -55.98404 | 2026-10-07 05:04:00 | NOAA-21 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 2ad8da5c-185d-3cff-8192-94e1f3bc63bb | -3.50613 | -51.68269 | 2026-10-07 05:04:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 84524c0c-1908-39fa-b01d-01f8601a2be8 | -6.15659 | -51.73484 | 2026-10-07 05:04:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 2fff9a20-04f0-3e92-beef-ba9774bd1f25 | -4.76478 | -55.66988 | 2026-10-07 05:04:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| bf9534c9-9d45-3b05-8339-5ca2033adcd9 | -4.09496 | -54.61881 | 2026-10-07 05:04:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| b107f45b-f382-3c9c-8b18-ac0afc0e42e8 | -3.0754 | -54.23897 | 2026-10-07 05:04:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| aa01911a-d0bb-38e1-8f85-5973531dbd7b | -3.53266 | -54.64851 | 2026-10-07 05:04:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| ef93455c-e339-3085-9a5c-262fb2717758 | -3.08763 | -54.24801 | 2026-10-07 05:04:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 23f1f810-d4a4-33c7-95dc-7c03104513a5 | -3.66851 | -60.62409 | 2026-10-07 05:04:00 | NOAA-21 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| b96addf7-13d4-3192-b26a-43ca7cd89b8d | -4.84787 | -42.86843 | 2026-10-07 05:04:00 | NOAA-21 | UNIÃO | PIAUÍ | Brasil | 2211100 | 22 | 33 | nan | nan | nan | Cerrado | 3.7 |
| febdcb94-d8d0-31f3-ad26-5923d8c128b9 | -3.36258 | -59.41752 | 2026-10-07 05:04:00 | NOAA-21 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 3d2863c1-98c2-3681-b8c3-576e058a8044 | -2.7931 | -57.67039 | 2026-10-07 05:04:00 | NOAA-21 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| a4ad6f88-be94-30ca-8316-12a064b51591 | -2.4795 | -56.09543 | 2026-10-07 05:04:00 | NOAA-21 | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 79422e6a-8d61-3d86-a7de-f569292da082 | -1.62724 | -55.12733 | 2026-10-07 05:04:00 | NOAA-21 | CURUÁ | PARÁ | Brasil | 1502855 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| d1119040-9fc8-3fb1-b154-56f66c8e844b | -5.72638 | -45.16689 | 2026-10-07 05:04:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 11.5 |
| ba3e2c34-b191-3494-bfe3-b0589730a9b5 | -3.23942 | -53.88145 | 2026-10-07 05:04:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 5e2aacfe-46e9-3399-908c-e0c41276594d | -1.08715 | -54.11549 | 2026-10-07 05:04:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| f85310c3-b542-3465-b831-999f82638502 | -3.54051 | -59.49367 | 2026-10-07 05:04:00 | NOAA-21 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 2.3 |
| d196a6fd-591f-3ad8-afeb-17b507fb58b0 | -3.42994 | -52.77501 | 2026-10-07 05:04:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 5dc974d9-b048-33af-97e6-772effeb5b74 | -3.11064 | -54.16544 | 2026-10-07 05:04:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 15.1 |
| b713bc70-5453-37f5-9aa8-aade1579913a | -2.56097 | -54.59597 | 2026-10-07 05:04:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 52d4f5a2-abbd-33cd-9798-a51285906b52 | -3.51835 | -54.6287 | 2026-10-07 05:04:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |


[Clique aqui para ver as próximas entradas](README72.md)
