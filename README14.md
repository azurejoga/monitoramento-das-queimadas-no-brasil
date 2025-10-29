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

## Dados Diários - Página 14

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 67245ae4-2902-3215-8885-a38431806f0c | -13.04406 | -43.82592 | 2025-10-29 03:55:00 | NOAA-21 | SANTANA | BAHIA | Brasil | 2928208 | 29 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 3fe097c7-96ff-3ca5-b3ca-8cf4e8abf94b | -9.7997 | -47.75642 | 2025-10-29 03:55:00 | NOAA-21 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 4.4 |
| b5baae56-a843-3097-90ed-6c24dcb19ac9 | -9.80694 | -47.75862 | 2025-10-29 03:55:00 | NOAA-21 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 4.2 |
| aaa7231c-bc1b-3f67-8774-07993dcbb938 | -12.00658 | -46.76223 | 2025-10-29 03:55:00 | NOAA-21 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| bfc64ce6-3db0-336f-8282-b030a27b5779 | -9.92928 | -47.66763 | 2025-10-29 03:55:00 | NOAA-21 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 07feec5f-d983-3634-b830-cd7fa736c84d | -10.90983 | -48.00199 | 2025-10-29 03:55:00 | NOAA-21 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 5104356f-a289-3d8d-b3aa-c1e46131609a | -10.94395 | -47.62192 | 2025-10-29 03:55:00 | NOAA-21 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| d4431523-c008-3024-894b-d2d9add8a29d | -9.90414 | -44.91124 | 2025-10-29 03:55:00 | NOAA-21 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 5.1 |
| e922ccf2-5115-3831-b609-48e6e7396a06 | -9.6196 | -47.7718 | 2025-10-29 03:55:00 | NOAA-21 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| dbe6a924-5631-38b1-b2ed-345e9038116b | -12.03324 | -47.02467 | 2025-10-29 03:55:00 | NOAA-21 | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 04245ac9-23c1-3c80-bff7-06a1f9b7ff88 | -14.31368 | -48.01517 | 2025-10-29 03:55:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 4f6fbf00-b4fc-32d4-8b87-5bd1c6d2b7d5 | -15.27134 | -43.17968 | 2025-10-29 03:55:00 | NOAA-21 | CATUTI | MINAS GERAIS | Brasil | 3115474 | 31 | 33 | nan | nan | nan | Caatinga | 0.9 |
| a48623b6-7663-33cf-9a74-79fb2bbefdc2 | -13.58085 | -49.59789 | 2025-10-29 03:55:00 | NOAA-21 | BONÓPOLIS | GOIÁS | Brasil | 5203575 | 52 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 50f36240-3108-32c3-9fe0-f439d24593d6 | -13.57998 | -49.60222 | 2025-10-29 03:55:00 | NOAA-21 | BONÓPOLIS | GOIÁS | Brasil | 5203575 | 52 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 8a0d3084-acae-3d22-974d-5e06234dba19 | -12.37033 | -50.16259 | 2025-10-29 03:55:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 3.6 |
| cd5412d2-7fef-3ab5-8b5e-350a4fcc2526 | -10.5647 | -49.83376 | 2025-10-29 03:55:00 | NOAA-21 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 00074653-7c05-3ce0-b95f-008a794c71d8 | -10.51036 | -47.73103 | 2025-10-29 03:55:00 | NOAA-21 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 57cea929-ec48-302e-b1f6-ac24905cd9f1 | -12.6971 | -46.32785 | 2025-10-29 03:55:00 | NOAA-21 | AURORA DO TOCANTINS | TOCANTINS | Brasil | 1702703 | 17 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 5c928308-01ba-3a64-a805-4db2ee71c3e5 | -13.91511 | -48.46058 | 2025-10-29 03:55:00 | NOAA-21 | CAMPINAÇU | GOIÁS | Brasil | 5204656 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 9b6b598c-2bee-3f61-976b-2feeab94320c | -15.64674 | -42.91292 | 2025-10-29 03:55:00 | NOAA-21 | PORTEIRINHA | MINAS GERAIS | Brasil | 3152204 | 31 | 33 | nan | nan | nan | Cerrado | 11.8 |
| fa7f4172-1bf8-33cb-841f-e8f2427d3543 | -14.2363 | -48.1111 | 2025-10-29 03:55:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 3.8 |
| e74177d5-b65f-344d-a7a0-a59be4abe059 | -10.50647 | -47.72379 | 2025-10-29 03:55:00 | NOAA-21 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| b31877f0-4ff5-314b-b656-6aa85f1ca073 | -11.3768 | -51.36828 | 2025-10-29 03:55:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 9474728d-4cd3-350e-b175-4e406ff52f2e | -13.64532 | -47.03349 | 2025-10-29 03:55:00 | NOAA-21 | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 0fda024c-dd75-30af-8bdb-f8ce508040f1 | -12.10703 | -44.59809 | 2025-10-29 03:55:00 | NOAA-21 | ANGICAL | BAHIA | Brasil | 2901403 | 29 | 33 | nan | nan | nan | Cerrado | 2.7 |
| c30de2fd-1436-3225-af9a-fe656f20d1cf | -10.57048 | -49.83489 | 2025-10-29 03:55:00 | NOAA-21 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| fe83afa1-7e71-3702-b773-6d232210e3fc | -10.9688 | -50.25315 | 2025-10-29 03:55:00 | NOAA-21 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| b2e467d0-7bd0-34ec-aad8-ca2a580966c7 | -13.0325 | -46.73569 | 2025-10-29 03:55:00 | NOAA-21 | CAMPOS BELOS | GOIÁS | Brasil | 5204904 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 2fcaf35f-9584-3ee6-b8e5-6cebc8495c4e | -12.69619 | -46.30799 | 2025-10-29 03:55:00 | NOAA-21 | AURORA DO TOCANTINS | TOCANTINS | Brasil | 1702703 | 17 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 14386fe8-9126-3367-b309-24b9bf12d004 | -10.95822 | -49.66707 | 2025-10-29 03:55:00 | NOAA-21 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 9bf4d39a-6d77-365f-9a7f-551e33d46259 | -13.21434 | -47.0593 | 2025-10-29 03:55:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 8bad3ff1-2b33-3183-ba14-cc7f1aab9f80 | -15.17548 | -47.23282 | 2025-10-29 03:55:00 | NOAA-21 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 34595ec1-59e0-38e6-af51-ef2aadc23220 | -9.92875 | -47.67059 | 2025-10-29 03:55:00 | NOAA-21 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 8df0fc45-0b29-3e11-95a0-9912e7ecd968 | -14.26411 | -48.12362 | 2025-10-29 03:55:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.9 |
| f1d11f11-6e24-3800-8838-dfc7b59da204 | -10.84083 | -44.41936 | 2025-10-29 03:55:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 3.1 |
| dc6f40ca-f421-350b-b8e0-36edfd828417 | -14.13114 | -44.06837 | 2025-10-29 03:55:00 | NOAA-21 | FEIRA DA MATA | BAHIA | Brasil | 2910776 | 29 | 33 | nan | nan | nan | Cerrado | 7.9 |
| 753ab7cd-d25b-33ae-9674-0717c10e4e4c | -10.54619 | -45.04691 | 2025-10-29 03:55:00 | NOAA-21 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| efcd2bdf-3723-3c14-85ca-f86c729cdcc2 | -12.01404 | -46.77374 | 2025-10-29 03:55:00 | NOAA-21 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 6.9 |
| fd1ca320-32f6-322d-94db-39d5d710e9c2 | -14.24111 | -48.11231 | 2025-10-29 03:55:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 5fb4fda5-41d3-3dc7-aa5e-8585d493b559 | -13.63634 | -46.52514 | 2025-10-29 03:55:00 | NOAA-21 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 20.6 |
| 583a6a9b-a74e-349c-aff8-d3d89b2329d7 | -10.65699 | -47.99577 | 2025-10-29 03:55:00 | NOAA-21 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 6.7 |
| 2f35f6af-f935-3ee2-a1d5-3f35df3ecb8f | -11.14754 | -47.77769 | 2025-10-29 03:55:00 | NOAA-21 | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 905f582a-1249-3a09-8920-c9832995128f | -10.64196 | -45.245 | 2025-10-29 03:55:00 | NOAA-21 | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| de2c3587-3e00-39cc-88eb-80966515d65a | -10.94088 | -47.80597 | 2025-10-29 03:55:00 | NOAA-21 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 04c9f383-3544-3148-a6d0-05cb7002c38c | -12.13868 | -45.20441 | 2025-10-29 03:55:00 | NOAA-21 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| fe4a27af-f7e8-3bc6-ac15-1ad3b848faf0 | -13.32386 | -47.45078 | 2025-10-29 03:55:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 175ef983-0430-3cd6-9e6a-dd763fae12bb | -9.05764 | -45.05488 | 2025-10-29 03:55:00 | NOAA-21 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 501fc0e8-c149-3a6b-bf50-274cb4ee7e0c | -14.51706 | -47.96339 | 2025-10-29 03:55:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| b62abd76-fc61-3ca9-bd43-6f0209c7e117 | -14.32652 | -46.52492 | 2025-10-29 03:55:00 | NOAA-21 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 848647b4-bede-37aa-b37f-55cebaba7154 | -10.98647 | -47.72781 | 2025-10-29 03:55:00 | NOAA-21 | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| b61c4513-7e08-399a-8833-bf2b6268fff3 | -9.92533 | -47.12249 | 2025-10-29 03:55:00 | NOAA-21 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 12.7 |
| 730aee1c-c4a7-3118-bb18-7d3b165c4b00 | -10.8538 | -47.88908 | 2025-10-29 03:55:00 | NOAA-21 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 25885dfa-f783-3d9f-aaac-0ba3ffc2986e | -10.86257 | -50.09637 | 2025-10-29 03:55:00 | NOAA-21 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 6.8 |
| f2b4c74b-b7ea-364b-ad6c-f2a0f67ffd66 | -11.7373 | -49.33056 | 2025-10-29 03:55:00 | NOAA-21 | DUERÉ | TOCANTINS | Brasil | 1707306 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 48902db9-ce21-37ca-adf1-f0c9a88d0d81 | -10.56889 | -49.84321 | 2025-10-29 03:55:00 | NOAA-21 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 6.1 |
| c3e679cc-98fb-3071-8fa7-e21fb572e144 | -14.98726 | -47.86489 | 2025-10-29 03:55:00 | NOAA-21 | ÁGUA FRIA DE GOIÁS | GOIÁS | Brasil | 5200175 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 0c5661c5-6f74-3c4d-aa46-7d43a184b111 | -9.8978 | -44.89775 | 2025-10-29 03:55:00 | NOAA-21 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 8a12d789-69ed-3c90-b11e-628e3ed5aec8 | -10.22515 | -45.94292 | 2025-10-29 03:55:00 | NOAA-21 | BARREIRAS DO PIAUÍ | PIAUÍ | Brasil | 2201309 | 22 | 33 | nan | nan | nan | Cerrado | 4.5 |
| a5108209-1ac2-33af-9be1-4c489cd95ad2 | -14.49749 | -47.88429 | 2025-10-29 03:55:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| e578270d-0050-3593-9459-14cf15a927f3 | -9.49639 | -46.98425 | 2025-10-29 03:55:00 | NOAA-21 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 3190df08-95f3-352a-9040-ab80be1adf65 | -11.94324 | -44.30673 | 2025-10-29 03:55:00 | NOAA-21 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| b6c64ad7-848f-3730-afa5-685a2885c306 | -13.91565 | -48.45781 | 2025-10-29 03:55:00 | NOAA-21 | CAMPINAÇU | GOIÁS | Brasil | 5204656 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 8b47e10a-eead-3003-ae5a-bd5205391e90 | -12.20666 | -46.5235 | 2025-10-29 03:55:00 | NOAA-21 | TAGUATINGA | TOCANTINS | Brasil | 1720903 | 17 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 7ce93b08-44fd-3fb8-9cea-78deb910b5ca | -11.05618 | -45.36417 | 2025-10-29 03:55:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 7f9273de-85f2-36d7-9bde-1694450e86a9 | -13.93445 | -48.44112 | 2025-10-29 03:55:00 | NOAA-21 | CAMPINAÇU | GOIÁS | Brasil | 5204656 | 52 | 33 | nan | nan | nan | Cerrado | 5.0 |
| ddf23fe8-a747-3385-b915-46ab52063dbd | -13.60965 | -46.49694 | 2025-10-29 03:55:00 | NOAA-21 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 287f326e-aad9-349c-bcba-c148e961fc90 | -13.6349 | -46.4596 | 2025-10-29 03:55:00 | NOAA-21 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 2b1da9f4-3b1e-3857-a91b-00716b311666 | -9.09145 | -47.81464 | 2025-10-29 03:55:00 | NOAA-21 | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 0af84d91-0ef8-35ef-95c8-a8412ef62d67 | -12.18492 | -46.71656 | 2025-10-29 03:55:00 | NOAA-21 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 7.2 |
| 2f203730-70f1-3489-aaee-7936031149f2 | -8.72442 | -49.76667 | 2025-10-29 03:55:00 | NOAA-21 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 34f3d28e-3d52-389d-86db-c4e5ef491796 | -10.62192 | -47.8849 | 2025-10-29 03:55:00 | NOAA-21 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 7c1fb3d6-9876-3d2b-ab19-4900cc77cf18 | -10.03516 | -47.13158 | 2025-10-29 03:55:00 | NOAA-21 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 11.2 |
| a4c9660a-dde1-3cb6-b4bb-10d35eaa5307 | -12.94611 | -46.53469 | 2025-10-29 03:55:00 | NOAA-21 | NOVO ALEGRE | TOCANTINS | Brasil | 1715150 | 17 | 33 | nan | nan | nan | Cerrado | 3.7 |
| ff092832-6f48-3326-9ffd-8a771fdc6fca | -13.32753 | -47.48272 | 2025-10-29 03:55:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 5040e618-c1a7-36b1-a70c-fbf7ec38cf31 | -9.90061 | -44.9065 | 2025-10-29 03:55:00 | NOAA-21 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 71425c7e-93f9-3c66-aa31-9a01d369d6c2 | -11.35647 | -47.02079 | 2025-10-29 03:55:00 | NOAA-21 | PORTO ALEGRE DO TOCANTINS | TOCANTINS | Brasil | 1718006 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 4a430f9b-360d-3b5b-b431-e153154a87a3 | -10.51656 | -47.7258 | 2025-10-29 03:55:00 | NOAA-21 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 72a1cae7-e20d-320e-aeb4-c2fe157558ad | -14.52425 | -48.00416 | 2025-10-29 03:55:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 632a28c6-7b36-3547-8fcf-b89293540d0f | -14.23835 | -43.00895 | 2025-10-29 03:55:00 | NOAA-21 | GUANAMBI | BAHIA | Brasil | 2911709 | 29 | 33 | nan | nan | nan | Caatinga | 1.5 |
| dd2097ba-a248-3f66-9b82-069d4bb322bc | -12.18402 | -46.72138 | 2025-10-29 03:55:00 | NOAA-21 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 7.2 |
| ffe9acc2-8daa-3ac0-b2e8-370a83e495aa | -15.63745 | -42.99002 | 2025-10-29 03:55:00 | NOAA-21 | PORTEIRINHA | MINAS GERAIS | Brasil | 3152204 | 31 | 33 | nan | nan | nan | Cerrado | 10.2 |
| 2432f01d-100a-39f0-a3ce-52ee6f6fb602 | -10.84814 | -47.89127 | 2025-10-29 03:55:00 | NOAA-21 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| a5bb8b71-6540-3b21-b873-70c6ce971d82 | -11.25537 | -45.46871 | 2025-10-29 03:55:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 6.2 |
| c1d23d9f-d0a5-34b0-962f-b9842165b5c1 | -10.92025 | -47.61086 | 2025-10-29 03:55:00 | NOAA-21 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 2add74c9-ca3d-3da4-92b5-4af39354ea5c | -10.77871 | -44.76944 | 2025-10-29 03:55:00 | NOAA-21 | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 8eda6550-b96e-3154-9297-0efff171abaa | -10.65825 | -47.90452 | 2025-10-29 03:55:00 | NOAA-21 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 51a74e03-a4fd-307f-8723-ab5b79e5571b | -10.64436 | -48.00639 | 2025-10-29 03:55:00 | NOAA-21 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 8.4 |
| 4e56c0ca-25c1-3556-99ca-9a61a230ff54 | -14.31478 | -48.00951 | 2025-10-29 03:55:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 054e4e6c-ce84-3517-9db2-1e3afddd3618 | -9.45062 | -46.88891 | 2025-10-29 03:55:00 | NOAA-21 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 86911cbb-cbd3-340e-ae68-c03d8b81bed7 | -8.71893 | -47.98762 | 2025-10-29 03:55:00 | NOAA-21 | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 2d6b2b19-d978-3ce7-86eb-cd27a3a9ab4b | -14.1451 | -47.06858 | 2025-10-29 03:55:00 | NOAA-21 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 12bf5d4c-8b01-3b35-84ba-40bfb161671c | -13.6397 | -46.50713 | 2025-10-29 03:55:00 | NOAA-21 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 44b7220b-355d-398f-a891-1231c03fc4b0 | -10.90909 | -47.8084 | 2025-10-29 03:55:00 | NOAA-21 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 5bb2d56e-1212-3092-91ce-d4d7a304d3e0 | -10.76534 | -47.82823 | 2025-10-29 03:55:00 | NOAA-21 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 869f8d6e-37d5-398b-bca0-9953cce087a4 | -10.03556 | -47.14053 | 2025-10-29 03:55:00 | NOAA-21 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 58dda7ec-e864-348f-9044-06987f95625c | -13.41972 | -47.38233 | 2025-10-29 03:55:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.9 |
| ffe7722b-223f-3b6e-84ec-013f2119126c | -12.19319 | -46.72314 | 2025-10-29 03:55:00 | NOAA-21 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 15.7 |
| d42dbdd2-c615-34c5-a07c-bd466a6d2d9a | -13.70081 | -47.67658 | 2025-10-29 03:55:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 3e1a0cb3-a3dc-32c8-84bc-1c496dba2fb9 | -14.62231 | -45.00286 | 2025-10-29 03:55:00 | NOAA-21 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| d691c442-3a3d-321c-b814-c195b8c7add2 | -10.74881 | -44.75578 | 2025-10-29 03:55:00 | NOAA-21 | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |


[Clique aqui para ver as próximas entradas](README15.md)
