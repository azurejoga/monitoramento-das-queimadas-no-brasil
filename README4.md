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

## Dados Diários - Página 4

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| a86d30a2-66d3-3fb9-88ca-31b2de7c323e | -6.73425 | -35.32439 | 2024-12-09 03:29:00 | NOAA-21 | CURRAL DE CIMA | PARAÍBA | Brasil | 2505279 | 25 | 33 | nan | nan | nan | Caatinga | 1.5 |
| d3a4d145-37c8-30d6-9e70-5594697e8312 | -3.42977 | -42.98351 | 2024-12-09 03:29:00 | NOAA-21 | ANAPURUS | MARANHÃO | Brasil | 2100808 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| c85d2d5a-5ff3-3ea1-b708-cc9946db92dc | -3.23328 | -42.43022 | 2024-12-09 03:29:00 | NOAA-21 | SÃO BERNARDO | MARANHÃO | Brasil | 2110609 | 21 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 1dcdee58-a1f1-3171-b632-45f10b691cd1 | -3.42895 | -42.98824 | 2024-12-09 03:29:00 | NOAA-21 | SANTA QUITÉRIA DO MARANHÃO | MARANHÃO | Brasil | 2110104 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 75293d72-604c-3ff2-ab20-6d3edcb4acbc | -2.90165 | -40.44297 | 2024-12-09 03:29:00 | NOAA-21 | JIJOCA DE JERICOACOARA | CEARÁ | Brasil | 2307254 | 23 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 5ab6cbfb-386b-3da0-b820-93b4c37fb75d | -5.47596 | -39.41151 | 2024-12-09 03:29:00 | NOAA-21 | QUIXERAMOBIM | CEARÁ | Brasil | 2311405 | 23 | 33 | nan | nan | nan | Caatinga | 5.1 |
| 3661de00-026e-38b2-a8d4-7927c2fc092e | -5.64701 | -35.47393 | 2024-12-09 03:29:00 | NOAA-21 | CEARÁ-MIRIM | RIO GRANDE DO NORTE | Brasil | 2402600 | 24 | 33 | nan | nan | nan | Caatinga | 1.4 |
| cf09d39b-d0ab-36f9-ad48-9a1b8e5ec589 | -2.90219 | -40.43971 | 2024-12-09 03:29:00 | NOAA-21 | JIJOCA DE JERICOACOARA | CEARÁ | Brasil | 2307254 | 23 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 8d895437-1456-3525-9597-9e85619018ea | -3.22652 | -42.43391 | 2024-12-09 03:29:00 | NOAA-21 | SÃO BERNARDO | MARANHÃO | Brasil | 2110609 | 21 | 33 | nan | nan | nan | Cerrado | 5.8 |
| a47011a0-8df5-3b7f-a0c0-e3bb2d2dfaa5 | -3.2351 | -42.4353 | 2024-12-09 03:30:00 | GOES-16 | SÃO BERNARDO | MARANHÃO | Brasil | 2110609 | 21 | 33 | nan | nan | nan | Cerrado | 47.7 |
| dfd37762-b34f-3f8d-8abb-a8a0578bf4de | -13.2709 | -51.0929 | 2024-12-09 03:30:00 | GOES-16 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 72.0 |
| 1d66e3da-7d90-36e8-812a-6220542cb5bf | -9.978 | -36.47979 | 2024-12-09 03:32:00 | NOAA-21 | SÃO SEBASTIÃO | ALAGOAS | Brasil | 2708808 | 27 | 33 | nan | nan | nan | Mata Atlântica | 7.9 |
| 8fcaf849-64c1-3ad8-b2a3-1612d5e656b0 | -7.91279 | -35.19772 | 2024-12-09 03:32:00 | NOAA-21 | PAUDALHO | PERNAMBUCO | Brasil | 2610608 | 26 | 33 | nan | nan | nan | Mata Atlântica | 25.6 |
| 026a66b6-d60d-3c5b-8402-901d85179583 | -5.58071 | -45.21154 | 2024-12-09 03:32:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 6.4 |
| 424c0173-ded3-3459-b5f6-eed9c4912250 | -7.52251 | -34.94019 | 2024-12-09 03:32:00 | NOAA-21 | CAAPORÃ | PARAÍBA | Brasil | 2503001 | 25 | 33 | nan | nan | nan | Mata Atlântica | 1.9 |
| 9599f149-4536-3964-a10f-09af2de82304 | -6.97678 | -34.92694 | 2024-12-09 03:32:00 | NOAA-21 | SANTA RITA | PARAÍBA | Brasil | 2513703 | 25 | 33 | nan | nan | nan | Mata Atlântica | 3.6 |
| e585f07b-4890-3b64-bafd-8bdc421eb2e9 | -9.0341 | -35.64402 | 2024-12-09 03:32:00 | NOAA-21 | MATRIZ DE CAMARAGIBE | ALAGOAS | Brasil | 2705101 | 27 | 33 | nan | nan | nan | Mata Atlântica | 9.1 |
| c23fe7f2-9b2b-3c8f-b72a-b51d24f228ff | -5.58096 | -45.21585 | 2024-12-09 03:32:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 8.6 |
| 8fb4cf9c-d313-3a85-ab4b-4ec115165887 | -9.9787 | -36.47552 | 2024-12-09 03:32:00 | NOAA-21 | SÃO SEBASTIÃO | ALAGOAS | Brasil | 2708808 | 27 | 33 | nan | nan | nan | Mata Atlântica | 7.9 |
| f8fad8f5-76b3-3cce-ac70-8b21139cfb8e | -6.97137 | -34.93826 | 2024-12-09 03:32:00 | NOAA-21 | SANTA RITA | PARAÍBA | Brasil | 2513703 | 25 | 33 | nan | nan | nan | Mata Atlântica | 3.5 |
| 282f294f-cfee-39b6-9afd-2789dbc5f236 | -9.36829 | -35.82167 | 2024-12-09 03:32:00 | NOAA-21 | MESSIAS | ALAGOAS | Brasil | 2705200 | 27 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 492be2dc-47cb-38ce-a2d1-5287d3a78212 | -6.97391 | -34.92248 | 2024-12-09 03:32:00 | NOAA-21 | SANTA RITA | PARAÍBA | Brasil | 2513703 | 25 | 33 | nan | nan | nan | Mata Atlântica | 3.6 |
| 3633127a-4280-38a8-bcfc-56673c8f4771 | -6.96786 | -34.93771 | 2024-12-09 03:32:00 | NOAA-21 | SANTA RITA | PARAÍBA | Brasil | 2513703 | 25 | 33 | nan | nan | nan | Mata Atlântica | 5.2 |
| 59030192-6679-3ffa-a124-6ec5a1d4e6ee | -6.97615 | -34.93089 | 2024-12-09 03:32:00 | NOAA-21 | SANTA RITA | PARAÍBA | Brasil | 2513703 | 25 | 33 | nan | nan | nan | Mata Atlântica | 4.4 |
| f38f3d0a-c4b8-3e73-a7fa-f746f8aa483f | -8.42411 | -35.11381 | 2024-12-09 03:32:00 | NOAA-21 | IPOJUCA | PERNAMBUCO | Brasil | 2607208 | 26 | 33 | nan | nan | nan | Mata Atlântica | 1.8 |
| 081b0871-533b-32ed-a722-0540c30d0135 | -8.94922 | -35.18945 | 2024-12-09 03:32:00 | NOAA-21 | MARAGOGI | ALAGOAS | Brasil | 2704500 | 27 | 33 | nan | nan | nan | Mata Atlântica | 2.1 |
| 39f69eab-991b-34d4-bded-2bea6fe7804b | -7.91566 | -35.20224 | 2024-12-09 03:32:00 | NOAA-21 | PAUDALHO | PERNAMBUCO | Brasil | 2610608 | 26 | 33 | nan | nan | nan | Mata Atlântica | 3.1 |
| e8ec9b0c-a531-37db-82f3-686687f9694b | -5.58212 | -45.20957 | 2024-12-09 03:32:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 10.3 |
| 9c2c2eba-b9c8-38a2-9fda-9df217834d0b | -10.6964 | -37.04937 | 2024-12-09 03:32:00 | NOAA-21 | ROSÁRIO DO CATETE | SERGIPE | Brasil | 2806107 | 28 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 0d23b20d-de27-330c-8e98-04d59d7f79c7 | -6.97867 | -34.91518 | 2024-12-09 03:32:00 | NOAA-21 | SANTA RITA | PARAÍBA | Brasil | 2513703 | 25 | 33 | nan | nan | nan | Mata Atlântica | 3.7 |
| 6dd406c7-edf7-31bb-bbf5-ef372b8370d6 | -6.96976 | -34.92588 | 2024-12-09 03:32:00 | NOAA-21 | SANTA RITA | PARAÍBA | Brasil | 2513703 | 25 | 33 | nan | nan | nan | Mata Atlântica | 6.2 |
| 52f1f9f9-0fdf-3bd2-a625-d5e2fd548880 | -5.86608 | -45.36505 | 2024-12-09 03:32:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 9406d17f-b8ef-3e37-a02a-c9b10edab2bb | -6.97263 | -34.93037 | 2024-12-09 03:32:00 | NOAA-21 | SANTA RITA | PARAÍBA | Brasil | 2513703 | 25 | 33 | nan | nan | nan | Mata Atlântica | 4.4 |
| bc858253-4ff5-32a2-abf8-511342032a3d | -8.49782 | -35.01109 | 2024-12-09 03:32:00 | NOAA-21 | IPOJUCA | PERNAMBUCO | Brasil | 2607208 | 26 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| dd5b40d7-a235-3719-a702-46fc58792229 | -8.75016 | -36.18602 | 2024-12-09 03:32:00 | NOAA-21 | JUREMA | PERNAMBUCO | Brasil | 2608404 | 26 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 4c04777f-df11-3717-8761-227cd5888991 | -12.2813 | -45.49858 | 2024-12-09 03:32:00 | NOAA-21 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 5.8 |
| 46170b78-2e73-37b4-8eb4-0d74ff8d6e91 | -12.28355 | -45.49724 | 2024-12-09 03:32:00 | NOAA-21 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 11836f70-fcb1-3b47-a550-0776c930ef89 | -5.85925 | -45.3637 | 2024-12-09 03:32:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 93493ae7-bf6e-3771-bc23-4d960b2be963 | -8.4972 | -35.01492 | 2024-12-09 03:32:00 | NOAA-21 | IPOJUCA | PERNAMBUCO | Brasil | 2607208 | 26 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 4e087d61-01b1-3d19-a5c3-0f96d1622292 | -10.36357 | -40.55099 | 2024-12-09 03:32:00 | NOAA-21 | CAMPO FORMOSO | BAHIA | Brasil | 2906006 | 29 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 9c00569d-9fb7-37a0-b3d3-281668c3697e | -8.52833 | -39.44513 | 2024-12-09 03:32:00 | NOAA-21 | CABROBÓ | PERNAMBUCO | Brasil | 2603009 | 26 | 33 | nan | nan | nan | Caatinga | 2.2 |
| 4a1404ac-766a-38fe-be6e-cab5a6212a69 | -6.98217 | -34.91576 | 2024-12-09 03:32:00 | NOAA-21 | SANTA RITA | PARAÍBA | Brasil | 2513703 | 25 | 33 | nan | nan | nan | Mata Atlântica | 1.8 |
| 221476c0-8b40-3ab5-bf74-7de8440502e0 | -7.91215 | -35.20169 | 2024-12-09 03:32:00 | NOAA-21 | PAUDALHO | PERNAMBUCO | Brasil | 2610608 | 26 | 33 | nan | nan | nan | Mata Atlântica | 25.6 |
| 339df8c0-0a74-3a3a-8aca-884e4b47d3b2 | -10.08748 | -36.09911 | 2024-12-09 03:32:00 | NOAA-21 | CORURIPE | ALAGOAS | Brasil | 2702306 | 27 | 33 | nan | nan | nan | Mata Atlântica | 3.7 |
| ce496a1c-fc14-3c23-b8cd-3885db511e01 | -6.83246 | -44.38496 | 2024-12-09 03:32:00 | NOAA-21 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 226b617a-2cc1-3bed-8674-b432747f78ba | -10.69473 | -37.05093 | 2024-12-09 03:32:00 | NOAA-21 | ROSÁRIO DO CATETE | SERGIPE | Brasil | 2806107 | 28 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 8d6d6de8-ff29-3322-becf-b7906a413855 | -6.9704 | -34.92194 | 2024-12-09 03:32:00 | NOAA-21 | SANTA RITA | PARAÍBA | Brasil | 2513703 | 25 | 33 | nan | nan | nan | Mata Atlântica | 6.2 |
| a3f96f28-661e-352e-91fc-ca12075c34b0 | -10.23194 | -36.30625 | 2024-12-09 03:32:00 | NOAA-21 | CORURIPE | ALAGOAS | Brasil | 2702306 | 27 | 33 | nan | nan | nan | Mata Atlântica | 2.8 |
| f53ff9e7-e676-3473-b3b9-051bfad69677 | -7.75547 | -35.14075 | 2024-12-09 03:32:00 | NOAA-21 | TRACUNHAÉM | PERNAMBUCO | Brasil | 2615508 | 26 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 82dde7eb-ebc6-30a6-8931-770bfc52bf4d | -5.85924 | -45.36753 | 2024-12-09 03:32:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 41902c98-1502-3f7e-8584-8d6f5bff6a4d | -5.86053 | -45.36065 | 2024-12-09 03:32:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 37339ea0-9e2d-3663-86f8-21d331563ac7 | -7.88471 | -35.14883 | 2024-12-09 03:32:00 | NOAA-21 | PAUDALHO | PERNAMBUCO | Brasil | 2610608 | 26 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 111c4301-6b94-3f12-b71f-78abcc548693 | -6.96849 | -34.93378 | 2024-12-09 03:32:00 | NOAA-21 | SANTA RITA | PARAÍBA | Brasil | 2513703 | 25 | 33 | nan | nan | nan | Mata Atlântica | 3.2 |
| 8ea3279d-e054-3e1e-9f23-bba46c6ad95b | -7.88757 | -35.15336 | 2024-12-09 03:32:00 | NOAA-21 | PAUDALHO | PERNAMBUCO | Brasil | 2610608 | 26 | 33 | nan | nan | nan | Mata Atlântica | 2.6 |
| ebf8faf2-e465-3de7-bbf6-0c2fab73f006 | -9.03764 | -35.64463 | 2024-12-09 03:32:00 | NOAA-21 | MATRIZ DE CAMARAGIBE | ALAGOAS | Brasil | 2705101 | 27 | 33 | nan | nan | nan | Mata Atlântica | 9.1 |
| f6b491d9-0910-35eb-8ac9-be80e83c41f2 | -12.28256 | -45.50221 | 2024-12-09 03:32:00 | NOAA-21 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 2bef6398-2bab-3730-85ae-48000414f07e | -12.28028 | -45.50354 | 2024-12-09 03:32:00 | NOAA-21 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 6de8e6e4-e9a5-3891-8158-8bab2d9f3bc3 | -7.88407 | -35.15276 | 2024-12-09 03:32:00 | NOAA-21 | PAUDALHO | PERNAMBUCO | Brasil | 2610608 | 26 | 33 | nan | nan | nan | Mata Atlântica | 2.7 |
| 443b5a75-583a-3ecd-b28a-12040b9106fa | -5.5796 | -45.21782 | 2024-12-09 03:32:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 6.3 |
| c6fab557-094c-36db-a708-8e1643a67602 | -9.03476 | -35.64 | 2024-12-09 03:32:00 | NOAA-21 | MATRIZ DE CAMARAGIBE | ALAGOAS | Brasil | 2705101 | 27 | 33 | nan | nan | nan | Mata Atlântica | 2.1 |
| c373d305-5cdc-3e41-b078-016faceb257d | -9.36767 | -35.8206 | 2024-12-09 03:32:00 | NOAA-21 | MESSIAS | ALAGOAS | Brasil | 2705200 | 27 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 0b592e65-8bdc-3a34-a810-da9fcf956541 | -6.97804 | -34.91909 | 2024-12-09 03:32:00 | NOAA-21 | SANTA RITA | PARAÍBA | Brasil | 2513703 | 25 | 33 | nan | nan | nan | Mata Atlântica | 3.7 |
| e55b9154-d274-3ccc-8da0-762c6d35a987 | -6.972 | -34.93432 | 2024-12-09 03:32:00 | NOAA-21 | SANTA RITA | PARAÍBA | Brasil | 2513703 | 25 | 33 | nan | nan | nan | Mata Atlântica | 4.4 |
| f68a447f-bb96-34ce-b551-0a7fcd07dd9b | -5.58183 | -45.20527 | 2024-12-09 03:32:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 6.4 |
| ec6793ee-5dec-35c2-95e5-d868fe34b43f | -9.99131 | -38.16626 | 2024-12-09 03:32:00 | NOAA-21 | JEREMOABO | BAHIA | Brasil | 2918100 | 29 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 108b8b08-eb86-3a3d-a739-2bd1e25c9770 | -8.11612 | -35.06519 | 2024-12-09 03:32:00 | NOAA-21 | JABOATÃO DOS GUARARAPES | PERNAMBUCO | Brasil | 2607901 | 26 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| 84ac82e5-181d-30ce-ab31-4a634faffc1b | -8.42063 | -35.11324 | 2024-12-09 03:32:00 | NOAA-21 | IPOJUCA | PERNAMBUCO | Brasil | 2607208 | 26 | 33 | nan | nan | nan | Mata Atlântica | 2.4 |
| 59300171-d733-3fce-bf67-c18c537d1820 | -9.98235 | -36.47614 | 2024-12-09 03:32:00 | NOAA-21 | SÃO SEBASTIÃO | ALAGOAS | Brasil | 2708808 | 27 | 33 | nan | nan | nan | Mata Atlântica | 7.9 |
| 514ee03d-8f8a-32d9-98af-127866e16a55 | -10.08931 | -36.09576 | 2024-12-09 03:32:00 | NOAA-21 | CORURIPE | ALAGOAS | Brasil | 2702306 | 27 | 33 | nan | nan | nan | Mata Atlântica | 3.8 |
| 2b2d6b9e-b75d-3af5-a6c1-e6003dc718ae | -12.35417 | -38.14268 | 2024-12-09 03:32:00 | NOAA-21 | ITANAGRA | BAHIA | Brasil | 2915908 | 29 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 8039e808-a971-3c31-8695-c75264ff494d | -8.74947 | -36.19029 | 2024-12-09 03:32:00 | NOAA-21 | JUREMA | PERNAMBUCO | Brasil | 2608404 | 26 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 47a05b4d-dc8d-34a6-bb72-7e0ff4cde0c3 | -6.97454 | -34.91854 | 2024-12-09 03:32:00 | NOAA-21 | SANTA RITA | PARAÍBA | Brasil | 2513703 | 25 | 33 | nan | nan | nan | Mata Atlântica | 3.7 |
| add0393f-a9fd-35dd-9f01-309f2c035acf | -10.55815 | -36.96383 | 2024-12-09 03:32:00 | NOAA-21 | JAPARATUBA | SERGIPE | Brasil | 2803302 | 28 | 33 | nan | nan | nan | Mata Atlântica | 2.4 |
| 869e013a-62c1-3f04-80ff-9504048a4859 | -15.97231 | -42.25083 | 2024-12-09 03:34:00 | NOAA-21 | SALINAS | MINAS GERAIS | Brasil | 3157005 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.4 |
| 17e4b024-2c01-389d-8c98-fd42ccfbb4ee | -18.07887 | -45.28629 | 2024-12-09 03:34:00 | NOAA-21 | SÃO GONÇALO DO ABAETÉ | MINAS GERAIS | Brasil | 3161700 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 7a773b2d-387b-3b3c-ba4c-d149e81f9519 | -18.30773 | -47.19608 | 2024-12-09 03:34:00 | NOAA-21 | COROMANDEL | MINAS GERAIS | Brasil | 3119302 | 31 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 657631f5-36e7-3a97-a93a-d73d02e05145 | -18.30883 | -47.19126 | 2024-12-09 03:34:00 | NOAA-21 | COROMANDEL | MINAS GERAIS | Brasil | 3119302 | 31 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 63175afa-ce9a-3c3e-b2ed-789291a1310b | -17.67455 | -42.74348 | 2024-12-09 03:34:00 | NOAA-21 | ITAMARANDIBA | MINAS GERAIS | Brasil | 3132503 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 331178aa-ae02-3cb8-a396-38b63086f312 | -19.37389 | -43.74612 | 2024-12-09 03:34:00 | NOAA-21 | JABOTICATUBAS | MINAS GERAIS | Brasil | 3134608 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 21a0afd6-523a-31ed-ab39-f428a83ebe2d | -17.09313 | -43.80415 | 2024-12-09 03:34:00 | NOAA-21 | BOCAIÚVA | MINAS GERAIS | Brasil | 3107307 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 48da7b68-787c-39fb-9629-2697aefbf944 | -18.30389 | -47.19038 | 2024-12-09 03:34:00 | NOAA-21 | COROMANDEL | MINAS GERAIS | Brasil | 3119302 | 31 | 33 | nan | nan | nan | Cerrado | 2.5 |
| cbf4e7fe-afe0-31a4-9f51-3a04b797106f | -19.06301 | -43.61453 | 2024-12-09 03:34:00 | NOAA-21 | CONCEIÇÃO DO MATO DENTRO | MINAS GERAIS | Brasil | 3117504 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 6951223f-82a6-35ae-be71-b2141d1e0f3b | -14.97625 | -44.41145 | 2024-12-09 03:34:00 | NOAA-21 | JANUÁRIA | MINAS GERAIS | Brasil | 3135209 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| a62cbc01-b468-3f9a-b9eb-851237428889 | -18.07832 | -45.28371 | 2024-12-09 03:34:00 | NOAA-21 | SÃO GONÇALO DO ABAETÉ | MINAS GERAIS | Brasil | 3161700 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 31ffcfa5-4690-34ca-b1fb-5eb43124a787 | -16.34718 | -43.69685 | 2024-12-09 03:34:00 | NOAA-21 | CAPITÃO ENÉAS | MINAS GERAIS | Brasil | 3112703 | 31 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 90b15ab8-fdaa-3c0a-a3a4-a0cadbfc9fe0 | -20.59335 | -42.12558 | 2024-12-09 03:34:00 | NOAA-21 | DIVINO | MINAS GERAIS | Brasil | 3122009 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 6f5ab381-8586-3d96-99ea-a93872a66074 | -19.369 | -43.74501 | 2024-12-09 03:34:00 | NOAA-21 | JABOTICATUBAS | MINAS GERAIS | Brasil | 3134608 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| c9479f6d-229c-345f-bc83-527567d02236 | -15.9733 | -42.24897 | 2024-12-09 03:34:00 | NOAA-21 | SALINAS | MINAS GERAIS | Brasil | 3157005 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.2 |
| 9327dd86-2f28-301b-9a96-29c9c1ead484 | -14.97549 | -44.41527 | 2024-12-09 03:34:00 | NOAA-21 | JANUÁRIA | MINAS GERAIS | Brasil | 3135209 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 219ae5d0-d963-31ba-94f0-92e42967eb23 | -18.30282 | -47.19521 | 2024-12-09 03:34:00 | NOAA-21 | COROMANDEL | MINAS GERAIS | Brasil | 3119302 | 31 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 1ba4326d-2aea-331d-ac12-0e0b26e9e035 | -19.37028 | -43.7481 | 2024-12-09 03:34:00 | NOAA-21 | JABOTICATUBAS | MINAS GERAIS | Brasil | 3134608 | 31 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 404a065e-c839-3055-afe9-9ea748652c5c | -20.90108 | -43.8194 | 2024-12-09 03:36:00 | NOAA-21 | CARANDAÍ | MINAS GERAIS | Brasil | 3113206 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| 1cfdeacd-f4a1-3c09-8b1c-91b84591db02 | -3.2351 | -42.4353 | 2024-12-09 03:40:00 | GOES-16 | SÃO BERNARDO | MARANHÃO | Brasil | 2110609 | 21 | 33 | nan | nan | nan | Cerrado | 53.1 |
| 9566db4f-2dbc-3d84-8043-19d57a51180b | -3.2351 | -42.4353 | 2024-12-09 03:50:00 | GOES-16 | SÃO BERNARDO | MARANHÃO | Brasil | 2110609 | 21 | 33 | nan | nan | nan | Cerrado | 41.1 |
| f80f42e3-0cc8-3d59-9e43-12eafadaee9a | -7.75001 | -35.26498 | 2024-12-09 03:53:00 | NPP-375D | NAZARÉ DA MATA | PERNAMBUCO | Brasil | 2609501 | 26 | 33 | nan | nan | nan | Mata Atlântica | 4.2 |
| e4ce00f5-8755-3e8f-885c-ec5f64ac39ab | -5.53749 | -39.23705 | 2024-12-09 03:53:00 | NPP-375D | QUIXERAMOBIM | CEARÁ | Brasil | 2311405 | 23 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 9a4bc14d-3ec3-315a-8e16-ae961715275c | -5.47882 | -39.41019 | 2024-12-09 03:53:00 | NPP-375D | QUIXERAMOBIM | CEARÁ | Brasil | 2311405 | 23 | 33 | nan | nan | nan | Caatinga | 2.4 |
| e2dde200-56dc-3133-ba7f-304fab983413 | -5.33198 | -44.13908 | 2024-12-09 03:53:00 | NPP-375D | GOVERNADOR EUGÊNIO BARROS | MARANHÃO | Brasil | 2104602 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 24f4d310-a439-36bf-891a-46a6c7b84376 | -6.96833 | -34.92158 | 2024-12-09 03:53:00 | NPP-375D | SANTA RITA | PARAÍBA | Brasil | 2513703 | 25 | 33 | nan | nan | nan | Mata Atlântica | 10.7 |
| a915bec2-a4e8-3cdd-b0b1-80493cd3507e | -5.42092 | -44.71107 | 2024-12-09 03:53:00 | NPP-375D | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |


[Clique aqui para ver as próximas entradas](README5.md)
