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
| 0b4afc14-aabf-34d1-a5e0-bea71e15cd17 | -6.63522 | -44.63409 | 2025-10-27 03:42:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 9866e101-3954-3a4a-b1f6-9b9aa97daca3 | -10.32787 | -47.15243 | 2025-10-27 03:42:00 | NOAA-20 | NOVO ACORDO | TOCANTINS | Brasil | 1715101 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 8708a23b-c797-3b4c-ab07-e31467c3a4a2 | -7.975 | -45.47072 | 2025-10-27 03:42:00 | NOAA-20 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 6f9b4987-599b-3a58-8dbc-97efa14b8758 | -7.96633 | -45.46897 | 2025-10-27 03:42:00 | NOAA-20 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 83ec34b4-5079-341c-ac4e-943223439abc | -8.69144 | -44.43105 | 2025-10-27 03:42:00 | NOAA-20 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| cfc6092e-52ea-3c39-96cf-9fec43bcb063 | -7.85246 | -46.45256 | 2025-10-27 03:42:00 | NOAA-20 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 30993492-61f3-3031-86b5-831ced56a796 | -7.43618 | -41.87081 | 2025-10-27 03:42:00 | NOAA-20 | SANTO INÁCIO DO PIAUÍ | PIAUÍ | Brasil | 2209500 | 22 | 33 | nan | nan | nan | Caatinga | 7.0 |
| d998fe41-958f-3a2c-89b5-ddcef1c997cf | -10.21537 | -44.82243 | 2025-10-27 03:42:00 | NOAA-20 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 65561272-d3fb-3b64-ac97-a1dc2e763393 | -6.25781 | -41.84099 | 2025-10-27 03:42:00 | NOAA-20 | VALENÇA DO PIAUÍ | PIAUÍ | Brasil | 2211308 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| e4c33f3f-667e-34ff-b877-53452c2d4d0a | -9.98537 | -47.18937 | 2025-10-27 03:42:00 | NOAA-20 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 0b3fcc2f-bb16-3c3a-9aae-16c920e83ee2 | -7.84576 | -46.42192 | 2025-10-27 03:42:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 0f974653-537d-3555-ad31-5a2ff540dbbe | -10.73384 | -44.19232 | 2025-10-27 03:42:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| d2b13fc2-6ef7-33b5-84d6-1138a498db46 | -8.48653 | -41.22754 | 2025-10-27 03:42:00 | NOAA-20 | QUEIMADA NOVA | PIAUÍ | Brasil | 2208650 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 8a4b8d6c-561c-3874-8255-be7de6236f56 | -8.64499 | -47.24863 | 2025-10-27 03:42:00 | NOAA-20 | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 625ef037-e415-31c5-ae47-8245cedf9279 | -9.57226 | -46.90298 | 2025-10-27 03:42:00 | NOAA-20 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 6.6 |
| 5c37edc4-f183-3dbe-9e4e-4db6f7131e92 | -6.89408 | -45.15154 | 2025-10-27 03:42:00 | NOAA-20 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 2838fd11-8e58-3922-901d-b00f4ab39ff0 | -7.82968 | -46.44178 | 2025-10-27 03:42:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 536f63de-6cf5-3db7-9e2b-b5191e39ba68 | -7.78715 | -45.38304 | 2025-10-27 03:42:00 | NOAA-20 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 3e596e7c-0da4-3c26-ae1c-a191128a2e9b | -7.33475 | -42.44647 | 2025-10-27 03:42:00 | NOAA-20 | SÃO FRANCISCO DO PIAUÍ | PIAUÍ | Brasil | 2209708 | 22 | 33 | nan | nan | nan | Caatinga | 2.8 |
| 314c5f31-7dea-3a62-b1ef-e902132555bd | -6.44942 | -42.34592 | 2025-10-27 03:42:00 | NOAA-20 | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| e03daa68-a94d-3e00-b4f8-a0395057eded | -11.42327 | -46.1158 | 2025-10-27 03:42:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 54e4093d-c1cd-3eb8-9fd0-1588be40cdb4 | -7.85251 | -46.48581 | 2025-10-27 03:42:00 | NOAA-20 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 1b9d1702-072e-3757-8031-767ffb8177b0 | -10.21348 | -45.17903 | 2025-10-27 03:42:00 | NOAA-20 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 8646d1f3-a040-3b39-b0ed-ac23f953a84d | -7.76302 | -45.40168 | 2025-10-27 03:42:00 | NOAA-20 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 87d3e4ab-7990-39a9-9993-0e05452cca3f | -8.20995 | -43.8078 | 2025-10-27 03:42:00 | NOAA-20 | COLÔNIA DO GURGUÉIA | PIAUÍ | Brasil | 2202752 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 8e070f93-1f62-3667-aed7-b1d250075d05 | -7.78233 | -45.37777 | 2025-10-27 03:42:00 | NOAA-20 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 0ee9ba55-eec0-332d-aa16-ebc7cacd6345 | -8.03161 | -46.74709 | 2025-10-27 03:42:00 | NOAA-20 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| e8fdbaa0-1587-345e-ab77-e54ae93f0862 | -7.86436 | -46.42165 | 2025-10-27 03:42:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 50868dd5-a9cc-3889-89fe-423a57164966 | -8.40584 | -40.9878 | 2025-10-27 03:42:00 | NOAA-20 | AFRÂNIO | PERNAMBUCO | Brasil | 2600203 | 26 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 36504964-95cc-34c6-977e-50e3abf5cac2 | -8.03074 | -46.75182 | 2025-10-27 03:42:00 | NOAA-20 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| bda35764-e07b-34bb-be6f-71c29fa6fc18 | -8.6923 | -44.43259 | 2025-10-27 03:42:00 | NOAA-20 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 3464264d-a281-3121-8119-7e83d21b6e1b | -8.06179 | -42.49239 | 2025-10-27 03:42:00 | NOAA-20 | SOCORRO DO PIAUÍ | PIAUÍ | Brasil | 2210904 | 22 | 33 | nan | nan | nan | Caatinga | 3.9 |
| e2fd0459-9d87-3562-9d83-76499828b463 | -11.7852 | -45.25883 | 2025-10-27 03:42:00 | NOAA-20 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 674da7b0-38c5-3919-a280-341e85f0ad82 | -9.62483 | -40.34877 | 2025-10-27 03:42:00 | NOAA-20 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 0.7 |
| a6445c26-8986-3cda-adbb-efd63fef25dc | -6.25862 | -41.83632 | 2025-10-27 03:42:00 | NOAA-20 | VALENÇA DO PIAUÍ | PIAUÍ | Brasil | 2211308 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 37f1cd1d-136d-34b7-98f9-d73883d94439 | -8.66904 | -44.76276 | 2025-10-27 03:42:00 | NOAA-20 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 6f7855ab-5a8f-3bf4-b903-678bd43056c5 | -6.15103 | -43.13331 | 2025-10-27 03:42:00 | NOAA-20 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Caatinga | 2.7 |
| 04a90a01-b45f-3104-ba79-fba07aaf42c0 | -6.88775 | -45.15457 | 2025-10-27 03:42:00 | NOAA-20 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| e6c9d633-9d42-3926-8559-b38e9d8752f0 | -7.8331 | -46.45666 | 2025-10-27 03:42:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 4.4 |
| d7e2dc85-5bd2-3761-844e-b8cbf49b5606 | -8.64668 | -44.77327 | 2025-10-27 03:42:00 | NOAA-20 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| f104b98b-cd8f-31ac-8645-7dcfd7e0b0aa | -10.07278 | -44.86241 | 2025-10-27 03:42:00 | NOAA-20 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 08117937-a13c-3eee-82f5-4d53daf11fc3 | -10.34014 | -47.22663 | 2025-10-27 03:42:00 | NOAA-20 | NOVO ACORDO | TOCANTINS | Brasil | 1715101 | 17 | 33 | nan | nan | nan | Cerrado | 6.1 |
| 075a775f-79c1-318b-a305-5dcfae1f11fe | -8.09804 | -47.06268 | 2025-10-27 03:42:00 | NOAA-20 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| a29acfd3-bfd1-308c-9bcd-ee519cb407fa | -9.06034 | -45.10426 | 2025-10-27 03:42:00 | NOAA-20 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 2.4 |
| a59f71fc-d90e-3d8e-8843-2803b86257ed | -9.89836 | -45.76088 | 2025-10-27 03:42:00 | NOAA-20 | BARREIRAS DO PIAUÍ | PIAUÍ | Brasil | 2201309 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 9853c953-5a90-30ee-81ec-a3436761dd9e | -12.05906 | -43.98772 | 2025-10-27 03:42:00 | NOAA-20 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 8.0 |
| 9b3058e3-9d34-344d-9beb-f18b0e919758 | -9.55404 | -46.933 | 2025-10-27 03:42:00 | NOAA-20 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 320c6a17-7293-35a9-9b8b-061481947082 | -6.37198 | -44.26685 | 2025-10-27 03:42:00 | NOAA-20 | SUCUPIRA DO NORTE | MARANHÃO | Brasil | 2111904 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 876d3bba-987a-399a-b022-9bb92e42ee93 | -6.59576 | -42.6705 | 2025-10-27 03:42:00 | NOAA-20 | FRANCISCO AYRES | PIAUÍ | Brasil | 2204105 | 22 | 33 | nan | nan | nan | Caatinga | 2.2 |
| 4550e580-bd30-3369-acfc-3899c8e37fa2 | -7.08379 | -39.5722 | 2025-10-27 03:42:00 | NOAA-20 | CRATO | CEARÁ | Brasil | 2304202 | 23 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 193e2402-2e29-3af0-9c8c-c50a343b6437 | -7.43092 | -41.87463 | 2025-10-27 03:42:00 | NOAA-20 | SANTO INÁCIO DO PIAUÍ | PIAUÍ | Brasil | 2209500 | 22 | 33 | nan | nan | nan | Caatinga | 7.0 |
| 03042996-b4b3-3181-86c0-514109c13c09 | -6.14964 | -42.69146 | 2025-10-27 03:42:00 | NOAA-20 | ANGICAL DO PIAUÍ | PIAUÍ | Brasil | 2200608 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| a94892ca-7d1a-3370-80bc-e8bec45c3f17 | -7.77848 | -45.37996 | 2025-10-27 03:42:00 | NOAA-20 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 412eef12-080e-3653-b384-b620a67b06b0 | -8.64729 | -44.76985 | 2025-10-27 03:42:00 | NOAA-20 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| cebfb1de-2eb6-3426-ac4e-7f24f2c46310 | -6.23204 | -42.5565 | 2025-10-27 03:42:00 | NOAA-20 | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 5.4 |
| 711add2c-b8e4-36ae-bd50-de01dcd3572f | -10.3128 | -47.19835 | 2025-10-27 03:42:00 | NOAA-20 | NOVO ACORDO | TOCANTINS | Brasil | 1715101 | 17 | 33 | nan | nan | nan | Cerrado | 3.5 |
| effaea4c-b719-3330-a6b7-da3cd4109032 | -9.9899 | -47.16576 | 2025-10-27 03:42:00 | NOAA-20 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| bfb41106-1efd-3686-ac54-0cccdff75202 | -6.88287 | -43.56992 | 2025-10-27 03:42:00 | NOAA-20 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 5b4bc842-14fd-3978-be8a-3b824885ee13 | -7.00003 | -46.9991 | 2025-10-27 03:42:00 | NOAA-20 | ESTREITO | MARANHÃO | Brasil | 2104057 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 2fbee621-0863-33c8-aa3e-8782fa4dd3a2 | -8.69512 | -44.44624 | 2025-10-27 03:42:00 | NOAA-20 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 1a3a1f2f-5bd9-3b63-b517-bb45fac4e0aa | -7.93748 | -44.84023 | 2025-10-27 03:42:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 5904076a-4a13-394c-b73b-ad349deca442 | -8.3149 | -46.18158 | 2025-10-27 03:42:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| b2f3df32-5fa9-36cb-9c65-17db6778cd2f | -7.8228 | -46.44543 | 2025-10-27 03:42:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| d5fd38bb-b6f0-332c-913a-e1b571b87634 | -8.69715 | -44.42907 | 2025-10-27 03:42:00 | NOAA-20 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 71ef4496-4488-3ea1-8838-117c1da0215f | -7.0846 | -39.56735 | 2025-10-27 03:42:00 | NOAA-20 | CRATO | CEARÁ | Brasil | 2304202 | 23 | 33 | nan | nan | nan | Caatinga | 1.2 |
| a6f9f1a8-5844-3dac-9319-64751f748a0d | -10.16862 | -49.31959 | 2025-10-27 03:42:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 0e262dbf-8a03-3152-975e-8db29aac3147 | -7.80336 | -45.38934 | 2025-10-27 03:42:00 | NOAA-20 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 2.8 |
| a8498ae5-a262-382c-9820-56f0d3705fb9 | -7.59863 | -45.69104 | 2025-10-27 03:42:00 | NOAA-20 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| e3bb615c-088e-31be-b459-1aeedf5d364c | -7.43538 | -41.87537 | 2025-10-27 03:42:00 | NOAA-20 | SANTO INÁCIO DO PIAUÍ | PIAUÍ | Brasil | 2209500 | 22 | 33 | nan | nan | nan | Caatinga | 7.0 |
| 21f5b72a-650d-3795-89ee-fde273388314 | -7.43011 | -41.87924 | 2025-10-27 03:42:00 | NOAA-20 | SANTO INÁCIO DO PIAUÍ | PIAUÍ | Brasil | 2209500 | 22 | 33 | nan | nan | nan | Caatinga | 3.3 |
| 59bbe20f-6f4c-3586-9beb-9051b9a4415e | -7.83814 | -46.46291 | 2025-10-27 03:42:00 | NOAA-20 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 56d1ec1e-fb7c-3a98-b8e9-31da9540e000 | -8.48219 | -45.56253 | 2025-10-27 03:42:00 | NOAA-20 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 10b1a5c0-ed14-3117-aabb-8ddbb11009fd | -7.83375 | -46.48653 | 2025-10-27 03:42:00 | NOAA-20 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 11.6 |
| 5623248a-a5a4-3bb5-8ec2-1f1dd0946382 | -11.28523 | -45.15191 | 2025-10-27 03:42:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 59aa3702-c244-3839-8a12-09fc1235f7b9 | -6.23121 | -42.55931 | 2025-10-27 03:42:00 | NOAA-20 | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 2.7 |
| 5b15a5be-369e-381f-b17e-eb778a379bed | -6.88184 | -43.57584 | 2025-10-27 03:42:00 | NOAA-20 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 10.7 |
| 309bbc45-ab8d-3274-af4c-597c98d15cd2 | -7.4406 | -41.87175 | 2025-10-27 03:42:00 | NOAA-20 | SANTO INÁCIO DO PIAUÍ | PIAUÍ | Brasil | 2209500 | 22 | 33 | nan | nan | nan | Caatinga | 4.1 |
| 6e4b89d4-1980-32ab-bfd7-0226e975d711 | -8.2956 | -42.31518 | 2025-10-27 03:42:00 | NOAA-20 | SÃO JOÃO DO PIAUÍ | PIAUÍ | Brasil | 2210003 | 22 | 33 | nan | nan | nan | Caatinga | 2.3 |
| 93634222-3cd5-3fd3-91ec-0d44b2ae5120 | -10.31189 | -47.20306 | 2025-10-27 03:42:00 | NOAA-20 | NOVO ACORDO | TOCANTINS | Brasil | 1715101 | 17 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 5a0bd6bf-d016-33dd-8c5f-432d0ea44bec | -7.43376 | -41.88457 | 2025-10-27 03:42:00 | NOAA-20 | SANTO INÁCIO DO PIAUÍ | PIAUÍ | Brasil | 2209500 | 22 | 33 | nan | nan | nan | Caatinga | 3.3 |
| c1150cc2-4b93-39e9-ab86-b86ecf78b851 | -10.7475 | -44.20107 | 2025-10-27 03:42:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 31.4 |
| e70128eb-fdcd-367f-b646-687c2ad7770c | -10.35245 | -47.18676 | 2025-10-27 03:42:00 | NOAA-20 | NOVO ACORDO | TOCANTINS | Brasil | 1715101 | 17 | 33 | nan | nan | nan | Cerrado | 3.6 |
| fe68aace-52ba-3a73-8b77-3f057b81a1b6 | -8.02196 | -46.76521 | 2025-10-27 03:42:00 | NOAA-20 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 28738c18-01b5-3140-9444-05e24054747b | -7.83635 | -46.47254 | 2025-10-27 03:42:00 | NOAA-20 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 7.3 |
| 52d422a7-703b-3a84-a61d-1fd047d00106 | -7.97175 | -45.47118 | 2025-10-27 03:42:00 | NOAA-20 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 5ce926de-1ae4-3331-bf8b-7ed26763a6bd | -9.57046 | -46.91234 | 2025-10-27 03:42:00 | NOAA-20 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 4.4 |
| fc3e08e0-2145-393b-a9c6-a5ecef6249a7 | -8.57671 | -45.11017 | 2025-10-27 03:42:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 3d2d9e34-8137-3a3d-8001-92a6b525ffbe | -6.42834 | -42.0271 | 2025-10-27 03:42:00 | NOAA-20 | NOVO ORIENTE DO PIAUÍ | PIAUÍ | Brasil | 2206902 | 22 | 33 | nan | nan | nan | Caatinga | 3.3 |
| 89eb0bcf-297a-326a-8aae-5486de46e904 | -7.85505 | -46.47209 | 2025-10-27 03:42:00 | NOAA-20 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| b8803bc9-630c-38b1-953a-0b98adfe2bde | -11.42397 | -46.11225 | 2025-10-27 03:42:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 64de5973-d304-3b16-9050-231d195d92d6 | -6.88688 | -38.27849 | 2025-10-27 03:42:00 | NOAA-20 | SOUSA | PARAÍBA | Brasil | 2516201 | 25 | 33 | nan | nan | nan | Caatinga | 0.9 |
| b7d77224-4a3e-3ff5-a014-ea2aa07f73fd | -7.43457 | -41.87996 | 2025-10-27 03:42:00 | NOAA-20 | SANTO INÁCIO DO PIAUÍ | PIAUÍ | Brasil | 2209500 | 22 | 33 | nan | nan | nan | Caatinga | 3.3 |
| 762b6ca7-2ef4-3dfe-85ee-4da7ead775b1 | -9.55315 | -46.9376 | 2025-10-27 03:42:00 | NOAA-20 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 01fc88e5-3024-3794-b865-a322c4640c7c | -8.30733 | -46.18975 | 2025-10-27 03:42:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 0c056910-068e-3637-a144-540f047d5fe2 | -11.97082 | -44.30648 | 2025-10-27 03:42:00 | NOAA-20 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 2.8 |
| d8ea1463-0cef-3e15-aac3-26b68e710cf6 | -8.95782 | -47.19888 | 2025-10-27 03:42:00 | NOAA-20 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 7.1 |
| 35786388-5115-39c4-ab50-5d47d620be88 | -10.76429 | -44.19281 | 2025-10-27 03:42:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 28c62c6f-df27-3f05-89ed-7d0931d5996a | -6.85032 | -46.29539 | 2025-10-27 03:42:00 | NOAA-20 | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 17ebac8c-e3e7-381d-829c-0769e84c2c4a | -10.31099 | -47.20776 | 2025-10-27 03:42:00 | NOAA-20 | NOVO ACORDO | TOCANTINS | Brasil | 1715101 | 17 | 33 | nan | nan | nan | Cerrado | 4.0 |
| a78203ae-b780-3186-9cd6-a14ba7bd1040 | -6.48875 | -42.21862 | 2025-10-27 03:42:00 | NOAA-20 | VÁRZEA GRANDE | PIAUÍ | Brasil | 2211407 | 22 | 33 | nan | nan | nan | Caatinga | 2.2 |


[Clique aqui para ver as próximas entradas](README21.md)
