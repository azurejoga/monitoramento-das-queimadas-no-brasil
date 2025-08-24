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

## Dados Diários - Página 55

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| b3345ae5-6f46-30b5-bd95-18fdbdb779dd | -9.18086 | -59.65685 | 2025-08-24 04:59:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 87903589-69d2-3ead-8e0a-2c92e71d5e6a | -8.85862 | -52.05059 | 2025-08-24 04:59:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 8fc5f83d-2e13-37f2-8f96-b901ef374f17 | -7.44458 | -57.62151 | 2025-08-24 04:59:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| fba78487-ebd8-31c6-b29f-938c06b4b328 | -8.91929 | -62.43546 | 2025-08-24 04:59:00 | NPP-375D | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 37947442-44f1-3312-b86b-6d667de70c7d | -9.22718 | -59.75227 | 2025-08-24 04:59:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 7dae9585-d4d8-331d-b549-3df8e1eca200 | -8.896 | -62.42574 | 2025-08-24 04:59:00 | NPP-375D | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 0219a999-0bbd-37ba-acc5-66742b98435b | -7.57105 | -63.44428 | 2025-08-24 04:59:00 | NPP-375D | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 1811c931-f5b9-3fc2-96d1-bce75f9090cc | -9.1586 | -59.50035 | 2025-08-24 04:59:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 08051f3f-1a31-3fd1-9405-352481ab65e8 | -9.20574 | -60.78748 | 2025-08-24 04:59:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 14.9 |
| bf185275-7c85-339b-bec3-d84044845d48 | -8.91247 | -62.41765 | 2025-08-24 04:59:00 | NPP-375D | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 5.2 |
| 00ffe4de-0d5d-3f7c-988b-ab588ac36b41 | -9.57454 | -55.3614 | 2025-08-24 04:59:00 | NPP-375D | NOVO MUNDO | MATO GROSSO | Brasil | 5106265 | 51 | 33 | nan | nan | nan | Amazônia | 0.1 |
| f5ba28b6-7b99-34eb-8e68-6f3131828b56 | -8.83841 | -49.90007 | 2025-08-24 04:59:00 | NPP-375D | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 2df79fae-5f27-3b7c-add5-3a106a61e574 | -9.17475 | -60.8117 | 2025-08-24 04:59:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 98a8dd52-0746-36bb-9443-f1576534bee9 | -10.80921 | -46.41287 | 2025-08-24 04:59:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 5909c74e-fdd4-3abb-81a0-7e0b13e7a69d | -8.13292 | -62.8663 | 2025-08-24 04:59:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 2bf50af0-769a-3860-b8d7-18854d355459 | -9.25161 | -59.63617 | 2025-08-24 04:59:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 14aaf206-eb28-37a3-a491-d467d84003ef | -9.02584 | -59.01335 | 2025-08-24 04:59:00 | NPP-375D | COTRIGUAÇU | MATO GROSSO | Brasil | 5103379 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 7253e7c5-1496-3d66-9bb2-c0ee7b321f00 | -11.31441 | -47.85752 | 2025-08-24 04:59:00 | NPP-375D | SANTA ROSA DO TOCANTINS | TOCANTINS | Brasil | 1718907 | 17 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 4dc18984-6ecc-39bd-a7d2-583847df18cf | -9.1493 | -59.44881 | 2025-08-24 04:59:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 28d3b4a3-1d72-311e-b131-0a99b3f2d4a5 | -9.14975 | -59.5041 | 2025-08-24 04:59:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 8127c95f-f0fc-37ab-80c7-6d3bdcae77da | -9.67885 | -48.34579 | 2025-08-24 04:59:00 | NPP-375D | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| b7cbc5b8-8823-39c4-a8f1-6d0989d30d5c | -8.62835 | -62.6284 | 2025-08-24 04:59:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 5.7 |
| ff928501-bc79-35ca-bc8b-aa91fc2e34b5 | -8.23732 | -47.46201 | 2025-08-24 04:59:00 | NPP-375D | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| d96d12f0-2c1b-332d-a3ee-9f1dabcf6627 | -8.06014 | -44.99258 | 2025-08-24 04:59:00 | NPP-375D | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 2ad74f0d-9f46-3aa8-8e00-ea9586c22b2b | -8.91832 | -62.44089 | 2025-08-24 04:59:00 | NPP-375D | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 1622c7f1-d600-36f0-ad25-23979469da90 | -9.15028 | -59.47771 | 2025-08-24 04:59:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 6.3 |
| a60007f2-c4ce-368c-b182-98ba567f68ab | -8.22335 | -45.11383 | 2025-08-24 04:59:00 | NPP-375D | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 2fe857e4-15f7-3223-94fe-f5b39ebf10b1 | -9.24222 | -60.47808 | 2025-08-24 04:59:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 4aa7bcc6-b2c6-36ab-aa93-fff24d3d8d67 | -5.80332 | -59.21803 | 2025-08-24 04:59:00 | NPP-375D | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 82f6d50a-11d2-32cb-adff-3e3c1790b541 | -9.2196 | -59.62326 | 2025-08-24 04:59:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 26e5510a-8193-307e-acc6-15a325d19dc3 | -8.90181 | -62.42127 | 2025-08-24 04:59:00 | NPP-375D | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 1.6 |
| eee6f13d-508c-3535-b7d4-4a6a704d2d00 | -8.21663 | -45.08052 | 2025-08-24 04:59:00 | NPP-375D | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 7d62be7d-bf5f-3157-b19f-213ea1e4a539 | -9.15206 | -59.48097 | 2025-08-24 04:59:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 69c83839-db70-3242-bcf1-37b22de646ad | -5.79384 | -59.22422 | 2025-08-24 04:59:00 | NPP-375D | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| fd8eec91-3056-37bb-b4d6-6daa17e44ae5 | -6.57953 | -59.8731 | 2025-08-24 04:59:00 | NPP-375D | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 1ce12470-0c08-36c1-96d4-4057031ec8df | -8.04282 | -44.99707 | 2025-08-24 04:59:00 | NPP-375D | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| db7fce8e-607c-3ccd-b810-8efc62944867 | -9.25328 | -48.19313 | 2025-08-24 04:59:00 | NPP-375D | PEDRO AFONSO | TOCANTINS | Brasil | 1716505 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 129e5bc7-47d0-3e77-95e5-318369a872c3 | -9.15344 | -59.49712 | 2025-08-24 04:59:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 5.7 |
| 62d04f1e-7440-3973-8f65-84dde27e63e6 | -5.81029 | -59.22697 | 2025-08-24 04:59:00 | NPP-375D | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| f21a445c-d2a9-320a-8c42-9ebd44c97b65 | -9.13112 | -60.77522 | 2025-08-24 04:59:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 5b8c2421-cb24-3c73-b589-04abbfbffcfe | -8.92899 | -60.7202 | 2025-08-24 04:59:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.3 |
| 8c79428d-05a6-3dde-8ac4-f471e2c2e05a | -9.62241 | -48.32718 | 2025-08-24 04:59:00 | NPP-375D | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 4.5 |
| f1ef94ff-00ab-3717-be0c-6ccf026f3832 | -11.31505 | -47.85273 | 2025-08-24 04:59:00 | NPP-375D | SANTA ROSA DO TOCANTINS | TOCANTINS | Brasil | 1718907 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 9f609025-5524-354d-8520-76398cec17ad | -9.15171 | -59.50743 | 2025-08-24 04:59:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 81c8e1de-4ae6-38ff-a116-ee2cfb7c9b33 | -8.21581 | -45.11748 | 2025-08-24 04:59:00 | NPP-375D | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 04fa458a-98fb-34c1-a097-8105bb141465 | -9.17676 | -59.46644 | 2025-08-24 04:59:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 5444b4b4-0bc1-31f7-bf63-a12f05221bdf | -7.55979 | -63.85517 | 2025-08-24 04:59:00 | NPP-375D | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 549a5fcf-f01d-38f7-bd44-a0c76f881c3e | -7.80669 | -62.3391 | 2025-08-24 04:59:00 | NPP-375D | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 75f3947e-bfe6-32d4-a48b-65103ab359fc | -9.02762 | -47.6461 | 2025-08-24 04:59:00 | NPP-375D | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 6.5 |
| e243b94a-7993-3fcf-8935-ae8a8affab45 | -10.30118 | -46.7538 | 2025-08-24 04:59:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| c56b8e21-e8b5-310e-947d-f31dd91f47dc | -10.60319 | -50.15108 | 2025-08-24 04:59:00 | NPP-375D | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 296ddfc0-0990-37af-8f5b-88b4f755bdba | -8.13346 | -62.86335 | 2025-08-24 04:59:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.4 |
| e1818cbb-0d44-3983-8baa-569bee463d0b | -5.61926 | -60.23621 | 2025-08-24 04:59:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 486cb411-c2ff-3d22-9d02-484f2ed7278f | -8.14303 | -62.86817 | 2025-08-24 04:59:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 13212330-0bf5-3205-82b8-19cf95ba6cd5 | -9.1524 | -59.45462 | 2025-08-24 04:59:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 7.5 |
| f89193f5-d453-3d53-9c3e-7adcd8b205c2 | -9.21154 | -59.47789 | 2025-08-24 04:59:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 4b592a34-09a7-3a50-8528-1b794064e1f1 | -5.80271 | -59.22173 | 2025-08-24 04:59:00 | NPP-375D | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| da4ed19f-d9d3-3644-aaa5-11dae1729d79 | -8.2162 | -45.08379 | 2025-08-24 04:59:00 | NPP-375D | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 69d651cf-e25e-3aaa-8706-fb83f67c37a3 | -6.57824 | -59.88084 | 2025-08-24 04:59:00 | NPP-375D | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| ed18073b-8421-3934-bc00-181910177ede | -9.19086 | -59.62264 | 2025-08-24 04:59:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| cbc701ba-f832-3c7f-a1d6-8e5f23978acd | -8.91365 | -62.11013 | 2025-08-24 04:59:00 | NPP-375D | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 9e5016e5-d7fb-32af-b289-162e94476d9d | -11.05534 | -44.61575 | 2025-08-24 04:59:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 352485ed-62ec-3249-9620-91004b57fca0 | -9.39998 | -47.3539 | 2025-08-24 04:59:00 | NPP-375D | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 08a3d550-d8fe-35ee-92a4-03e003e2a36d | -9.68391 | -48.34215 | 2025-08-24 04:59:00 | NPP-375D | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 3ad908bb-2a87-3161-b105-bb7fb2dfa655 | -8.61638 | -62.60675 | 2025-08-24 04:59:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 129ac66b-bdd4-3f67-b02e-e5794d886837 | -8.91444 | -62.43458 | 2025-08-24 04:59:00 | NPP-375D | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 1.7 |
| de0c9798-52ac-39c7-af9b-00e647dd6e3d | -8.13895 | -62.87475 | 2025-08-24 04:59:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.0 |
| aaa78a06-69ba-37ac-bb85-2e843472f50a | -10.81385 | -46.38969 | 2025-08-24 04:59:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| b3138a5a-416e-30bb-a4bf-dc06e67b5aae | -9.15723 | -59.45017 | 2025-08-24 04:59:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 7.5 |
| 473e8c0a-2e17-3d67-81c6-2747aa4b46d2 | -7.91625 | -45.90158 | 2025-08-24 04:59:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| f06fc36b-1859-3fed-8676-a92b578bee04 | -9.14809 | -59.48029 | 2025-08-24 04:59:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 11587ca6-59c4-382b-999c-cc1292b8e90a | -6.90501 | -62.98444 | 2025-08-24 04:59:00 | NPP-375D | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 81c248e3-44ab-3714-849c-80aaa300caf5 | -7.8078 | -63.553 | 2025-08-24 04:59:00 | NPP-375D | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 89d563a4-cfbd-301c-8e1d-006b770fd260 | -8.59799 | -63.29154 | 2025-08-24 04:59:00 | NPP-375D | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 1.7 |
| c10a885c-64c0-3e30-93f5-e3774a60a579 | -9.15731 | -59.48426 | 2025-08-24 04:59:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 6.3 |
| 3192454a-10a8-3a03-b0bd-d860c69d2944 | -5.79508 | -59.21679 | 2025-08-24 04:59:00 | NPP-375D | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| c20a6e7f-b2c6-322e-bf39-8d74404f23ab | -7.72914 | -67.07226 | 2025-08-24 04:59:00 | NPP-375D | PAUINI | AMAZONAS | Brasil | 1303502 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 8ceb08c2-0d80-3740-b909-f204f43df5f2 | -11.13466 | -46.33081 | 2025-08-24 04:59:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| c0e28dcf-b516-339e-a88e-b777eba029ff | -7.80565 | -61.35603 | 2025-08-24 04:59:00 | NPP-375D | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| a1de4e70-6d98-3800-9300-e205dc24f230 | -5.79859 | -59.2211 | 2025-08-24 04:59:00 | NPP-375D | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 29bdd5ce-6e72-371c-b3af-cfea5fb4eefe | -6.57529 | -59.87236 | 2025-08-24 04:59:00 | NPP-375D | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 834ce65c-de46-3c1c-8c78-b347258d37b3 | -9.24761 | -59.63549 | 2025-08-24 04:59:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 69e2f081-844d-30ab-b998-08e01d679afc | -6.3809 | -62.90979 | 2025-08-24 04:59:00 | NPP-375D | TAPAUÁ | AMAZONAS | Brasil | 1304104 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 12ab9ebe-23ac-37b9-b637-373a2993a77e | -9.15335 | -59.48358 | 2025-08-24 04:59:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 6.3 |
| f89c3e7c-22db-3a77-84e1-10cd1075a00d | -9.17056 | -58.30715 | 2025-08-24 04:59:00 | NPP-375D | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 8931bea2-b96c-3728-b337-78700dc47c96 | -8.53602 | -48.85965 | 2025-08-24 04:59:00 | NPP-375D | ITAPORÃ DO TOCANTINS | TOCANTINS | Brasil | 1711100 | 17 | 33 | nan | nan | nan | Amazônia | 0.9 |
| bf07e4dc-0af6-378b-80ea-744fa57db50a | -9.15566 | -59.44702 | 2025-08-24 04:59:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 6.0 |
| e6968e5b-8709-30c4-91a7-2d98cc3dfc1f | -8.90861 | -62.43914 | 2025-08-24 04:59:00 | NPP-375D | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 3d5d04aa-4ad9-36f4-be96-35cfcb2e57fe | -9.18685 | -59.62196 | 2025-08-24 04:59:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| b14e6a60-3444-39fc-bd5f-1ea1ec18e066 | -9.15293 | -59.47578 | 2025-08-24 04:59:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 7.1 |
| 7d17a754-f395-3913-a5c0-83f276296414 | -9.17043 | -60.81092 | 2025-08-24 04:59:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 4.0 |
| feb76944-28fb-365c-9f4c-e61369428d96 | -11.10694 | -44.76773 | 2025-08-24 04:59:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| fde0d771-c078-3a6a-a0ae-9603a1f4693a | -8.60778 | -62.60149 | 2025-08-24 04:59:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 8.7 |
| 2c87d9c4-f4c6-3cc1-8abe-bd0e32be395f | -8.76669 | -46.75224 | 2025-08-24 04:59:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 206b7a11-c191-3aa9-a2d6-f7f050df0761 | -7.54537 | -63.84151 | 2025-08-24 04:59:00 | NPP-375D | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 0209f1ac-6a03-3e2a-93eb-d079fd05a04c | -8.22126 | -45.11815 | 2025-08-24 04:59:00 | NPP-375D | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 9eb8dda2-4c1a-335a-ad45-238fc2ecbcd2 | -10.80489 | -46.41922 | 2025-08-24 04:59:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| d7419766-96c6-3e8c-9ce2-5d1bc803d8b9 | -8.93867 | -62.43905 | 2025-08-24 04:59:00 | NPP-375D | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 1.4 |
| de2d0639-92a4-3555-bee6-875adc170c84 | -11.32378 | -47.85933 | 2025-08-24 04:59:00 | NPP-375D | SANTA ROSA DO TOCANTINS | TOCANTINS | Brasil | 1718907 | 17 | 33 | nan | nan | nan | Cerrado | 6.3 |
| 4f6d48aa-1a3c-3049-91e4-d0505ea9991f | -8.91735 | -62.44631 | 2025-08-24 04:59:00 | NPP-375D | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 1.4 |


[Clique aqui para ver as próximas entradas](README56.md)
