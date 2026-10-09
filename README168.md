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

## Dados Diários - Página 168

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 38a1935d-df83-3e1d-bb9c-f1ceed491169 | -3.30962 | -53.70084 | 2026-10-09 05:04:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 58ac9fd4-4c4d-330c-999f-70564c17943e | -4.5348 | -49.67082 | 2026-10-09 05:04:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| c5533f22-250f-3dd0-8282-2a5474a6342d | -10.3368 | -46.22881 | 2026-10-09 05:04:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| ea71bac7-cd80-350d-b3e5-f6fb5f7d124b | -11.28458 | -45.19999 | 2026-10-09 05:04:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| a93b0b96-d264-32de-a72d-285ba5267440 | -6.96392 | -45.27889 | 2026-10-09 05:04:00 | NPP-375D | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| d49b7f56-2aa5-3917-8b8e-0d965a33ae38 | -10.97984 | -45.39452 | 2026-10-09 05:04:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 09b3f3e5-8d37-3767-9fce-754b118317f6 | -3.0553 | -53.93464 | 2026-10-09 05:04:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 48e3f308-3aa6-3ee1-858e-6d3cadc626dc | -11.67474 | -46.77721 | 2026-10-09 05:04:00 | NPP-375D | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 16b676b9-679a-3e0d-b2cb-60c0d484b5fb | -9.82859 | -47.45902 | 2026-10-09 05:04:00 | NPP-375D | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 5c906c78-00dd-3f8b-8a5e-57b8e855691d | -4.13576 | -53.9928 | 2026-10-09 05:04:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 8ab8a395-fbdd-30e9-94ae-5ca58b1856a7 | -6.17549 | -52.86304 | 2026-10-09 05:04:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 58edcfe2-544c-3cf1-b99c-e98aa1fa5f60 | -3.02071 | -54.08184 | 2026-10-09 05:04:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 07f95940-ba34-3a3f-8bb1-72af8b6706a0 | -6.32213 | -54.79372 | 2026-10-09 05:04:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 320d9fc0-1889-3a7e-8bdc-404755507379 | -2.94159 | -54.05833 | 2026-10-09 05:04:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 4939c676-c911-3fba-a45f-5b07869345e9 | -8.73598 | -45.15394 | 2026-10-09 05:04:00 | NPP-375D | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 94d24962-c985-36eb-995d-42e651d6e022 | -3.20492 | -57.87023 | 2026-10-09 05:04:00 | NPP-375D | BOA VISTA DO RAMOS | AMAZONAS | Brasil | 1300680 | 13 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 2a21a519-9320-3211-9d66-8c6f9c94f1ee | -3.96996 | -51.86298 | 2026-10-09 05:04:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| e1e7a51e-7604-3d6a-ac85-4c8f80e80af8 | -3.90223 | -52.16067 | 2026-10-09 05:04:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 71834ea9-aa37-35b4-8837-c6c0fc8d27a5 | -3.05769 | -59.08841 | 2026-10-09 05:04:00 | NPP-375D | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 18bd6984-ef74-3186-90cb-1c77134a622b | -11.99625 | -43.48793 | 2026-10-09 05:04:00 | NPP-375D | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 5839c240-572e-3a47-8f21-039e2c3f7e04 | -6.14217 | -52.9006 | 2026-10-09 05:04:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 44e31ba7-b8af-38ec-a276-2c343aa74134 | -3.30116 | -54.06206 | 2026-10-09 05:04:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 6d084221-006f-334e-9bdf-8e237d34172e | -7.44023 | -63.55556 | 2026-10-09 05:04:00 | NPP-375D | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 70e43509-621c-39b6-9187-c7016a76061a | -6.48223 | -62.85876 | 2026-10-09 05:04:00 | NPP-375D | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 7e6826a9-1e6f-311b-a958-cb9bdd26fe1e | -8.7318 | -45.14781 | 2026-10-09 05:04:00 | NPP-375D | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 6.3 |
| ddd37069-5016-3bdc-97d4-3d142c62b8d1 | -9.20676 | -57.72823 | 2026-10-09 05:04:00 | NPP-375D | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 3c79a3bf-ba4e-3ee0-946e-6b2721cb5338 | -11.2511 | -46.30272 | 2026-10-09 05:04:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 42538ff2-e928-3574-9692-23ad6b8727fb | -3.00847 | -54.75431 | 2026-10-09 05:04:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 10c8f256-d338-3af1-bc94-037bd56ebabd | -3.74481 | -59.3693 | 2026-10-09 05:04:00 | NPP-375D | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 8.5 |
| b7d361b1-d2b5-3d24-98d4-4dd8e9dc1236 | -9.69456 | -58.09148 | 2026-10-09 05:04:00 | NPP-375D | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| b6e18454-ca02-3885-9b2e-3bcae7e6cf4f | -5.71472 | -53.49523 | 2026-10-09 05:04:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 15.5 |
| a570f9a0-0c79-31aa-99ac-4f528890b19d | -8.8366 | -61.46104 | 2026-10-09 05:04:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| c4d7f85b-b232-3883-809f-e0edb92fb687 | -3.55147 | -54.68681 | 2026-10-09 05:04:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 8.4 |
| a1170cdc-47f0-3b61-8c8f-683c1147b2af | -10.30926 | -46.59248 | 2026-10-09 05:04:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| fbd56f7f-1bf3-3690-8e7e-ff059ea3d6f5 | -5.85989 | -53.45998 | 2026-10-09 05:04:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 36e190e0-0b86-3d93-af1c-cb58a1841574 | -3.27653 | -53.81794 | 2026-10-09 05:04:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| d977e0be-13a8-39a6-9124-125ea6abae2d | -2.99747 | -54.06723 | 2026-10-09 05:04:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| ac21d8b6-d8fd-3039-b8c2-73ccc09f513c | -8.93257 | -48.60832 | 2026-10-09 05:04:00 | NPP-375D | GUARAÍ | TOCANTINS | Brasil | 1709302 | 17 | 33 | nan | nan | nan | Amazônia | 1.5 |
| faee3042-b3f4-3f0d-b749-7b61bc52aa72 | -11.99628 | -43.48065 | 2026-10-09 05:04:00 | NPP-375D | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 06a085d6-13bd-338a-b5ef-73a9d8852f5a | -4.29707 | -60.95278 | 2026-10-09 05:04:00 | NPP-375D | BERURI | AMAZONAS | Brasil | 1300631 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| f686c588-7140-3d00-a146-66ba68a63a3c | -2.52458 | -56.25925 | 2026-10-09 05:04:00 | NPP-375D | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| a528d79e-39aa-3223-929c-5745f33e8411 | -3.1806 | -58.84393 | 2026-10-09 05:04:00 | NPP-375D | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| bd1c82af-1b5e-3982-9a0f-59878fe55e7e | -6.01039 | -40.97841 | 2026-10-09 05:04:00 | NPP-375D | ASSUNÇÃO DO PIAUÍ | PIAUÍ | Brasil | 2201051 | 22 | 33 | nan | nan | nan | Caatinga | 13.0 |
| a4bf5284-44cf-39e7-a51a-c9809a8e6cc6 | -3.74003 | -59.3685 | 2026-10-09 05:04:00 | NPP-375D | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 8.5 |
| 9d2e5942-3c5d-34b5-afc9-6122f57a4e90 | -2.5641 | -57.41284 | 2026-10-09 05:04:00 | NPP-375D | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 5.6 |
| 030c3f8c-175d-3b6a-bbf9-76a1fe33c87d | -2.88553 | -54.16033 | 2026-10-09 05:04:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 33b55411-6d96-33ef-988e-c65da490808c | -3.30619 | -53.70027 | 2026-10-09 05:04:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| ae64e8f2-0a22-3740-a3ac-47116d8caa9f | -6.32089 | -54.80134 | 2026-10-09 05:04:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 9cc23e1f-ec26-3205-880b-72f9115f3747 | -11.66554 | -46.77597 | 2026-10-09 05:04:00 | NPP-375D | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 3.7 |
| db22db06-f884-386e-81ca-6a0e4cc99ed6 | -10.87949 | -44.79558 | 2026-10-09 05:04:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 10.6 |
| 3f2e45c9-c9f7-3889-81aa-5c9d1d50f199 | -4.29125 | -60.95508 | 2026-10-09 05:04:00 | NPP-375D | BERURI | AMAZONAS | Brasil | 1300631 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 6bcd0b23-917f-35d2-a262-68a2b8c0e39d | -5.10941 | -46.22116 | 2026-10-09 05:04:00 | NPP-375D | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Amazônia | 1.8 |
| d0a26241-e310-32f0-910e-eb1c44e92980 | -3.3245 | -61.2648 | 2026-10-09 05:04:00 | NPP-375D | CAAPIRANGA | AMAZONAS | Brasil | 1300839 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| f7c4bd8f-808b-397b-a0d7-bfe3cc1087c4 | -5.27887 | -55.95567 | 2026-10-09 05:04:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| a4a13e1f-5168-328f-8ffe-ed46afdb3228 | -3.08161 | -54.26236 | 2026-10-09 05:04:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| c540b608-77b7-3bdc-ae5c-f8afa291a1f4 | -4.28214 | -55.72314 | 2026-10-09 05:04:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| ee5cf466-f0ce-3e49-aa7f-0a52e88ad3a1 | -3.20695 | -53.86526 | 2026-10-09 05:04:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 6ebb24e6-90c4-3fd5-b717-c5d157321c44 | -5.75591 | -50.22772 | 2026-10-09 05:04:00 | NPP-375D | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| ef2f6283-8d87-3bbd-aa4b-930e9f9eb678 | -8.73332 | -45.13677 | 2026-10-09 05:04:00 | NPP-375D | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 6.0 |
| 94a74c78-00fc-3bcd-9c56-dd4f1bc62240 | -6.54047 | -56.0384 | 2026-10-09 05:04:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| e65337d5-2b4f-3e8a-b879-7c7eab60d1a2 | -5.87764 | -53.52127 | 2026-10-09 05:04:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 5.2 |
| e3c387bb-b1b4-3bf6-afab-95f1bcc255db | -3.04 | -53.8973 | 2026-10-09 05:04:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 45afbcf6-e951-35ed-adea-06969fddce42 | -8.96953 | -45.15548 | 2026-10-09 05:04:00 | NPP-375D | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 9899f6b7-fcd1-3cd8-b2c6-08ac02648ac8 | -5.22834 | -60.23625 | 2026-10-09 05:04:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| daba7adf-0039-3c61-b67c-f765d9b4a997 | -3.10209 | -53.95381 | 2026-10-09 05:04:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 65b0f653-30a8-3b4d-b659-779497d6c09b | -6.49521 | -62.8529 | 2026-10-09 05:04:00 | NPP-375D | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| e9170cf9-4ac9-33e3-8bf1-74425e2791d5 | -2.94418 | -54.1537 | 2026-10-09 05:04:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| d17cfb7f-5be2-3da3-8d67-2aa6ab7fb4da | -11.18378 | -45.3161 | 2026-10-09 05:04:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 06c439ed-035d-3f2f-a3f2-7e81e4dc498d | -3.58689 | -54.68276 | 2026-10-09 05:04:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 942979aa-b7bc-31b2-88dd-f637f3e0288d | -3.30726 | -54.02401 | 2026-10-09 05:04:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 435eb70c-b079-380a-a496-bf2dc699cec5 | -4.30831 | -54.79557 | 2026-10-09 05:04:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| d79768f6-3ebd-3f5e-9f41-28afc5c77df8 | -9.03248 | -46.86478 | 2026-10-09 05:04:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 47f0b2c2-9ebd-3545-84cc-92a9b2ca6a79 | -3.39906 | -60.84825 | 2026-10-09 05:04:00 | NPP-375D | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| b13c2da6-d319-39d4-a06a-a5ec759628f2 | -3.4705 | -60.25626 | 2026-10-09 05:04:00 | NPP-375D | CAREIRO | AMAZONAS | Brasil | 1301100 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 563775a4-2fbc-31b2-9da2-90fb901bdd60 | -2.82765 | -57.6214 | 2026-10-09 05:04:00 | NPP-375D | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 6b399a0b-fbfd-3e19-bc34-7cd024ef2047 | -3.65518 | -54.28524 | 2026-10-09 05:04:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| e161ec33-a360-37d7-b2f4-dfbda6133af1 | -6.82812 | -39.56134 | 2026-10-09 05:04:00 | NPP-375D | FARIAS BRITO | CEARÁ | Brasil | 2304301 | 23 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 8bcbb7b2-9426-32be-b06c-dc1ebb2ef92b | -8.75448 | -62.61902 | 2026-10-09 05:04:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 999ed53e-097d-3504-9bdc-4ac7bc8de982 | -3.22474 | -54.29156 | 2026-10-09 05:04:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| bf5a177d-435f-3e04-a68e-4dad29e06d5a | -7.47315 | -42.84071 | 2026-10-09 05:04:00 | NPP-375D | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 1eda22ad-3f83-3e18-be2b-e492ef299dd5 | -6.51681 | -51.11846 | 2026-10-09 05:04:00 | NPP-375D | OURILÂNDIA DO NORTE | PARÁ | Brasil | 1505437 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| e0ad0490-a916-32ed-a106-963f4fe768de | -6.0068 | -40.9584 | 2026-10-09 05:04:00 | NPP-375D | ASSUNÇÃO DO PIAUÍ | PIAUÍ | Brasil | 2201051 | 22 | 33 | nan | nan | nan | Caatinga | 6.4 |
| 8a9a3954-2a6a-390d-98ba-458c99a14402 | -2.50281 | -58.06976 | 2026-10-09 05:04:00 | NPP-375D | SÃO SEBASTIÃO DO UATUMÃ | AMAZONAS | Brasil | 1303957 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| b29ed0f8-40d8-3f3c-8a0f-91d8fb55cb1a | -3.02545 | -54.18554 | 2026-10-09 05:04:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 9.4 |
| 86f88d3d-b97b-3fca-9b10-5a209c785987 | -3.99134 | -59.35659 | 2026-10-09 05:04:00 | NPP-375D | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 6.8 |
| 1c0f7384-b6f3-39fb-bd59-ae4b24eac1f4 | -8.84111 | -61.46496 | 2026-10-09 05:04:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 1c19da77-4183-3d66-aea0-cd51a908771f | -6.22305 | -44.14725 | 2026-10-09 05:04:00 | NPP-375D | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 9f571f9d-53ab-3b45-8048-21e1d231f1dd | -3.16669 | -54.74041 | 2026-10-09 05:04:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| c9fac75f-16c3-324e-be21-ddf1e412507f | -2.90649 | -54.02524 | 2026-10-09 05:04:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| f7cf678e-d2e1-38e7-88fb-1a6dfe4824ad | -7.48556 | -42.83431 | 2026-10-09 05:04:00 | NPP-375D | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 90bb3f19-d532-3fa5-9a5c-13f200612917 | -3.1637 | -61.08383 | 2026-10-09 05:04:00 | NPP-375D | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 1062ee6a-57f4-3c55-8c1f-c2199549a865 | -3.10789 | -53.78461 | 2026-10-09 05:04:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 7.3 |
| a540517c-ec4d-3526-b164-492be9d80315 | -3.10954 | -54.15854 | 2026-10-09 05:04:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| dfea4b6e-1565-33b7-82ba-06011a88f2c8 | -6.50222 | -55.38789 | 2026-10-09 05:04:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| e572663d-b9c9-3731-b564-4ce18a374443 | -2.99036 | -53.84398 | 2026-10-09 05:04:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 2f2df956-dc1e-3b56-87c8-855f24181b7e | -8.19638 | -46.42225 | 2026-10-09 05:04:00 | NPP-375D | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 9b3b4542-8e25-3353-914c-0949a46d498d | -6.3874 | -55.25874 | 2026-10-09 05:04:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 597f1884-5bcd-30f6-bdda-b5a681b3c414 | -3.0573 | -54.03271 | 2026-10-09 05:04:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| e5d3e071-1e23-3938-b864-0c17d8ac269c | -5.92528 | -51.81861 | 2026-10-09 05:04:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 4f49daa6-d099-36fa-9778-2db250747e49 | -11.24222 | -44.87119 | 2026-10-09 05:04:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |


[Clique aqui para ver as próximas entradas](README169.md)
