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

## Dados Diários - Página 74

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 5324c65c-dbbb-3dcf-ac11-64c9c7f4551d | -12.1988 | -53.9024 | 2025-09-09 08:30:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 77.3 |
| 96c8b568-36cd-3fc8-a499-387ddeb4cd0b | -21.8925 | -47.3114 | 2025-09-09 08:30:00 | GOES-19 | PIRASSUNUNGA | SÃO PAULO | Brasil | 3539301 | 35 | 33 | nan | nan | nan | Mata Atlântica | 101.1 |
| 261e590c-d1ba-34cd-b748-d8660b96c90c | -21.871 | -47.3406 | 2025-09-09 08:30:00 | GOES-19 | PIRASSUNUNGA | SÃO PAULO | Brasil | 3539301 | 35 | 33 | nan | nan | nan | Mata Atlântica | 185.9 |
| ec3283fa-6b72-3dcc-82d3-aeeab7d2b445 | -21.8717 | -47.3167 | 2025-09-09 08:30:00 | GOES-19 | PIRASSUNUNGA | SÃO PAULO | Brasil | 3539301 | 35 | 33 | nan | nan | nan | Mata Atlântica | 128.6 |
| 1a68fd2e-f6bb-3c0b-a4de-7ae94956e942 | -12.1991 | -53.8817 | 2025-09-09 08:30:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 79.6 |
| 3ede5d43-814f-3d0b-92d7-0ce0f38842a7 | -12.1991 | -53.8817 | 2025-09-09 08:40:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 56.6 |
| 6412478e-545f-310d-9015-66b28dd9b253 | -12.1988 | -53.9024 | 2025-09-09 08:40:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 66.2 |
| 25e041ee-a7e5-324b-8294-b75366d14eae | -12.1991 | -53.8817 | 2025-09-09 08:50:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 67.5 |
| 48978227-22b2-39c7-99e7-3e66d13a4c0a | -12.1988 | -53.9024 | 2025-09-09 08:50:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 70.9 |
| 2e1a7491-1bc9-3376-91d7-2f7f3d2b620c | -9.0931 | -45.7314 | 2025-09-09 09:10:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 169.0 |
| aa7d3a62-3300-33fb-92eb-a38b28aa2bac | -9.0934 | -45.7088 | 2025-09-09 09:10:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 222.8 |
| 198e6907-67e0-3592-9934-dfeb0e3404c5 | -14.3615 | -47.3333 | 2025-09-09 09:10:00 | GOES-19 | SÃO JOÃO D'ALIANÇA | GOIÁS | Brasil | 5220009 | 52 | 33 | nan | nan | nan | Cerrado | 160.2 |
| 9d5d7652-1aae-3b1f-b361-d55c8b91457a | -21.8918 | -47.3353 | 2025-09-09 09:20:00 | GOES-19 | PIRASSUNUNGA | SÃO PAULO | Brasil | 3539301 | 35 | 33 | nan | nan | nan | Mata Atlântica | 133.0 |
| 085470fa-04ea-3c24-9377-0e81a5051cf2 | -21.8717 | -47.3167 | 2025-09-09 09:50:00 | GOES-19 | PIRASSUNUNGA | SÃO PAULO | Brasil | 3539301 | 35 | 33 | nan | nan | nan | Mata Atlântica | 168.1 |
| 43072740-8c41-3bc1-905d-521a28dcf756 | -21.3915 | -48.9296 | 2025-09-09 10:50:00 | GOES-19 | ITÁPOLIS | SÃO PAULO | Brasil | 3522703 | 35 | 33 | nan | nan | nan | Cerrado | 555.9 |
| a7e0d70c-da03-360a-b5c4-84d2a8ce9cbd | -21.8918 | -47.3353 | 2025-09-09 10:50:00 | GOES-19 | PIRASSUNUNGA | SÃO PAULO | Brasil | 3539301 | 35 | 33 | nan | nan | nan | Mata Atlântica | 157.4 |
| af8baa19-feb4-3f9d-b268-dea89c53daaf | -21.3921 | -48.9064 | 2025-09-09 10:50:00 | GOES-19 | ITÁPOLIS | SÃO PAULO | Brasil | 3522703 | 35 | 33 | nan | nan | nan | Cerrado | 381.9 |
| 182d0f7c-16ae-3b39-bc20-a9d807df87ef | -21.8925 | -47.3114 | 2025-09-09 10:50:00 | GOES-19 | PIRASSUNUNGA | SÃO PAULO | Brasil | 3539301 | 35 | 33 | nan | nan | nan | Mata Atlântica | 188.0 |
| 34011808-cf21-37a3-afa1-eba5701ef170 | -5.5504 | -45.1891 | 2025-09-09 11:00:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 89.2 |
| 7c609d34-9238-3735-9672-503fceb858c7 | -10.817 | -48.2972 | 2025-09-09 11:20:00 | GOES-19 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 76.5 |
| 341507c3-1ffe-3a2e-9d6e-f8ebe9cb6029 | -11.9739 | -50.9935 | 2025-09-09 11:20:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 178.2 |
| 377d32d5-5d64-37ec-b767-e9f1b0e49f88 | -11.9548 | -50.9957 | 2025-09-09 11:20:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 90.9 |
| 198e6bcd-4411-3b03-a09b-ed16834ae806 | -15.8205 | -52.2444 | 2025-09-09 11:20:00 | GOES-19 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 80.8 |
| 64e9ffca-2037-3d4b-bf43-a15f1701a74d | -11.9926 | -51.0126 | 2025-09-09 11:30:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 138.7 |
| 9187b2b4-2d8f-3ca5-9d16-43cea7fa5c78 | -20.5484 | -51.4435 | 2025-09-09 11:30:00 | GOES-19 | ITAPURA | SÃO PAULO | Brasil | 3523008 | 35 | 33 | nan | nan | nan | Mata Atlântica | 125.4 |
| a44bf6f3-2345-3d19-9ca8-33c64d3a93dd | -11.9548 | -50.9957 | 2025-09-09 11:30:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 135.6 |
| defcf68d-bc2b-342b-a441-236a6a6d9735 | -11.9739 | -50.9935 | 2025-09-09 11:30:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 149.9 |
| 93bd2192-638a-32db-bc57-96d0b4326f02 | -12.0298 | -51.0722 | 2025-09-09 11:30:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 115.1 |
| 8d1b24a1-7302-3d69-a1f9-60cd45e03b44 | -5.5504 | -45.1891 | 2025-09-09 11:30:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 98.5 |
| 1789e90a-5aba-3ad4-a71f-f30f215f9286 | -11.9735 | -51.0148 | 2025-09-09 11:30:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 75.8 |
| 7ea1dc39-683e-346a-afe2-27f41f725896 | -20.528 | -51.4475 | 2025-09-09 11:30:00 | GOES-19 | ITAPURA | SÃO PAULO | Brasil | 3523008 | 35 | 33 | nan | nan | nan | Mata Atlântica | 162.7 |
| 16c8818e-7d98-3a10-a749-bceff6a3505a | -13.937 | -48.2522 | 2025-09-09 11:40:00 | GOES-19 | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 73.8 |
| 760f28bf-20e6-3249-8e57-2d1fd7398926 | -11.9739 | -50.9935 | 2025-09-09 11:40:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 78.6 |
| 7e2079a9-91e5-3615-84a0-4e2a2355bcbc | -11.9926 | -51.0126 | 2025-09-09 11:40:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 111.0 |
| fd66e23e-a587-3a39-863c-64b01f1bcab6 | -13.0165 | -48.0326 | 2025-09-09 11:40:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 162.0 |
| 317f36ef-8ee1-3283-a62f-aef2fb59aa8c | -5.5504 | -45.1891 | 2025-09-09 11:40:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 93.5 |
| 1fcae67c-6a61-3485-9346-bd7045ff59b0 | -18.6904 | -52.594 | 2025-09-09 11:40:00 | GOES-19 | CHAPADÃO DO SUL | MATO GROSSO DO SUL | Brasil | 5002951 | 50 | 33 | nan | nan | nan | Cerrado | 366.1 |
| be847f7f-b1de-37d9-bfa5-4739d6f4043e | -12.0295 | -51.0935 | 2025-09-09 11:40:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 119.8 |
| 9bf8c1f6-8858-301f-b8db-04def2986503 | -13.0357 | -48.0298 | 2025-09-09 11:40:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 79.0 |
| a3acd60a-600f-32cb-be75-91b42cdcab18 | -12.0298 | -51.0722 | 2025-09-09 11:40:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 158.7 |
| cd44cb17-cd8c-32dd-b68a-eb571017a942 | -10.8913 | -55.693 | 2025-09-09 11:40:00 | GOES-19 | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 73.4 |
| a04a0daa-1bc3-3031-b3f8-57918e653fb4 | -17.2762 | -46.7305 | 2025-09-09 11:50:00 | GOES-19 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 86.1 |
| b5b9454d-ec0b-348c-bf32-5942af0d5df0 | -9.0931 | -45.7314 | 2025-09-09 11:50:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 67.5 |
| 54bbf824-8086-3984-a5ab-2ac24ca0b50d | -5.5504 | -45.1891 | 2025-09-09 11:50:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 90.0 |
| c5469d00-4f45-397a-afe9-e46fc35e30fd | -12.0295 | -51.0935 | 2025-09-09 11:50:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 135.3 |
| 3a6511cf-b775-3598-9b40-a7aa7a31ea63 | -11.0436 | -45.9476 | 2025-09-09 11:50:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 104.6 |
| 35c9d4a2-d97b-38e7-a489-9a51a1e92a73 | -14.5465 | -48.758 | 2025-09-09 11:50:00 | GOES-19 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 78.2 |
| 42996847-2014-35ad-bf96-ba60d90ddf02 | -7.789 | -46.0891 | 2025-09-09 11:50:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 80.2 |
| 917e2835-752f-3ded-8fea-eda11553342f | -11.9735 | -51.0148 | 2025-09-09 11:50:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 72.2 |
| 3635f106-cbf9-3bdd-b2c5-6e8fbe62fa35 | -6.2224 | -43.3693 | 2025-09-09 11:50:00 | GOES-19 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 83.6 |
| de35dd75-52dd-32a5-8ed6-d360d3db6d7d | -12.0298 | -51.0722 | 2025-09-09 11:50:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 83.9 |
| d547b0c0-91f6-37dd-8f89-a0f520497fab | -11.0245 | -45.9502 | 2025-09-09 11:50:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 85.0 |
| c0ce9ead-5ab1-397a-ac49-6548fd774c2c | -5.5506 | -45.1664 | 2025-09-09 11:50:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 73.0 |
| 9e6f9bf7-4afb-30f3-a8c0-5f7715926663 | -11.9926 | -51.0126 | 2025-09-09 11:50:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 77.8 |
| 7c7a39ae-ad07-3d7f-b0c4-092f8679fb63 | -13.0357 | -48.0298 | 2025-09-09 11:50:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 92.3 |
| d3b231f6-6e70-3679-8416-a65bc5f9a566 | -13.0165 | -48.0326 | 2025-09-09 11:50:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 122.0 |
| 406cdc88-c8f7-3671-8294-b3a6d25bbd24 | -11.9739 | -50.9935 | 2025-09-09 11:50:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 77.1 |
| 8768415a-fe31-361c-971c-b6f9fb23e5d2 | -12.2938 | -50.0121 | 2025-09-09 11:50:00 | GOES-19 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 86.4 |
| 46554e9b-bf3a-3f92-968b-bee92d7b938a | -7.5407 | -48.2303 | 2025-09-09 11:50:00 | GOES-19 | NOVA OLINDA | TOCANTINS | Brasil | 1714880 | 17 | 33 | nan | nan | nan | Cerrado | 104.7 |
| 3f73e42b-3663-3fc1-a3ad-05f7e3c3ca24 | -5.5504 | -45.1891 | 2025-09-09 12:00:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 88.0 |
| 334b2d89-68e4-328c-947c-aa8e6f82c6e5 | -6.2224 | -43.3693 | 2025-09-09 12:00:00 | GOES-19 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 88.2 |
| 47e5120e-38e5-36a1-8938-db24b2019a91 | -9.0931 | -45.7314 | 2025-09-09 12:00:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 123.7 |
| 09a201cd-cdea-33b2-918c-ae87be7bc809 | -11.4322 | -50.3504 | 2025-09-09 12:00:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 83.1 |
| 0ab18210-7697-33d0-89da-6f4353914e59 | -12.0295 | -51.0935 | 2025-09-09 12:00:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 115.6 |
| 37095cfa-33fb-30a8-a78f-9d3c7d39d333 | -9.0934 | -45.7088 | 2025-09-09 12:00:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 84.1 |
| faafa7be-e74f-3794-88fa-80ce84110386 | -10.2982 | -48.8148 | 2025-09-09 12:00:00 | GOES-19 | PARAÍSO DO TOCANTINS | TOCANTINS | Brasil | 1716109 | 17 | 33 | nan | nan | nan | Cerrado | 64.1 |
| bdb034b7-ee91-3f8d-ae8d-9bb76819bc61 | -11.9926 | -51.0126 | 2025-09-09 12:00:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 112.4 |
| 1d0460ea-e501-37eb-b472-dd731dbfa514 | -12.2938 | -50.0121 | 2025-09-09 12:00:00 | GOES-19 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 99.5 |
| ce770329-5d15-3d90-9f5e-c592aadb3b3e | -7.5407 | -48.2303 | 2025-09-09 12:00:00 | GOES-19 | NOVA OLINDA | TOCANTINS | Brasil | 1714880 | 17 | 33 | nan | nan | nan | Cerrado | 137.9 |
| de2b5020-e15e-300d-8e1f-445f32539eea | -5.5506 | -45.1664 | 2025-09-09 12:00:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 72.0 |
| 8311cf03-849d-3506-a538-33f839b3e640 | -11.4325 | -50.329 | 2025-09-09 12:00:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 76.9 |
| e23416f4-69d3-359c-bef8-252fc9fe6120 | -12.2941 | -49.9904 | 2025-09-09 12:00:00 | GOES-19 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 84.2 |
| 6fe1b879-d86b-3c27-bc58-f926b5484652 | -5.5506 | -45.1664 | 2025-09-09 12:10:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 69.7 |
| 13e2a1a7-64ff-36e1-801f-46ed7e00be63 | -13.0357 | -48.0298 | 2025-09-09 12:10:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 127.3 |
| e3047ecc-f69f-3ae0-8e60-f8081caece14 | -12.0295 | -51.0935 | 2025-09-09 12:10:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 99.8 |
| 9181dbb0-967b-3ddd-aac8-a86c0d11f0c6 | -12.2938 | -50.0121 | 2025-09-09 12:10:00 | GOES-19 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 80.9 |
| 91802398-eea1-3e0c-bc21-34f394abdd1f | -11.9926 | -51.0126 | 2025-09-09 12:10:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 234.4 |
| 9b484898-df58-3159-af95-108c7dfa6c62 | -13.9564 | -48.2493 | 2025-09-09 12:10:00 | GOES-19 | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 87.7 |
| 6e4d3367-834b-32b4-81eb-be781beda62e | -6.2224 | -43.3693 | 2025-09-09 12:10:00 | GOES-19 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 90.0 |
| ca67baec-5a7d-3d96-a4aa-901558cee19b | -11.9739 | -50.9935 | 2025-09-09 12:10:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 105.4 |
| a9302803-3729-38fc-9bda-ca7ab88548bc | -12.2941 | -49.9904 | 2025-09-09 12:10:00 | GOES-19 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 87.2 |
| a7e6313e-8da1-3eab-83a6-4cfff1c3c70b | -15.8205 | -52.2444 | 2025-09-09 12:10:00 | GOES-19 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 126.2 |
| 3276f81f-4519-393e-811d-3bd638733aab | -9.0934 | -45.7088 | 2025-09-09 12:10:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 118.3 |
| bed11152-5e8a-344c-b9a5-d0db99fab57e | -13.9375 | -48.2299 | 2025-09-09 12:10:00 | GOES-19 | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 64.6 |
| eb5cca8c-6283-3f48-ac12-d028a5451af7 | -11.0436 | -45.9476 | 2025-09-09 12:10:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 157.8 |
| 3802b97d-dd10-3ded-a39d-89168399a259 | -9.0931 | -45.7314 | 2025-09-09 12:10:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 137.0 |
| 64ee5ff3-e9e4-38b9-813c-eada03d8a0a4 | -15.2686 | -53.7801 | 2025-09-09 12:10:00 | GOES-19 | NOVO SÃO JOAQUIM | MATO GROSSO | Brasil | 5106281 | 51 | 33 | nan | nan | nan | Cerrado | 92.9 |
| 3e0032a1-0127-32c9-8f75-eca96b1ded41 | -13.0165 | -48.0326 | 2025-09-09 12:10:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 83.7 |
| b974b6c4-3129-3ce5-ae5f-88d8777ef7f6 | -14.5465 | -48.758 | 2025-09-09 12:10:00 | GOES-19 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 84.4 |
| 15ec0840-ca7d-3026-b18a-9b4197efd88e | -7.789 | -46.0891 | 2025-09-09 12:10:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 156.2 |
| dfc75a6a-587e-33f6-9676-76b48752eae2 | -13.937 | -48.2522 | 2025-09-09 12:10:00 | GOES-19 | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 72.5 |
| 520ecde0-54d1-374f-9b44-fd7b7e7d01d9 | -11.0245 | -45.9502 | 2025-09-09 12:10:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 91.8 |
| 34e53ef4-6456-3b8a-83cd-7feb23f616d7 | -11.9923 | -51.034 | 2025-09-09 12:10:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 94.2 |
| 71bed312-762d-3946-8803-981ca1bbe59c | -10.2982 | -48.8148 | 2025-09-09 12:10:00 | GOES-19 | PARAÍSO DO TOCANTINS | TOCANTINS | Brasil | 1716109 | 17 | 33 | nan | nan | nan | Cerrado | 73.8 |
| f814b579-fee7-345b-9161-e0779e9f32e3 | -15.2492 | -53.7826 | 2025-09-09 12:10:00 | GOES-19 | NOVO SÃO JOAQUIM | MATO GROSSO | Brasil | 5106281 | 51 | 33 | nan | nan | nan | Cerrado | 71.2 |
| 38bd5ce6-bbf2-3a67-a5d9-629f4ecb7c67 | -5.5504 | -45.1891 | 2025-09-09 12:10:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 74.6 |
| 814d4c0a-170a-3f66-8e24-5aa4d6bfea55 | -11.9735 | -51.0148 | 2025-09-09 12:10:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 83.1 |
| 34bf7160-3b4d-39c6-aafd-e1c070b0e110 | -11.3018 | -46.4792 | 2025-09-09 12:20:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 121.0 |
| d2c684f8-6e4a-3b9f-b886-833ba15c799c | -13.937 | -48.2522 | 2025-09-09 12:20:00 | GOES-19 | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 85.8 |
| ff2deff3-e5e5-322a-b5a7-a232f45a3d89 | -11.9926 | -51.0126 | 2025-09-09 12:20:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 132.7 |


[Clique aqui para ver as próximas entradas](README75.md)
