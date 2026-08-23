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

## Dados Diários - Página 1

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 2b03a7d4-1a6a-3a05-add8-6cdb55307ead | -6.1469 | -57.8385 | 2026-08-23 00:00:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 55.8 |
| 12a80839-2fd0-30ab-9144-de1c4db46665 | -13.1886 | -51.4447 | 2026-08-23 00:00:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 77.3 |
| 3f7d5c9f-110c-3629-91b1-4be6c6eb387d | -7.6849 | -63.3443 | 2026-08-23 00:00:00 | GOES-19 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 66.1 |
| e8bbd707-9f08-3eb5-a28d-5d2d611b1de7 | -6.8188 | -59.6696 | 2026-08-23 00:00:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 128.8 |
| d4a997f3-de47-3cd1-a225-f7e7d5dc8949 | -6.8062 | -58.6469 | 2026-08-23 00:00:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 133.6 |
| d42ae4f8-5b95-36cc-a5a1-90759a1c8030 | -9.1722 | -59.4629 | 2026-08-23 00:00:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 55.8 |
| 911a19e1-9e73-339f-974d-e140b51a157b | -6.6765 | -58.7492 | 2026-08-23 00:00:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 134.7 |
| 6a57eba3-4b4f-3697-b2b2-ee4b7a3f49e1 | -13.2078 | -51.4423 | 2026-08-23 00:00:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 63.4 |
| 84699d9a-baf5-376f-8e00-01e830955347 | -6.7135 | -58.7283 | 2026-08-23 00:00:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 94.9 |
| efa4e179-d289-3eb7-8323-0f5dcf0c6e75 | -6.9698 | -59.0852 | 2026-08-23 00:00:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 102.4 |
| 15fdcaff-9b7e-3ba0-b861-9d9deff2472f | -6.8061 | -58.6663 | 2026-08-23 00:00:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 101.1 |
| 7e801da5-e98d-3cc1-96a8-1e6e44bbe2f4 | -6.8373 | -59.6689 | 2026-08-23 00:00:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 109.8 |
| e9768818-7aa7-3e53-856f-0c256f500479 | -6.9514 | -59.0666 | 2026-08-23 00:00:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 171.9 |
| f8eca494-2bdc-3d4a-abea-2f035f309cf8 | -7.6664 | -63.3449 | 2026-08-23 00:00:00 | GOES-19 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 59.1 |
| 8e7dce46-835a-3307-aee1-08017ee5abd3 | -6.9329 | -59.0674 | 2026-08-23 00:00:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 78.1 |
| 2bd04934-97eb-3a5d-94da-da2d743fa962 | -8.9252 | -48.5422 | 2026-08-23 00:00:00 | GOES-19 | GUARAÍ | TOCANTINS | Brasil | 1709302 | 17 | 33 | nan | nan | nan | Amazônia | 61.9 |
| 8a08c8cb-7802-3c57-9c95-0ad55653a0aa | -6.6766 | -58.7299 | 2026-08-23 00:00:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 217.1 |
| 2200b87c-bf49-3fe2-ab12-73ec07c108ce | -6.5671 | -58.5212 | 2026-08-23 00:00:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 62.8 |
| 6997572b-5419-3ca7-87bc-fe5cfd1b6c90 | -18.5406 | -47.1608 | 2026-08-23 00:00:00 | GOES-19 | COROMANDEL | MINAS GERAIS | Brasil | 3119302 | 31 | 33 | nan | nan | nan | Cerrado | 53.6 |
| 2862e885-dcd4-3d01-88ff-b5fa0f4df814 | -6.211 | -53.5221 | 2026-08-23 00:00:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 54.4 |
| 22eb19ee-6aa0-325d-aa70-d507f88c25fd | -5.7799 | -57.58 | 2026-08-23 00:00:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 64.7 |
| 96684de2-238c-3587-9baa-1aa4aad86079 | -6.8027 | -62.9024 | 2026-08-23 00:00:00 | GOES-19 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 84.3 |
| 6a643b21-3b95-3756-ac68-995023f48af9 | -2.982 | -48.9598 | 2026-08-23 00:00:00 | GOES-19 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 180.2 |
| 7806723d-9d9c-3cea-9390-9f9adacb26da | -18.5413 | -47.1375 | 2026-08-23 00:00:00 | GOES-19 | COROMANDEL | MINAS GERAIS | Brasil | 3119302 | 31 | 33 | nan | nan | nan | Cerrado | 70.3 |
| f7f26312-92b4-310d-8767-01b87be64c8f | -6.8004 | -59.6704 | 2026-08-23 00:00:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 69.2 |
| 6dcfe6c9-9010-34af-840b-f2d0f1f83d28 | -6.8247 | -58.6461 | 2026-08-23 00:00:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 62.9 |
| 4bacff87-f5fd-3cb5-991d-6e4d1345242e | -2.9821 | -48.9384 | 2026-08-23 00:00:00 | GOES-19 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 61.7 |
| 68cae061-d324-347e-9354-40c4fae148dd | -12.2613 | -43.1845 | 2026-08-23 00:00:00 | GOES-19 | IBOTIRAMA | BAHIA | Brasil | 2913200 | 29 | 33 | nan | nan | nan | Caatinga | 98.6 |
| f5b84ce4-4b79-343f-abd4-16cd228f1ce7 | -6.1286 | -57.8198 | 2026-08-23 00:00:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 80.7 |
| 83e294d6-11a1-3790-940a-37fd8e3032db | -6.5487 | -58.522 | 2026-08-23 00:00:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 114.3 |
| 3d03850d-2eda-3882-b243-35fcd8057dd7 | -6.9513 | -59.0859 | 2026-08-23 00:00:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 108.3 |
| 98b64d49-b721-3b41-a7cd-245aa6e55bca | -6.1101 | -57.84 | 2026-08-23 00:00:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 73.1 |
| f7fef09f-822a-3e14-9815-f7874431aa9d | -6.8018 | -59.4201 | 2026-08-23 00:00:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 81.2 |
| ee2d955f-0e49-3264-a846-11936aab5fe3 | -6.8008 | -59.5934 | 2026-08-23 00:00:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 109.7 |
| f9e48b96-b0a9-39d4-82e3-6f3c8f301bf7 | -6.9699 | -59.0658 | 2026-08-23 00:00:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 220.6 |
| f961546c-2192-3b47-bcc3-55633e491edc | -21.454 | -46.1371 | 2026-08-23 00:00:00 | GOES-19 | ALFENAS | MINAS GERAIS | Brasil | 3101607 | 31 | 33 | nan | nan | nan | Mata Atlântica | 80.1 |
| 9776a54b-dd16-3af9-9741-9cb940e7e68c | -12.075 | -50.5974 | 2026-08-23 00:00:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 71.2 |
| 120ebcd5-2ad0-337d-b29b-e876d083b943 | -7.5668 | -61.2096 | 2026-08-23 00:00:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 78.7 |
| ce42ff7b-e0fc-3186-8c2f-4b7b37c79c93 | -6.1924 | -53.5434 | 2026-08-23 00:00:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 48.7 |
| 90fff339-e104-373c-9099-b6e168142823 | -20.6607 | -46.5777 | 2026-08-23 00:00:00 | GOES-19 | PASSOS | MINAS GERAIS | Brasil | 3147907 | 31 | 33 | nan | nan | nan | Cerrado | 62.9 |
| 720e8e8a-ba7f-3acd-951f-9b40648ef682 | -6.8026 | -62.9212 | 2026-08-23 00:00:00 | GOES-19 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 75.7 |
| 8374615b-1bdd-372b-a920-4207ab401a06 | -12.242 | -43.1877 | 2026-08-23 00:00:00 | GOES-19 | IBOTIRAMA | BAHIA | Brasil | 2913200 | 29 | 33 | nan | nan | nan | Caatinga | 71.3 |
| 5f8738e0-8977-3da5-aecf-22e37cf92973 | -7.5669 | -61.1906 | 2026-08-23 00:00:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 92.6 |
| 5849663d-7345-38e7-9c9c-d8a3eebc32fb | -6.8571 | -59.4179 | 2026-08-23 00:00:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 67.8 |
| e62f3e53-edb8-3b88-9b48-b10ba79cd868 | -11.4302 | -44.5382 | 2026-08-23 00:00:00 | GOES-19 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 69.4 |
| 79f083cf-0d58-3936-9f74-487570f6182f | -6.9883 | -59.0651 | 2026-08-23 00:00:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 67.9 |
| bc438467-d501-3e4c-9454-83896901b6d0 | -9.1909 | -59.4619 | 2026-08-23 00:00:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 64.2 |
| b6fb4282-e34a-3c3f-bfa6-bf132e148bc1 | -9.191 | -59.4425 | 2026-08-23 00:00:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 79.4 |
| f79990bd-8c2e-3308-92c1-9df340a6d052 | -6.6949 | -58.7485 | 2026-08-23 00:00:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 94.4 |
| 2a1505ee-3dfa-3de7-a660-4ec670d87978 | -6.695 | -58.7291 | 2026-08-23 00:00:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 164.8 |
| ea89d971-02e0-317a-9ec5-286f1dbbf52b | -6.1925 | -53.5231 | 2026-08-23 00:00:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 145.4 |
| 282dc4b4-e9bc-3d17-a41b-316d2c243631 | -3.0005 | -48.9592 | 2026-08-23 00:00:00 | GOES-19 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 93.6 |
| 0e36ad67-d6dc-3c92-8140-7799b5e201ef | -6.1285 | -57.8393 | 2026-08-23 00:00:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 146.3 |
| e5f232f2-2334-3011-9eca-40e32dd8a7d2 | -6.8008 | -59.5934 | 2026-08-23 00:10:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 83.3 |
| 3be2dfc2-f4fe-3c09-a17e-5db11f105c24 | -6.211 | -53.5221 | 2026-08-23 00:10:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 58.5 |
| 0a1e43ab-117d-395d-8426-6a59482015b6 | -9.1722 | -59.4629 | 2026-08-23 00:10:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 54.4 |
| c6371b13-a412-34b7-b4be-780ee025acaa | -9.1909 | -59.4619 | 2026-08-23 00:10:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 67.5 |
| 5884aa31-22f7-3745-9b5e-2db198517884 | -2.5629 | -47.2445 | 2026-08-23 00:10:00 | GOES-19 | CAPITÃO POÇO | PARÁ | Brasil | 1502301 | 15 | 33 | nan | nan | nan | Amazônia | 52.8 |
| 0acf2905-1814-365e-b6c0-663609bbdaea | -3.0005 | -48.9592 | 2026-08-23 00:10:00 | GOES-19 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 148.8 |
| bb070c65-dc21-3416-b28c-58a77e326871 | -6.9513 | -59.0859 | 2026-08-23 00:10:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 110.0 |
| fa598bd7-2f38-37da-8209-94f7fbfe3bc9 | -7.5669 | -61.1906 | 2026-08-23 00:10:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 80.6 |
| c750ea11-eb4a-3837-afa8-b8dd037bbea2 | -6.5487 | -58.522 | 2026-08-23 00:10:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 105.6 |
| f4c9a1d7-bd66-3fa5-983a-818faf92b550 | -6.8026 | -62.9212 | 2026-08-23 00:10:00 | GOES-19 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 70.0 |
| 5b6755d3-fea8-37ef-be80-468b998fcdf3 | -6.8027 | -62.9024 | 2026-08-23 00:10:00 | GOES-19 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 69.9 |
| 65daa6a8-e7c1-3f60-afce-492c8a9588e0 | -7.5668 | -61.2096 | 2026-08-23 00:10:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 64.7 |
| ce419a63-8467-3c6e-8462-79103346f814 | -5.7615 | -57.5807 | 2026-08-23 00:10:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 54.3 |
| d6545338-73bb-358d-b407-83dea0dab70e | -6.8188 | -59.6696 | 2026-08-23 00:10:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 142.0 |
| 62bb1d26-01b0-3eaa-9873-1dcba39bad28 | -6.8018 | -59.4201 | 2026-08-23 00:10:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 73.9 |
| 532677c8-75d6-325d-9705-25d449648e5b | -6.8062 | -58.6469 | 2026-08-23 00:10:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 121.6 |
| 5ad15c97-47d7-3615-809e-bafd3592e3f2 | -6.8373 | -59.6689 | 2026-08-23 00:10:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 73.5 |
| e43e23a4-8b8f-32b7-bf75-305700038745 | -18.5205 | -47.1651 | 2026-08-23 00:10:00 | GOES-19 | COROMANDEL | MINAS GERAIS | Brasil | 3119302 | 31 | 33 | nan | nan | nan | Cerrado | 54.0 |
| f6b57b2d-0d3c-3aeb-887c-0e99579063b9 | -2.982 | -48.9598 | 2026-08-23 00:10:00 | GOES-19 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 173.5 |
| 9c7c204e-b7b8-36b3-a2d2-97df65e033ee | -6.9514 | -59.0666 | 2026-08-23 00:10:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 151.0 |
| 56c4a50f-bcad-37bb-b122-02424d590d2d | -12.2415 | -43.2116 | 2026-08-23 00:10:00 | GOES-19 | IBOTIRAMA | BAHIA | Brasil | 2913200 | 29 | 33 | nan | nan | nan | Cerrado | 74.0 |
| 16fe1498-6833-341b-8f94-009578fbf7ee | -6.9698 | -59.0852 | 2026-08-23 00:10:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 101.6 |
| 166eb594-c64c-31ce-86af-f351d7066db3 | -20.6607 | -46.5777 | 2026-08-23 00:10:00 | GOES-19 | PASSOS | MINAS GERAIS | Brasil | 3147907 | 31 | 33 | nan | nan | nan | Cerrado | 83.3 |
| 834b3482-b4b5-35a1-bb4f-1e03933dd7b9 | -6.8189 | -59.6504 | 2026-08-23 00:10:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 70.9 |
| c7d27355-fb73-311c-b1fa-d0436a3e7f06 | -12.2424 | -43.1638 | 2026-08-23 00:10:00 | GOES-19 | IBOTIRAMA | BAHIA | Brasil | 2913200 | 29 | 33 | nan | nan | nan | Caatinga | 117.7 |
| a322e30d-5664-39d1-bb0a-e8b45a98ce64 | -8.9252 | -48.5422 | 2026-08-23 00:10:00 | GOES-19 | GUARAÍ | TOCANTINS | Brasil | 1709302 | 17 | 33 | nan | nan | nan | Amazônia | 66.2 |
| 4bf85b59-a095-3474-90b0-4ef40a0c54de | -6.8061 | -58.6663 | 2026-08-23 00:10:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 86.7 |
| 321b7e29-3bd9-39f6-b1ce-481607dc4833 | -5.7799 | -57.58 | 2026-08-23 00:10:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 68.2 |
| 6b84f40d-136f-3ec1-81b2-6c423f9215e7 | -6.9883 | -59.0651 | 2026-08-23 00:10:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 65.5 |
| 63d7d0fc-3a80-3441-9792-44cc769c36ac | -6.9329 | -59.0674 | 2026-08-23 00:10:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 67.3 |
| bafb7507-b51a-33dd-9a38-8f58d747b72d | -13.1886 | -51.4447 | 2026-08-23 00:10:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 97.8 |
| 51347cd1-c371-3488-a0cb-2175c714e8ed | -6.8571 | -59.4179 | 2026-08-23 00:10:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 68.6 |
| 47194f7c-b0c8-31be-a963-1a8cacb70d2e | -9.191 | -59.4425 | 2026-08-23 00:10:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 82.9 |
| babec529-ab44-347b-9431-6080e90d2c6b | -21.454 | -46.1371 | 2026-08-23 00:10:00 | GOES-19 | ALFENAS | MINAS GERAIS | Brasil | 3101607 | 31 | 33 | nan | nan | nan | Mata Atlântica | 103.8 |
| 7c374ef5-3806-3d1a-b931-afc269b5b94a | -7.6664 | -63.3449 | 2026-08-23 00:10:00 | GOES-19 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 57.1 |
| 800e358c-2c8a-3b30-ab01-d7c3f9c37bba | -6.1285 | -57.8393 | 2026-08-23 00:10:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 146.8 |
| 6998c355-b611-3b39-9dbf-fc4d997ae280 | -6.1925 | -53.5231 | 2026-08-23 00:10:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 105.6 |
| e7726809-08c9-3d2d-9119-6a8af82e82ca | -12.2613 | -43.1845 | 2026-08-23 00:10:00 | GOES-19 | IBOTIRAMA | BAHIA | Brasil | 2913200 | 29 | 33 | nan | nan | nan | Caatinga | 227.2 |
| 2e9993ae-cc7f-3f30-b7b6-079bd73d3b17 | -12.2617 | -43.1606 | 2026-08-23 00:10:00 | GOES-19 | IBOTIRAMA | BAHIA | Brasil | 2913200 | 29 | 33 | nan | nan | nan | Caatinga | 92.9 |
| a8506c2c-a78a-34e1-9a19-76aa34c59b86 | -12.242 | -43.1877 | 2026-08-23 00:10:00 | GOES-19 | IBOTIRAMA | BAHIA | Brasil | 2913200 | 29 | 33 | nan | nan | nan | Caatinga | 305.9 |
| c7f27506-2d10-3b1a-9593-a1624930928e | -6.1924 | -53.5434 | 2026-08-23 00:10:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 44.3 |
| 8d40cb6f-0b9d-31e2-aeb9-5faa3b323370 | -6.1286 | -57.8198 | 2026-08-23 00:10:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 87.0 |
| 868d4809-0a3c-32e4-83f6-33f8e63f8ad8 | -6.9699 | -59.0658 | 2026-08-23 00:10:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 195.6 |
| 58d046dc-bb7b-3026-8954-6b2f5f2ff375 | -6.68 | -58.75 | 2026-08-23 00:15:00 | MSG-03 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| b33ba2e6-bf5e-3240-9bf5-30e8f7f29244 | -6.8027 | -62.9024 | 2026-08-23 00:20:00 | GOES-19 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 69.4 |
| 78833740-9b4c-3e02-88e7-fc38c6ecc4d2 | -6.9513 | -59.0859 | 2026-08-23 00:20:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 106.4 |
| 7245253c-3bb8-3885-8a1b-5e34895cc0ef | -12.2613 | -43.1845 | 2026-08-23 00:20:00 | GOES-19 | IBOTIRAMA | BAHIA | Brasil | 2913200 | 29 | 33 | nan | nan | nan | Caatinga | 138.0 |


[Clique aqui para ver as próximas entradas](README2.md)
