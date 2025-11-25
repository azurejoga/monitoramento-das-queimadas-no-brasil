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

## Dados Diários - Página 9

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 1ef19c68-2efa-3dc9-91b3-6b20be9407a0 | -6.05182 | -43.77735 | 2025-11-25 04:18:00 | NPP-375D | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 676655f2-46eb-3b83-8f4a-cb6872d61e72 | -6.89689 | -42.84306 | 2025-11-25 04:18:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 5.6 |
| 00730009-35f2-3dde-b140-b33cffb809bc | -6.50025 | -38.83425 | 2025-11-25 04:18:00 | NPP-375D | ICÓ | CEARÁ | Brasil | 2305407 | 23 | 33 | nan | nan | nan | Caatinga | 2.1 |
| aec2676a-a1f6-32db-ad69-4943d15e72a3 | -8.06501 | -43.13855 | 2025-11-25 04:18:00 | NPP-375D | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 4.1 |
| 6b81353e-7fb8-32bb-8499-7664de7672d6 | -4.65028 | -45.68975 | 2025-11-25 04:18:00 | NPP-375D | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 41fe0e0b-5403-3fcf-a82e-6296dfe56d6f | -6.50615 | -38.82694 | 2025-11-25 04:18:00 | NPP-375D | ICÓ | CEARÁ | Brasil | 2305407 | 23 | 33 | nan | nan | nan | Caatinga | 4.8 |
| b7d63fe8-39b2-36ae-a2fb-b2420353299c | -8.04563 | -43.13192 | 2025-11-25 04:18:00 | NPP-375D | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 11.6 |
| 45efabcf-2ae0-3a31-b3fd-47c75901c9df | -8.06555 | -43.13507 | 2025-11-25 04:18:00 | NPP-375D | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 2.2 |
| 537cc0e8-ec36-3448-a56e-d047bc41458d | -6.46562 | -43.55726 | 2025-11-25 04:18:00 | NPP-375D | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 112612a0-a3e5-32c9-95b5-3b536abcdf22 | -8.04617 | -43.12843 | 2025-11-25 04:18:00 | NPP-375D | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 11.6 |
| 357a7c89-24f2-379e-adef-1a783c18740e | -8.0473 | -43.14289 | 2025-11-25 04:18:00 | NPP-375D | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 3fe2e458-5943-39f2-a923-baa35d58789e | -5.57871 | -45.16505 | 2025-11-25 04:18:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| d26ef067-b015-3e0b-a733-1cfb5e90a180 | -6.68436 | -43.94613 | 2025-11-25 04:18:00 | NPP-375D | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 10.6 |
| 4cc8dacb-f500-370d-bd00-c864b4afed10 | -8.05172 | -43.13645 | 2025-11-25 04:18:00 | NPP-375D | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 22.1 |
| 96ba5791-4339-32bf-8c16-7a05196e591b | -5.63465 | -43.92715 | 2025-11-25 04:18:00 | NPP-375D | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| be7a446b-d1bf-33e5-a1f5-c4a74e4bbb09 | -7.57532 | -45.85681 | 2025-11-25 04:18:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 5e546a4b-1fcb-3d1a-af02-cace696eb822 | -8.04785 | -43.13941 | 2025-11-25 04:18:00 | NPP-375D | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 9.9 |
| 70892e9b-8c70-3efc-b3cc-9ff451df543c | -6.81072 | -38.57551 | 2025-11-25 04:18:00 | NPP-375D | CAJAZEIRAS | PARAÍBA | Brasil | 2503704 | 25 | 33 | nan | nan | nan | Caatinga | 2.2 |
| c30fc8eb-9fd2-37a3-9407-b839edfd94c5 | -5.78656 | -43.03711 | 2025-11-25 04:18:00 | NPP-375D | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 0.6 |
| b96ae810-e907-39b1-b34d-f53015390e0f | -5.57065 | -44.97336 | 2025-11-25 04:18:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 6.7 |
| be2ae4a1-5d6f-3d00-9cae-973eb582ff6e | -9.12091 | -44.4387 | 2025-11-25 04:18:00 | NPP-375D | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 94570172-9038-3811-a747-8b0d18bbe591 | -6.0048 | -44.17113 | 2025-11-25 04:18:00 | NPP-375D | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 3de0b4cf-2393-31b9-9dc1-d6d30ac0f69d | -8.5451 | -40.21307 | 2025-11-25 04:18:00 | NPP-375D | LAGOA GRANDE | PERNAMBUCO | Brasil | 2608750 | 26 | 33 | nan | nan | nan | Caatinga | 3.3 |
| e03b5309-c20f-3627-809b-db8559f903d7 | -7.46462 | -45.19119 | 2025-11-25 04:18:00 | NPP-375D | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 00e3b912-00a2-37ac-ae05-01e152452d7d | -8.05449 | -43.14046 | 2025-11-25 04:18:00 | NPP-375D | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 22.1 |
| bd20c3ed-9291-32a6-9537-ce41172ad1d2 | -8.16414 | -43.197 | 2025-11-25 04:18:00 | NPP-375D | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 2.5 |
| 0973d010-a89d-3d78-93fb-2358ffc14746 | -5.89921 | -44.51859 | 2025-11-25 04:18:00 | NPP-375D | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 845c223f-d50d-33d0-a617-55ca80d47b71 | -6.00144 | -44.1706 | 2025-11-25 04:18:00 | NPP-375D | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| d48bb376-1a6c-39f2-8a10-c3495d2e0392 | -5.7447 | -42.377 | 2025-11-25 04:18:00 | NPP-375D | PASSAGEM FRANCA DO PIAUÍ | PIAUÍ | Brasil | 2207751 | 22 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 4dfeedc4-a400-3115-8c1b-5ab5fa2d38ab | -7.56285 | -45.86684 | 2025-11-25 04:18:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| ddce5f5e-0cc4-32d5-a4b7-b0ad40d112e4 | -8.05062 | -43.14342 | 2025-11-25 04:18:00 | NPP-375D | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 69440652-3057-36bf-a97e-bb84f9893d45 | -7.56765 | -45.85962 | 2025-11-25 04:18:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| a9647b5c-f8c4-376e-84f0-b3cda717903c | -5.85384 | -42.93425 | 2025-11-25 04:18:00 | NPP-375D | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| a5067d21-4cd7-3e6a-9c99-5364a17ebf45 | -8.16137 | -43.19299 | 2025-11-25 04:18:00 | NPP-375D | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| d407f1f5-16fa-3276-8d0c-fe0f0d4a7808 | -5.58382 | -45.17764 | 2025-11-25 04:18:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 306ab226-97ae-3282-95ec-47bfe7fd38f8 | -5.59077 | -45.17875 | 2025-11-25 04:18:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| a2512811-8161-3120-8cc7-d9edaf89cb77 | -5.78988 | -43.03764 | 2025-11-25 04:18:00 | NPP-375D | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 0.6 |
| 77e3bb33-98a0-3079-8fa2-300af064973d | -5.95597 | -43.9276 | 2025-11-25 04:18:00 | NPP-375D | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| ea441ce8-5823-3749-b3ef-f52d6ea7d94d | -6.60091 | -43.68945 | 2025-11-25 04:18:00 | NPP-375D | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 0.4 |
| d37a8b0b-948f-378c-94d0-04ccfa4e61f3 | -8.04015 | -40.95047 | 2025-11-25 04:18:00 | NPP-375D | PAULISTANA | PIAUÍ | Brasil | 2207801 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 53012865-f4dc-37f1-850d-94645fd42fe7 | -6.68492 | -43.94263 | 2025-11-25 04:18:00 | NPP-375D | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 18.1 |
| 7a3f3f15-54d8-376d-93f1-9735cca02b19 | -6.90294 | -39.06124 | 2025-11-25 04:18:00 | NPP-375D | LAVRAS DA MANGABEIRA | CEARÁ | Brasil | 2307502 | 23 | 33 | nan | nan | nan | Caatinga | 1.5 |
| fb1bdac5-4af8-35b7-bcdb-7a48a70e5057 | -5.58566 | -45.16618 | 2025-11-25 04:18:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 9e0c299b-92aa-3cfe-9206-83bd1ba6a376 | -6.84077 | -46.27016 | 2025-11-25 04:18:00 | NPP-375D | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 2b1b66df-a3e5-3b18-9f49-7937c6caa01f | -6.70636 | -39.66452 | 2025-11-25 04:18:00 | NPP-375D | TARRAFAS | CEARÁ | Brasil | 2313252 | 23 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 3aec039e-11bd-3239-9d30-2502070f8e2e | -5.9604 | -44.7265 | 2025-11-25 04:18:00 | NPP-375D | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| a0c5ee23-940b-31aa-87af-fdecb1b538a8 | -4.4781 | -48.15508 | 2025-11-25 04:18:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 6ec2be77-1959-34bd-b0e8-ed0fd641aaf1 | -9.9644 | -44.26865 | 2025-11-25 04:18:00 | NPP-375D | CURIMATÁ | PIAUÍ | Brasil | 2203206 | 22 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 60aa73f6-2f76-33d4-bf91-7996a929c7ef | -5.31897 | -44.82732 | 2025-11-25 04:18:00 | NPP-375D | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 93b9d469-0fff-3a45-8810-25dd47ac3bf7 | -5.63521 | -43.92362 | 2025-11-25 04:18:00 | NPP-375D | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 505c1174-d301-3408-95f4-9d325173abad | -5.71417 | -47.27267 | 2025-11-25 04:18:00 | NPP-375D | GOVERNADOR EDISON LOBÃO | MARANHÃO | Brasil | 2104552 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 85ea16f0-d9ee-3802-a0f6-83cd29fac26b | -6.89303 | -42.84602 | 2025-11-25 04:18:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 4.1 |
| 6f33983c-aacd-3a1b-a422-ef5f64023404 | -4.47873 | -48.15116 | 2025-11-25 04:18:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 2a8bce9a-8174-38ba-8eda-3a2fc03a47e4 | -4.8158 | -44.91057 | 2025-11-25 04:18:00 | NPP-375D | POÇÃO DE PEDRAS | MARANHÃO | Brasil | 2108900 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 830ad64a-5db8-35d0-a175-3ff17c1e7f3d | -7.56572 | -45.8713 | 2025-11-25 04:18:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 3.5 |
| b968fbe6-22c6-3aec-8091-909e7763d1ec | -9.71009 | -43.92953 | 2025-11-25 04:18:00 | NPP-375D | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| b3bf1fe6-c992-378e-b78d-5542e34a87f5 | -4.96926 | -43.95988 | 2025-11-25 04:18:00 | NPP-375D | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 249a2ad7-a3bb-3c54-b1b1-d50fa42261de | -8.1946 | -44.43357 | 2025-11-25 04:18:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| dd3aa524-42de-376c-88d5-6419bd5358bd | -7.87946 | -41.73121 | 2025-11-25 04:18:00 | NPP-375D | CONCEIÇÃO DO CANINDÉ | PIAUÍ | Brasil | 2202802 | 22 | 33 | nan | nan | nan | Caatinga | 0.7 |
| dc202360-d515-353b-ad2f-cb082e273c6e | -5.58219 | -45.16562 | 2025-11-25 04:18:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| c158d657-b850-3ce4-ad08-3383ea417836 | -6.12245 | -42.94492 | 2025-11-25 04:18:00 | NPP-375D | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 7.3 |
| 0e18a85c-71ef-3b1e-bde1-aa9d70a1ca1d | -8.7992 | -44.3975 | 2025-11-25 04:18:00 | NPP-375D | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 0.6 |
| bc602c1e-555e-3ded-a7cd-ddaee0162365 | -7.56507 | -45.87521 | 2025-11-25 04:18:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 3.5 |
| caf2c7b7-aab3-3d88-874d-d10ac6a7f646 | -6.84119 | -46.27281 | 2025-11-25 04:18:00 | NPP-375D | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| c565490d-5127-334b-a239-dc85fbcabb14 | -7.46121 | -45.19061 | 2025-11-25 04:18:00 | NPP-375D | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| f8f4c75b-be0a-36e7-bc50-cdb73f375170 | -8.05282 | -43.12949 | 2025-11-25 04:18:00 | NPP-375D | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 28.2 |
| a713773c-4240-3685-bf21-e22ca2ed6237 | -4.96983 | -43.95633 | 2025-11-25 04:18:00 | NPP-375D | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| c66b8b60-e323-34fe-ac4c-b73c379deb4b | -6.89635 | -42.84654 | 2025-11-25 04:18:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 4.1 |
| 8fa30663-86f8-3602-92c4-cd7cfac7ccaa | -5.03083 | -43.25777 | 2025-11-25 04:18:00 | NPP-375D | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| bc893ac1-a63e-372d-92b1-c354d8dbba78 | -8.0661 | -43.13158 | 2025-11-25 04:18:00 | NPP-375D | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 2.2 |
| 040c1b99-fc8e-36c3-b8f6-77d212f76788 | -5.95988 | -43.92463 | 2025-11-25 04:18:00 | NPP-375D | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 70f92d75-3a99-3fff-a6c4-899cf12a6c8f | -8.06223 | -43.13454 | 2025-11-25 04:18:00 | NPP-375D | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 19.4 |
| 54704576-494a-3cb4-9118-4d7c1dbb6514 | -6.33008 | -43.98688 | 2025-11-25 04:18:00 | NPP-375D | PARAIBANO | MARANHÃO | Brasil | 2107704 | 21 | 33 | nan | nan | nan | Cerrado | 0.5 |
| e6b7d50b-3920-3828-9450-bb78d524bdee | -8.21407 | -45.02874 | 2025-11-25 04:18:00 | NPP-375D | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 73002be6-0138-3f19-ac07-46ae278d8f05 | -8.46344 | -40.70119 | 2025-11-25 04:18:00 | NPP-375D | DORMENTES | PERNAMBUCO | Brasil | 2605152 | 26 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 10f8f59d-b832-37e4-9d75-7fe880df4f4f | -8.21121 | -39.67138 | 2025-11-25 04:18:00 | NPP-375D | PARNAMIRIM | PERNAMBUCO | Brasil | 2610400 | 26 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 3d67fa11-1ad9-3ff5-b501-bd59f93afb43 | -6.07612 | -39.54985 | 2025-11-25 04:18:00 | NPP-375D | ACOPIARA | CEARÁ | Brasil | 2300309 | 23 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 0752a4bb-88b2-38ee-b719-7b884182f015 | -6.69215 | -43.9402 | 2025-11-25 04:18:00 | NPP-375D | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 8ce25d0d-dcf5-38a4-b3d0-3d51bc278721 | -6.31244 | -43.81844 | 2025-11-25 04:18:00 | NPP-375D | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 62dd3ab5-e1e9-3c19-ab31-a589c6e0310f | -7.86275 | -46.75329 | 2025-11-25 04:18:00 | NPP-375D | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| e47eb81d-b6ee-3993-b41a-49e4c8920ad0 | -5.32241 | -44.82789 | 2025-11-25 04:18:00 | NPP-375D | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| f5af10aa-ac8c-3fd1-9a67-e9d759c642db | -8.21068 | -45.02819 | 2025-11-25 04:18:00 | NPP-375D | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 0.8 |
| ab980a8d-0f56-3e17-9ea3-5f367ab7e8d4 | -6.45751 | -38.38101 | 2025-11-25 04:18:00 | NPP-375D | UIRAÚNA | PARAÍBA | Brasil | 2516904 | 25 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 6b83c7ec-53f5-359d-9a30-e6b3d03d002b | -5.0197 | -43.94606 | 2025-11-25 04:18:00 | NPP-375D | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 2e775cf8-6887-31d7-8fba-9020c96bfc47 | -5.41756 | -43.65824 | 2025-11-25 04:18:00 | NPP-375D | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| ae74e4ea-05b7-3d75-8c1d-86659f491c9b | -6.68882 | -43.93967 | 2025-11-25 04:18:00 | NPP-375D | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 18.1 |
| 42dd2fb9-3cfd-311d-b508-92dc6d751257 | -6.68387 | -42.4777 | 2025-11-25 04:18:00 | NPP-375D | ARRAIAL | PIAUÍ | Brasil | 2201002 | 22 | 33 | nan | nan | nan | Caatinga | 2.3 |
| 46714bb1-7abe-34a7-af21-616e0b0bb155 | -7.56922 | -45.87188 | 2025-11-25 04:18:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| bc3d2dc0-3653-380a-a64a-55c6aede182b | -7.16841 | -44.9933 | 2025-11-25 04:18:00 | NPP-375D | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 5a9d4c5b-43c3-3ea0-afa1-b34a0a383a1b | -7.86347 | -46.74905 | 2025-11-25 04:18:00 | NPP-375D | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 09f1ba6b-a77d-3bf5-a145-aed5430e2ee5 | -6.80752 | -38.20798 | 2025-11-25 04:18:00 | NPP-375D | SOUSA | PARAÍBA | Brasil | 2516201 | 25 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 225c3f7b-1635-3679-9b87-507f14b847e5 | -8.05395 | -43.14394 | 2025-11-25 04:18:00 | NPP-375D | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 6ccf99bc-d67d-36d3-897f-bcaf477881bc | -6.67943 | -42.48418 | 2025-11-25 04:18:00 | NPP-375D | ARRAIAL | PIAUÍ | Brasil | 2201002 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| e8bc3a12-92a7-35a3-97ba-502a2bebccdd | -6.89357 | -42.84254 | 2025-11-25 04:18:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 5.6 |
| b439fe17-524b-35e9-9708-9db95e1e66b6 | -7.56704 | -42.86348 | 2025-11-25 04:18:00 | NPP-375D | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| ae6bb89b-128d-3563-be4c-0e9969ff67c8 | -6.89744 | -42.83959 | 2025-11-25 04:18:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 5.6 |
| 6a7b7607-d387-39eb-8942-5354a7457c0f | -7.5386 | -46.56988 | 2025-11-25 04:18:00 | NPP-375D | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| acbd4104-3a9f-3370-ae9f-f6614fb2b36b | -6.66535 | -43.77103 | 2025-11-25 04:18:00 | NPP-375D | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 800f2ab8-5d85-3096-913e-779ffbab50d9 | -6.35007 | -41.39858 | 2025-11-25 04:18:00 | NPP-375D | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 4304feb8-cc48-3ad6-8ae2-1fefd9996a7d | -6.05487 | -43.77425 | 2025-11-25 04:18:00 | NPP-375D | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |


[Clique aqui para ver as próximas entradas](README10.md)
