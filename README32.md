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

## Dados Diários - Página 32

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 2cf97f8a-e2f8-3a08-982d-d44c0ed3f6a8 | -9.95162 | -58.11698 | 2024-10-10 01:54:00 | TERRA_M-M | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 6.4 |
| 1e57bb44-6110-380a-afa9-c7549f0c8a74 | -9.93436 | -56.73609 | 2024-10-10 01:54:00 | TERRA_M-M | PARANAÍTA | MATO GROSSO | Brasil | 5106299 | 51 | 33 | nan | nan | nan | Amazônia | 12.8 |
| 2d913761-02cd-3429-b892-3a46e020c735 | -9.91971 | -58.12196 | 2024-10-10 01:54:00 | TERRA_M-M | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 15.1 |
| 7071818a-0a98-3add-beb6-bced3bfc9e12 | -9.90908 | -58.12361 | 2024-10-10 01:54:00 | TERRA_M-M | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 23.3 |
| a5902eb1-4919-3208-9a04-049a0bba4766 | -9.90513 | -58.13009 | 2024-10-10 01:54:00 | TERRA_M-M | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 13.9 |
| c13e077d-d3f3-3e06-8d61-f9ce6b5d3d64 | -9.89846 | -58.1254 | 2024-10-10 01:54:00 | TERRA_M-M | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 28.2 |
| d81d5c2f-d6b9-3a6b-9d8d-af0db34a6965 | -9.8945 | -58.13184 | 2024-10-10 01:54:00 | TERRA_M-M | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 20.4 |
| 853fc595-e8ac-3350-9954-43a77e11b0f5 | -9.89252 | -58.11861 | 2024-10-10 01:54:00 | TERRA_M-M | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 12.9 |
| 3bf1202a-c495-3a1d-985d-4820bdc3aeac | -9.72996 | -57.87258 | 2024-10-10 01:54:00 | TERRA_M-M | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 12.8 |
| 5edc1dc2-8346-32ee-ad11-54c442088697 | -9.72782 | -57.8586 | 2024-10-10 01:54:00 | TERRA_M-M | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 13.6 |
| f5991588-202d-332e-bc41-2527b59f0516 | -9.65594 | -56.95231 | 2024-10-10 01:54:00 | TERRA_M-M | NOVA MONTE VERDE | MATO GROSSO | Brasil | 5108956 | 51 | 33 | nan | nan | nan | Amazônia | 10.6 |
| d31cf668-927f-3bed-9741-c3e2676612fa | -10.33152 | -57.51548 | 2024-10-10 01:54:00 | TERRA_M-M | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 7.4 |
| 39172b32-6d3b-348a-9f21-6756a730cee3 | -10.32929 | -57.501 | 2024-10-10 01:54:00 | TERRA_M-M | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 10.8 |
| 830478f1-8200-3f99-86f3-ad7eb0c35bc6 | -10.27945 | -57.70475 | 2024-10-10 01:54:00 | TERRA_M-M | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 26.7 |
| d9ae5cd9-31b3-3082-91ae-e6870a2c69a3 | -10.26347 | -57.96035 | 2024-10-10 01:54:00 | TERRA_M-M | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 8.9 |
| 28a7b25c-1284-3002-a21d-d18711c83cad | -10.22935 | -57.81271 | 2024-10-10 01:54:00 | TERRA_M-M | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 9.3 |
| 8f6c3fff-9888-39ae-957f-5fd65488c751 | -10.22699 | -57.81898 | 2024-10-10 01:54:00 | TERRA_M-M | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 8.2 |
| ed0fb7f7-3f52-374d-8e00-f9a8ffc91508 | -10.10968 | -58.22717 | 2024-10-10 01:54:00 | TERRA_M-M | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 6.4 |
| 71ef984d-32b4-3344-8948-88a70325505d | -11.04725 | -57.22857 | 2024-10-10 01:54:00 | TERRA_M-M | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 12.3 |
| a9eaea44-c44c-3e47-93a2-b211f6330d66 | -11.04684 | -57.22292 | 2024-10-10 01:54:00 | TERRA_M-M | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 14.9 |
| 7a8696aa-6493-3a03-9ca0-636274a00db1 | -11.04498 | -57.21374 | 2024-10-10 01:54:00 | TERRA_M-M | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 18.7 |
| 61f66e8a-a8ec-35b8-b416-7aaba66c65be | -11.04444 | -57.20802 | 2024-10-10 01:54:00 | TERRA_M-M | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 10.7 |
| 7464d609-2755-36c5-b577-462f0f09f374 | -11.0361 | -57.23047 | 2024-10-10 01:54:00 | TERRA_M-M | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 84.6 |
| ab7faf46-b097-3a67-a501-7f6dc9841ba6 | -11.0338 | -57.21555 | 2024-10-10 01:54:00 | TERRA_M-M | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 427.5 |
| d1b0df0d-a609-3ae3-8ead-1d1e59650f2f | -11.03147 | -57.20047 | 2024-10-10 01:54:00 | TERRA_M-M | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 102.7 |
| 1e7fc50a-c9af-3013-84c1-e05dfc025cce | -11.02723 | -57.24706 | 2024-10-10 01:54:00 | TERRA_M-M | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 18.4 |
| 19092602-fe9f-37b7-b376-3dfd3aebd422 | -11.02493 | -57.2322 | 2024-10-10 01:54:00 | TERRA_M-M | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 41.5 |
| 0d95c2c2-2e3b-3d7c-b831-4c51843c9fd0 | -11.02262 | -57.21732 | 2024-10-10 01:54:00 | TERRA_M-M | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 17.9 |
| 127d0f17-fa53-3d34-921f-b85593edb215 | -8.12123 | -58.04981 | 2024-10-10 01:54:00 | TERRA_M-M | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 14.5 |
| 48d35f27-01c0-3430-bd1d-b48ef34e6029 | -8.1191 | -58.03561 | 2024-10-10 01:54:00 | TERRA_M-M | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 18.8 |
| c568fcbd-3f83-37fc-9d86-51833141ba37 | -8.11018 | -58.05141 | 2024-10-10 01:54:00 | TERRA_M-M | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 17.5 |
| 2972909a-98b4-37d0-9b7e-7797dfe92e0b | -8.10805 | -58.03729 | 2024-10-10 01:54:00 | TERRA_M-M | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 28.7 |
| 6684d5b8-e8c4-3bba-9da2-eefdbdec4994 | -9.54639 | -58.9598 | 2024-10-10 01:54:00 | TERRA_M-M | COTRIGUAÇU | MATO GROSSO | Brasil | 5103379 | 51 | 33 | nan | nan | nan | Amazônia | 6.1 |
| 32bc484f-4b4a-3f8e-86cb-f2e78b134a4c | -9.44183 | -58.94511 | 2024-10-10 01:54:00 | TERRA_M-M | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 5.4 |
| 99b1b4a1-dfe3-3026-870f-ff2f923e0c08 | -10.70202 | -58.54495 | 2024-10-10 01:54:00 | TERRA_M-M | CASTANHEIRA | MATO GROSSO | Brasil | 5102850 | 51 | 33 | nan | nan | nan | Amazônia | 6.3 |
| a792fcf5-8e84-3e2a-aeca-57296a1ddb25 | -10.57127 | -59.49945 | 2024-10-10 01:54:00 | TERRA_M-M | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 6.4 |
| 180498f0-ac5e-3f7e-8ae9-be25077275d4 | -10.40368 | -59.14699 | 2024-10-10 01:54:00 | TERRA_M-M | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 16.3 |
| 0f1c2313-1985-3ea3-864a-f165abadbf68 | -10.39384 | -59.14843 | 2024-10-10 01:54:00 | TERRA_M-M | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 4.5 |
| c2f5a021-eeb3-33ac-a595-a717127897e8 | -10.06634 | -59.35975 | 2024-10-10 01:54:00 | TERRA_M-M | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 46fd29a9-2ba4-3feb-9d46-f81ba1be5bb7 | -10.05659 | -59.36124 | 2024-10-10 01:54:00 | TERRA_M-M | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 5.3 |
| fb0f62d1-90cd-353d-b6bf-168fa02c2bab | -12.32414 | -59.174 | 2024-10-10 01:54:00 | TERRA_M-M | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 10.9 |
| 80cda0cc-af3f-3390-b0dc-04e4cc789a5c | -12.32255 | -59.16333 | 2024-10-10 01:54:00 | TERRA_M-M | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 9.4 |
| b0c66406-519e-3812-856f-7253f278023b | -12.31457 | -59.17543 | 2024-10-10 01:54:00 | TERRA_M-M | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 8.4 |
| bda60cbc-532b-3bb0-ae31-ae4b07d25ec8 | -12.31297 | -59.16475 | 2024-10-10 01:54:00 | TERRA_M-M | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 4.9 |
| b924b202-7a5f-3840-8562-b37b26884169 | -12.305 | -59.17687 | 2024-10-10 01:54:00 | TERRA_M-M | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 25.3 |
| 2b39a4be-afbe-3901-af5e-ce9895d9e8d2 | -12.3034 | -59.16619 | 2024-10-10 01:54:00 | TERRA_M-M | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 784dc88d-2be2-350c-9bd6-76230f39b865 | -11.88178 | -59.01482 | 2024-10-10 01:54:00 | TERRA_M-M | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 689182d6-19e0-3c06-bb45-56027f66470a | -11.87831 | -59.00997 | 2024-10-10 01:54:00 | TERRA_M-M | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 6.7 |
| 937aed1f-8c5d-3e31-95a7-af14f63c3c4f | -11.8145 | -58.84952 | 2024-10-10 01:54:00 | TERRA_M-M | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 33.8 |
| ab0a3051-4329-39f8-a4d8-40a7255ec039 | -11.81281 | -58.83828 | 2024-10-10 01:54:00 | TERRA_M-M | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 13.2 |
| fdb5a799-e236-3246-a044-52aede3481bf | -11.66722 | -58.89635 | 2024-10-10 01:54:00 | TERRA_M-M | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 21.3 |
| f676abc0-37a2-3546-be4c-70fb2e01edf8 | -11.12413 | -59.09933 | 2024-10-10 01:54:00 | TERRA_M-M | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Amazônia | 9.3 |
| ade6a5db-ed79-3786-8d7f-d4a09c2c1069 | -9.21646 | -59.78413 | 2024-10-10 01:54:00 | TERRA_M-M | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 9.6 |
| 31d8c469-4056-32ef-bde0-00bd418a7c73 | -9.25851 | -60.27351 | 2024-10-10 01:54:00 | TERRA_M-M | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 5.1 |
| c17827d0-8a15-30dc-adb7-1ea2ead39dd4 | -9.24251 | -60.48898 | 2024-10-10 01:54:00 | TERRA_M-M | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 3659921b-6cdc-3f36-9266-ba0f797ebfc3 | -9.24106 | -60.47914 | 2024-10-10 01:54:00 | TERRA_M-M | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 12.2 |
| b0e153ce-b922-351d-ae8e-4bb1ca9404a3 | -9.23816 | -60.45946 | 2024-10-10 01:54:00 | TERRA_M-M | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 21de1d0b-d181-34bc-928e-608cfd834ea2 | -9.18721 | -60.3521 | 2024-10-10 01:54:00 | TERRA_M-M | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 5.9 |
| c0614204-90fa-3f76-bb0a-1b98f7ed4000 | -9.05222 | -60.44949 | 2024-10-10 01:54:00 | TERRA_M-M | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 61857d92-cd69-3108-a9b4-5e07ccd76e57 | -9.04638 | -60.45675 | 2024-10-10 01:54:00 | TERRA_M-M | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 6.9 |
| 138c2940-e252-3be9-b401-16a2268688f5 | -8.74618 | -60.48959 | 2024-10-10 01:54:00 | TERRA_M-M | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 3.8 |
| ae47116d-abf3-34f6-80d3-b46588bcd8d8 | -8.74475 | -60.47967 | 2024-10-10 01:54:00 | TERRA_M-M | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 04ddad1e-1d61-3a7f-b241-fedd3bedb611 | -9.85953 | -59.83694 | 2024-10-10 01:54:00 | TERRA_M-M | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 91b2846b-e7d7-3b02-b963-2d5fb4945898 | -10.46096 | -60.10413 | 2024-10-10 01:54:00 | TERRA_M-M | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 8.2 |
| 97933261-6a61-3a80-aea2-085e6fef5fe7 | -10.43357 | -61.00434 | 2024-10-10 01:54:00 | TERRA_M-M | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 5.3 |
| f6002106-4312-3fcd-aef3-6e8952e30ee6 | -10.43224 | -60.99512 | 2024-10-10 01:54:00 | TERRA_M-M | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 24.0 |
| fa176310-1ea3-34a6-93a7-06e9a58f80bc | -10.43091 | -60.98583 | 2024-10-10 01:54:00 | TERRA_M-M | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 5.7 |
| 740be4e9-bedd-36df-9268-dad599c92ca6 | -10.42459 | -61.0057 | 2024-10-10 01:54:00 | TERRA_M-M | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 16.4 |
| bde7f813-e1a5-327c-927f-8818ec3434a8 | -10.42326 | -60.99647 | 2024-10-10 01:54:00 | TERRA_M-M | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 22.2 |
| d767a385-4b84-350c-8a60-29e21909fc30 | -10.42191 | -60.98714 | 2024-10-10 01:54:00 | TERRA_M-M | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 6.6 |
| 3ee8aeac-72b5-3013-938e-1ba3848e6905 | -10.37583 | -61.24483 | 2024-10-10 01:54:00 | TERRA_M-M | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 9.4 |
| fd72ce86-6e21-3b3e-8675-ae8bbcdc7dc6 | -10.36951 | -61.26435 | 2024-10-10 01:54:00 | TERRA_M-M | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 11.6 |
| ee771f36-dfbd-3bc3-9ae5-367d30f981f4 | -10.3682 | -61.25521 | 2024-10-10 01:54:00 | TERRA_M-M | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 33.3 |
| e198ce9c-5a99-3331-a5c8-64d381f0ad29 | -10.36688 | -61.24605 | 2024-10-10 01:54:00 | TERRA_M-M | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 20.0 |
| 26f87266-a4f5-3cbc-be77-476b377ccdb2 | -10.36557 | -61.23688 | 2024-10-10 01:54:00 | TERRA_M-M | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 16.8 |
| 0074c306-2b50-34ab-b79b-8bdb38261c1c | -10.17866 | -60.8997 | 2024-10-10 01:54:00 | TERRA_M-M | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 9.6 |
| 5ce0c3a3-2fb5-345f-9a5d-bcde8920cf76 | -9.94962 | -60.15047 | 2024-10-10 01:54:00 | TERRA_M-M | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 8.0 |
| 623b9f30-a0a1-37b5-89e6-fee47d13c30a | -9.94815 | -60.14047 | 2024-10-10 01:54:00 | TERRA_M-M | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 6.6 |
| c8a4a76c-6eca-304e-b9c8-b409827e6a9d | -9.88422 | -60.26888 | 2024-10-10 01:54:00 | TERRA_M-M | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 6a2eed0a-1eb9-32be-9699-2d41621c0b74 | -9.86364 | -60.32245 | 2024-10-10 01:54:00 | TERRA_M-M | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 28.8 |
| 62ec97e9-52fc-35ee-8260-f5ae1f4dcdf2 | -9.86219 | -60.31258 | 2024-10-10 01:54:00 | TERRA_M-M | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 13.4 |
| fa3c9e2f-74d5-39e6-b4b3-1a0f90851536 | -9.85627 | -60.31932 | 2024-10-10 01:54:00 | TERRA_M-M | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 6.0 |
| ebe8b2f5-aa42-3eaa-9607-02ae25f4061d | -9.85426 | -60.6962 | 2024-10-10 01:54:00 | TERRA_M-M | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 5.8 |
| 0977b893-06ad-359d-8c1a-c55d62716a8a | -9.85343 | -60.75472 | 2024-10-10 01:54:00 | TERRA_M-M | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 4.9 |
| ae3df105-d1ed-3744-ae49-69752f9f0bf2 | -9.85205 | -60.74522 | 2024-10-10 01:54:00 | TERRA_M-M | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 6.6 |
| 9613c299-5185-3a15-861d-b613cb3fe9a1 | -9.8072 | -60.43715 | 2024-10-10 01:54:00 | TERRA_M-M | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 27945efb-172f-3c86-925b-42b70278e585 | -9.71472 | -60.74892 | 2024-10-10 01:54:00 | TERRA_M-M | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 4.3 |
| f1b659a9-383b-3369-84d7-076d14f8393f | -9.38942 | -61.05318 | 2024-10-10 01:54:00 | TERRA_M-M | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 11.7 |
| 70dfcd0a-367e-3061-a137-099668ebd0fc | -9.38809 | -61.04383 | 2024-10-10 01:54:00 | TERRA_M-M | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 7.1 |
| 7346a3f4-02b9-3f37-945e-d5e648f9b472 | -11.5402 | -60.30539 | 2024-10-10 01:54:00 | TERRA_M-M | VILHENA | RONDÔNIA | Brasil | 1100304 | 11 | 33 | nan | nan | nan | Amazônia | 4.9 |
| bd07f41a-c6eb-36ce-9c85-4e97d8534dd1 | -11.53881 | -60.29583 | 2024-10-10 01:54:00 | TERRA_M-M | VILHENA | RONDÔNIA | Brasil | 1100304 | 11 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 02f10d97-ac8f-3eaa-8977-e1485565310a | -11.42364 | -60.45251 | 2024-10-10 01:54:00 | TERRA_M-M | ESPIGÃO D'OESTE | RONDÔNIA | Brasil | 1100098 | 11 | 33 | nan | nan | nan | Amazônia | 8.0 |
| 729e554a-6185-3bd9-83a6-598462d9af66 | -11.41456 | -60.45388 | 2024-10-10 01:54:00 | TERRA_M-M | ESPIGÃO D'OESTE | RONDÔNIA | Brasil | 1100098 | 11 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 1b96992f-485b-37b6-9aa7-c6abd7518bc3 | -11.39996 | -60.41716 | 2024-10-10 01:54:00 | TERRA_M-M | VILHENA | RONDÔNIA | Brasil | 1100304 | 11 | 33 | nan | nan | nan | Amazônia | 10.1 |
| 37aa34bb-c980-33d2-bf86-af9bc6efe28f | -11.39859 | -60.4077 | 2024-10-10 01:54:00 | TERRA_M-M | VILHENA | RONDÔNIA | Brasil | 1100304 | 11 | 33 | nan | nan | nan | Amazônia | 29.0 |
| 50f33e07-f0f8-35c9-bfe9-1df9f6e0acd2 | -11.39087 | -60.41857 | 2024-10-10 01:54:00 | TERRA_M-M | VILHENA | RONDÔNIA | Brasil | 1100304 | 11 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 1d1ee021-1ed0-3b0b-8c67-92238452e845 | -11.38949 | -60.40907 | 2024-10-10 01:54:00 | TERRA_M-M | VILHENA | RONDÔNIA | Brasil | 1100304 | 11 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 7ebdc624-d343-39be-94ec-ef5776e88301 | -11.34793 | -60.56679 | 2024-10-10 01:54:00 | TERRA_M-M | ESPIGÃO D'OESTE | RONDÔNIA | Brasil | 1100098 | 11 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 070ab270-2942-36c0-9056-bf066b7eea8a | -11.28629 | -60.33295 | 2024-10-10 01:54:00 | TERRA_M-M | VILHENA | RONDÔNIA | Brasil | 1100304 | 11 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 58b8fa7f-dc56-33c0-9760-c2bfc491a190 | -11.27213 | -60.49129 | 2024-10-10 01:54:00 | TERRA_M-M | VILHENA | RONDÔNIA | Brasil | 1100304 | 11 | 33 | nan | nan | nan | Amazônia | 13.2 |


[Clique aqui para ver as próximas entradas](README33.md)
