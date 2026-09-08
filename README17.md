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

## Dados Diários - Página 17

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| c26c57c8-87f3-3200-a0d8-fd642a859d4e | -9.72862 | -43.47884 | 2026-09-08 04:46:00 | NPP-375D | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| e53e6a6d-7458-352f-a3aa-0ae5290fceb4 | -11.31682 | -45.07772 | 2026-09-08 04:46:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.7 |
| ab85c876-ce90-3393-8270-cf5d52ef997d | -9.74539 | -43.50736 | 2026-09-08 04:46:00 | NPP-375D | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 2.5 |
| ed929840-d5d5-382f-ab0e-d8d83f1548a4 | -11.94507 | -49.74141 | 2026-09-08 04:46:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 31b6e591-c7c8-3696-9283-ad115d61f3ae | -9.72505 | -43.47461 | 2026-09-08 04:46:00 | NPP-375D | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| ac579a92-b275-3c81-b8bc-5ccc1038ded6 | -11.31861 | -45.09217 | 2026-09-08 04:46:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 1a506129-99b0-3cd9-9f89-6614c4f5b308 | -13.25051 | -61.71098 | 2026-09-08 04:46:00 | NPP-375D | CEREJEIRAS | RONDÔNIA | Brasil | 1100056 | 11 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 70143c31-0c21-38f5-81bd-aba84b6527f2 | -9.7118 | -43.42044 | 2026-09-08 04:46:00 | NPP-375D | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Caatinga | 10.9 |
| 6344dab2-4d0b-311b-baa7-a464ff7bafb7 | -11.36682 | -45.73574 | 2026-09-08 04:46:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 8a50e983-4b03-30ef-a81f-5ade58b1b424 | -9.74027 | -43.514 | 2026-09-08 04:46:00 | NPP-375D | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 2.8 |
| dd80cfbe-65b9-356a-ac29-dabde1aa6525 | -13.22859 | -61.71254 | 2026-09-08 04:46:00 | NPP-375D | CEREJEIRAS | RONDÔNIA | Brasil | 1100056 | 11 | 33 | nan | nan | nan | Amazônia | 1.5 |
| ef70ec2a-f561-3e25-b03f-69d7dcd5796d | -14.28446 | -42.69254 | 2026-09-08 04:46:00 | NPP-375D | GUANAMBI | BAHIA | Brasil | 2911709 | 29 | 33 | nan | nan | nan | Caatinga | 2.1 |
| ca20d044-2598-3db0-b094-6201f439521a | -13.21486 | -61.7149 | 2026-09-08 04:46:00 | NPP-375D | CEREJEIRAS | RONDÔNIA | Brasil | 1100056 | 11 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 9fc13df0-fe8e-3aba-90dd-0db7b9318918 | -9.98279 | -43.43943 | 2026-09-08 04:46:00 | NPP-375D | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 8adf678b-b9f6-39f6-8a68-d19090c812cf | -14.28371 | -42.69426 | 2026-09-08 04:46:00 | NPP-375D | GUANAMBI | BAHIA | Brasil | 2911709 | 29 | 33 | nan | nan | nan | Caatinga | 2.4 |
| 1ecabfc9-4d6f-31aa-9bd5-fc541cc6910e | -8.86101 | -49.73951 | 2026-09-08 04:46:00 | NPP-375D | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 0bb8ef19-af70-38c3-883e-3a22a06eb81f | -10.76683 | -60.78861 | 2026-09-08 04:46:00 | NPP-375D | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| f2060647-419b-3779-b72d-85c939680813 | -9.73723 | -43.50614 | 2026-09-08 04:46:00 | NPP-375D | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 18cccd1c-69fa-3e39-bd46-bca28e480e9c | -9.76236 | -43.47641 | 2026-09-08 04:46:00 | NPP-375D | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 3.7 |
| f216d646-9c74-3890-bea8-96598d3894e5 | -13.21665 | -61.71439 | 2026-09-08 04:46:00 | NPP-375D | CEREJEIRAS | RONDÔNIA | Brasil | 1100056 | 11 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 0d9b7cb6-eeeb-3004-bcd1-84ee22c78f03 | -9.71173 | -43.45065 | 2026-09-08 04:46:00 | NPP-375D | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| c3f39f8a-80f4-3928-9ea9-4fc981096b76 | -9.76645 | -43.47701 | 2026-09-08 04:46:00 | NPP-375D | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 0f978ad2-964e-3325-a2c1-446e25bd1087 | -6.63373 | -59.44156 | 2026-09-08 04:46:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 5.8 |
| c6e5b1c3-cea8-30c1-a6d5-4e819c85cd02 | -9.70611 | -43.46093 | 2026-09-08 04:46:00 | NPP-375D | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 65892bef-64f9-3d37-81c1-6a28e5493860 | -6.76743 | -59.43307 | 2026-09-08 04:46:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| d240cdde-554c-3b9e-9d87-793932a61748 | -9.76078 | -43.48734 | 2026-09-08 04:46:00 | NPP-375D | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 7995097e-2190-3496-8912-561fe2fcb58c | -9.76539 | -43.48431 | 2026-09-08 04:46:00 | NPP-375D | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| dbdfb93d-db54-32bd-90d9-d7ad34e10980 | -14.91563 | -44.67231 | 2026-09-08 04:46:00 | NPP-375D | CÔNEGO MARINHO | MINAS GERAIS | Brasil | 3117836 | 31 | 33 | nan | nan | nan | Cerrado | 7.4 |
| af483d90-d17d-3279-a371-3f612b01601a | -9.70711 | -43.45384 | 2026-09-08 04:46:00 | NPP-375D | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 6.4 |
| 2f4c78ce-b8eb-380f-a753-bd4f1da67925 | -9.72453 | -43.47824 | 2026-09-08 04:46:00 | NPP-375D | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| bc1228a6-56a0-31f6-825f-a11f36a40166 | -9.72766 | -43.39713 | 2026-09-08 04:46:00 | NPP-375D | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 04d0f249-debf-35e3-8bfe-5e13f0ee3e1e | -13.43885 | -43.81283 | 2026-09-08 04:46:00 | NPP-375D | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 4.9 |
| a6736aae-cbc5-365d-908b-bd46fa1ee3ad | -9.74958 | -43.47821 | 2026-09-08 04:46:00 | NPP-375D | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 6f1f259b-622a-3cbc-b12e-6431902fdf5e | -9.72044 | -43.47765 | 2026-09-08 04:46:00 | NPP-375D | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| ce931ee1-908d-3987-b718-95bb83b52c8f | -9.76592 | -43.48067 | 2026-09-08 04:46:00 | NPP-375D | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 016bb236-12b1-3f0a-90fe-eb2fa080e73d | -9.7051 | -43.4681 | 2026-09-08 04:46:00 | NPP-375D | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 7fb06355-700a-3bd5-92bb-2cc234a21ce5 | -9.74591 | -43.50372 | 2026-09-08 04:46:00 | NPP-375D | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 2.5 |
| e0e3562b-58b7-3c01-8534-8178f803efb5 | -9.74434 | -43.51464 | 2026-09-08 04:46:00 | NPP-375D | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 1daae065-7e3b-37c9-a16b-aa79139514e8 | -9.76501 | -43.45805 | 2026-09-08 04:46:00 | NPP-375D | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 3.2 |
| cce9cb26-af6d-38cb-8f0b-90d10bfaf3a5 | -9.76289 | -43.47275 | 2026-09-08 04:46:00 | NPP-375D | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 6.2 |
| d4fbd9ac-9b6e-3d85-9661-8c051f69414c | -9.7235 | -43.48553 | 2026-09-08 04:46:00 | NPP-375D | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 3.8 |
| bd71ecd1-d20c-3ebf-bac0-faa16e2c5bf0 | -9.7625 | -43.44646 | 2026-09-08 04:46:00 | NPP-375D | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 27ae06d0-3f61-3837-8551-386260c61530 | -9.72401 | -43.48188 | 2026-09-08 04:46:00 | NPP-375D | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 7877d4ca-bae7-3c16-afda-78ad6f847a46 | -9.76555 | -43.45437 | 2026-09-08 04:46:00 | NPP-375D | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 3.2 |
| e5f617b3-7a15-32eb-9411-f27da81cf115 | -9.71077 | -43.42778 | 2026-09-08 04:46:00 | NPP-375D | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Caatinga | 4.0 |
| 092e647c-0257-3b6b-a2b2-55e584065f2e | -13.27217 | -61.76535 | 2026-09-08 04:46:00 | NPP-375D | CEREJEIRAS | RONDÔNIA | Brasil | 1100056 | 11 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 9d253005-9a1e-3db1-8ad3-dc78f8a12745 | -13.23042 | -61.71198 | 2026-09-08 04:46:00 | NPP-375D | CEREJEIRAS | RONDÔNIA | Brasil | 1100056 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 8bad238d-6cef-382d-81be-91c729d1affb | -9.70762 | -43.45017 | 2026-09-08 04:46:00 | NPP-375D | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Caatinga | 3.6 |
| 1dd20387-c64e-3870-952d-9a64adb314b4 | -9.72966 | -43.47156 | 2026-09-08 04:46:00 | NPP-375D | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 678c7ceb-2d98-3604-9961-725a18d87ab5 | -9.72411 | -43.39255 | 2026-09-08 04:46:00 | NPP-375D | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Caatinga | 5.8 |
| 7d5207dd-3e9b-3e0c-aa3b-f60854bc80fd | -11.36619 | -45.73998 | 2026-09-08 04:46:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.6 |
| e127f409-95fe-371a-b80b-4cfdbe5939bb | -9.76342 | -43.46908 | 2026-09-08 04:46:00 | NPP-375D | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 6.2 |
| 265eef16-df11-3b8a-9376-7aca57125e2a | -13.22118 | -61.71635 | 2026-09-08 04:46:00 | NPP-375D | CEREJEIRAS | RONDÔNIA | Brasil | 1100056 | 11 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 07f51275-138c-3b04-b0ff-c79dc1f54472 | -8.78035 | -48.36728 | 2026-09-08 04:46:00 | NPP-375D | GUARAÍ | TOCANTINS | Brasil | 1709302 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 7ce15593-c3ca-341a-9463-b3ebe1cb1de1 | -9.76487 | -43.48795 | 2026-09-08 04:46:00 | NPP-375D | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 10a49e97-5b93-302b-bb9a-9273f0ec4941 | -14.90699 | -44.67485 | 2026-09-08 04:46:00 | NPP-375D | CÔNEGO MARINHO | MINAS GERAIS | Brasil | 3117836 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| fd850c2f-3766-345a-8394-4bf0ffed8fce | -9.7666 | -43.44707 | 2026-09-08 04:46:00 | NPP-375D | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 4.1 |
| c369a52f-facc-3328-a99d-9d2464847bf1 | -14.90244 | -44.67793 | 2026-09-08 04:46:00 | NPP-375D | CÔNEGO MARINHO | MINAS GERAIS | Brasil | 3117836 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 10f16573-ab28-3eeb-b1c6-1414363d0d81 | -9.70561 | -43.4645 | 2026-09-08 04:46:00 | NPP-375D | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 8ad3b8b9-e3f8-3c56-85aa-466657aece5c | -14.91612 | -44.66862 | 2026-09-08 04:46:00 | NPP-375D | CÔNEGO MARINHO | MINAS GERAIS | Brasil | 3117836 | 31 | 33 | nan | nan | nan | Cerrado | 7.4 |
| 381edc5e-157c-350a-9a82-10f6427c2121 | -14.80385 | -48.79116 | 2026-09-08 04:46:00 | NPP-375D | BARRO ALTO | GOIÁS | Brasil | 5203203 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| ae15a88e-8868-3ccc-a183-230fb47ac311 | -9.71845 | -43.43266 | 2026-09-08 04:46:00 | NPP-375D | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 03de223f-7ef2-3554-9247-07bcba616347 | -9.76303 | -43.44279 | 2026-09-08 04:46:00 | NPP-375D | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 3.9 |
| d731a331-5664-3b47-90a7-bb0418a6167d | -9.72758 | -43.48612 | 2026-09-08 04:46:00 | NPP-375D | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 2136d44e-ae6f-3af3-be38-e441bf74336e | -9.76671 | -43.41729 | 2026-09-08 04:46:00 | NPP-375D | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 063f78db-2ab0-33db-92ec-8240411b5a9f | -9.7282 | -43.39331 | 2026-09-08 04:46:00 | NPP-375D | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Caatinga | 4.5 |
| 8a67f833-f81b-3d0d-b45a-084aef2888db | -9.76698 | -43.47334 | 2026-09-08 04:46:00 | NPP-375D | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| f4da18eb-d564-33c6-8220-b2d841b3b98f | -9.71743 | -43.41017 | 2026-09-08 04:46:00 | NPP-375D | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Caatinga | 5.0 |
| a69607ae-caa4-33ab-924b-3e214f372730 | -20.50044 | -57.41806 | 2026-09-08 04:49:00 | NPP-375D | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Pantanal | 1.0 |
| 127fb15b-eb4b-359f-8dfd-b464b112a843 | -20.49878 | -57.42641 | 2026-09-08 04:49:00 | NPP-375D | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Pantanal | 1.0 |
| 684f814b-9ded-3c6f-bdfa-baea0031e363 | -17.09748 | -56.8715 | 2026-09-08 04:49:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.5 |
| 906b0810-949a-371c-a5d8-48d8778a0f13 | -15.83678 | -56.60862 | 2026-09-08 04:49:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 244f154d-9915-3212-b47c-777d6069dc46 | -20.49961 | -57.42224 | 2026-09-08 04:49:00 | NPP-375D | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Pantanal | 1.0 |
| d53e9723-ff98-3191-a8b0-5100e5a1664b | -16.00818 | -55.78093 | 2026-09-08 04:49:00 | NPP-375D | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 82a9a7fe-778a-3f51-8538-c74eeddb2897 | -20.49371 | -57.42966 | 2026-09-08 04:49:00 | NPP-375D | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Pantanal | 1.1 |
| 10684983-f271-3af8-803d-ed287d07f103 | -18.23461 | -47.26282 | 2026-09-08 04:49:00 | NPP-375D | COROMANDEL | MINAS GERAIS | Brasil | 3119302 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| e7414b19-0df1-3e75-810f-35314a47ea56 | -20.59374 | -57.97622 | 2026-09-08 04:49:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.9 |
| f4e892db-9f82-36d9-b521-881c865c5683 | -18.7769 | -49.43952 | 2026-09-08 04:49:00 | NPP-375D | CAPINÓPOLIS | MINAS GERAIS | Brasil | 3112604 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| a3a17e66-91c1-308f-b7e2-07c2ef99717e | -17.09313 | -56.87058 | 2026-09-08 04:49:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 0.7 |
| 44952f6e-e8f7-3824-ac5b-2ae5839bdcbe | -20.43281 | -57.43535 | 2026-09-08 04:49:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.1 |
| de7d078e-771e-31b5-8699-d01d2007343e | -16.00889 | -55.77704 | 2026-09-08 04:49:00 | NPP-375D | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| ee7f5639-e14f-3e7c-9a42-33047bc4f622 | -15.64151 | -54.1778 | 2026-09-08 04:49:00 | NPP-375D | PRIMAVERA DO LESTE | MATO GROSSO | Brasil | 5107040 | 51 | 33 | nan | nan | nan | Cerrado | 4.1 |
| bad388ca-1c4a-3633-96ac-ecac0e961507 | -20.59811 | -57.97721 | 2026-09-08 04:49:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.9 |
| 85901cb6-e8b5-3af6-801a-b25cc8e67fd5 | -23.67241 | -55.24556 | 2026-09-08 04:51:00 | NPP-375D | PARANHOS | MATO GROSSO DO SUL | Brasil | 5006358 | 50 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 8369c328-8050-3e8f-b015-f0df2a006534 | -23.67321 | -55.24115 | 2026-09-08 04:51:00 | NPP-375D | PARANHOS | MATO GROSSO DO SUL | Brasil | 5006358 | 50 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| bddf87d4-7b5d-31c4-8f52-011f870c5c15 | -22.58761 | -54.95973 | 2026-09-08 04:51:00 | NPP-375D | CAARAPÓ | MATO GROSSO DO SUL | Brasil | 5002407 | 50 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| 794d4182-9731-3aea-a310-7cd4804bd9ef | -22.58905 | -54.95787 | 2026-09-08 04:51:00 | NPP-375D | CAARAPÓ | MATO GROSSO DO SUL | Brasil | 5002407 | 50 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 9d8233be-eb31-3965-b049-e185bdd146b9 | -23.66963 | -55.24039 | 2026-09-08 04:51:00 | NPP-375D | PARANHOS | MATO GROSSO DO SUL | Brasil | 5006358 | 50 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| c77ecdaa-1a51-3f2d-a611-df4e344d04a4 | -2.88304 | -50.45108 | 2026-09-08 05:01:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 6b0db079-f10b-3791-bfc6-8277dd743827 | -2.96535 | -49.55893 | 2026-09-08 05:01:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 4fa23ea0-6469-3366-882a-2ce1ab364286 | -2.30709 | -48.57905 | 2026-09-08 05:01:00 | NOAA-20 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 03d2454c-7205-3711-8475-cffa8e70aa0f | 1.0696 | -52.49839 | 2026-09-08 05:01:00 | NOAA-20 | PEDRA BRANCA DO AMAPARI | AMAPÁ | Brasil | 1600154 | 16 | 33 | nan | nan | nan | Amazônia | 0.6 |
| d4a313e8-8297-3b3d-ade2-f587563ca529 | -1.61424 | -54.90405 | 2026-09-08 05:01:00 | NOAA-20 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| d69374e7-36a8-3a88-9107-4973e9121f4f | -3.06718 | -49.52441 | 2026-09-08 05:01:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| d6968dbe-21b4-3743-bc5e-13e007c96655 | -1.20071 | -55.73617 | 2026-09-08 05:01:00 | NOAA-20 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| ee5f442b-e0ad-3690-b2d4-1164dcb8786e | -1.56268 | -55.25198 | 2026-09-08 05:01:00 | NOAA-20 | CURUÁ | PARÁ | Brasil | 1502855 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 7d768e8a-424e-3304-afd8-33283df7098b | -2.87813 | -50.4588 | 2026-09-08 05:01:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 5cfc403a-a979-33c9-8f99-f4b84babed39 | -1.47667 | -54.8462 | 2026-09-08 05:01:00 | NOAA-20 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 749cf084-ac4c-33bd-a3f5-db57596bb510 | -1.61231 | -55.44694 | 2026-09-08 05:01:00 | NOAA-20 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 417c33bb-bbfa-3dc3-a38a-278369e13630 | -1.19351 | -55.70785 | 2026-09-08 05:01:00 | NOAA-20 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |


[Clique aqui para ver as próximas entradas](README18.md)
