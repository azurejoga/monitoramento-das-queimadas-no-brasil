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

## Dados Diários - Página 149

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| cc3cf654-ca19-3be8-939c-85d2b3221349 | -2.4841 | -56.11843 | 2026-10-08 05:23:00 | NPP-375D | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 2fb424dc-6ec6-3d99-8b34-d09eec8eefeb | -2.78031 | -54.07272 | 2026-10-08 05:23:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 935c5b49-d323-3018-a143-2507f319199f | -3.54133 | -54.67491 | 2026-10-08 05:23:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 6.9 |
| 8afe00a4-97d8-376e-920a-36eccde7ba4f | -1.88525 | -55.52351 | 2026-10-08 05:23:00 | NPP-375D | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| a7b30398-85f0-3a41-a8c0-11be8308dfcd | -3.11423 | -53.78131 | 2026-10-08 05:23:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| e988a383-be9c-389d-a526-ccbb78ae08e3 | -3.04827 | -53.90113 | 2026-10-08 05:23:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| f06ceb06-2b73-3ed1-b014-b90f76e18b25 | -3.2967 | -54.04204 | 2026-10-08 05:23:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 5f09c67d-e2a7-3b15-854b-36505a9227ea | -2.49362 | -56.16597 | 2026-10-08 05:23:00 | NPP-375D | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 8a7ff0af-dd39-36a0-8695-e919e07f64ac | -3.14775 | -53.71931 | 2026-10-08 05:23:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| f7529e0d-d9a5-3218-b0d4-ad7008414760 | -3.1753 | -58.63437 | 2026-10-08 05:23:00 | NPP-375D | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 4fe95c42-5a63-3663-85c2-a72a87e1cc43 | -3.0861 | -54.28307 | 2026-10-08 05:23:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| b9417cdc-fe2c-3217-87e3-d4520347273f | -3.69456 | -59.64532 | 2026-10-08 05:23:00 | NPP-375D | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 8547bce1-cfdf-30ca-954a-a4d7298bcfe3 | -4.12067 | -59.87241 | 2026-10-08 05:23:00 | NPP-375D | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 6e0d8726-766f-3dbd-a70c-f255e0177a80 | -2.78145 | -56.50512 | 2026-10-08 05:23:00 | NPP-375D | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| b9ac3870-b4e2-3901-a4b3-c4171e60e94e | -3.02154 | -54.07325 | 2026-10-08 05:23:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 01f5920e-ed71-327a-be47-4c90531905b0 | -8.62083 | -67.05538 | 2026-10-08 05:23:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 40c00e40-d274-32c1-b10a-6c00412b70ca | -5.23994 | -50.9042 | 2026-10-08 05:23:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 96969f33-53c2-3bb0-a005-ab7bc57a2d81 | -2.94373 | -54.17582 | 2026-10-08 05:23:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 697f3a8d-b72a-3fa2-a056-f503b1144209 | -4.37453 | -54.75079 | 2026-10-08 05:23:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 875948c5-c9f1-3d22-9cf6-efc59843d4f4 | -4.31762 | -50.77868 | 2026-10-08 05:23:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| a1a81b68-f225-3527-ba31-4dd8c09109f1 | -1.46124 | -54.76612 | 2026-10-08 05:23:00 | NPP-375D | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 2e522173-63f1-330d-955d-1eeaa3961dc8 | -3.02614 | -54.08984 | 2026-10-08 05:23:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| cd805f3d-adf8-34f6-9f13-b3018fdefade | -3.01512 | -54.06828 | 2026-10-08 05:23:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 076aa79f-5d6d-3c5b-96ae-1e44ac0ea029 | -4.12245 | -59.88302 | 2026-10-08 05:23:00 | NPP-375D | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 5.0 |
| ca966f28-fed1-3cbc-ab75-0ac4c2b9d7ec | -3.0928 | -59.19114 | 2026-10-08 05:23:00 | NPP-375D | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 6.0 |
| dfe38278-7d5d-3699-97ef-aaf888b18ea7 | -1.18458 | -54.1758 | 2026-10-08 05:23:00 | NPP-375D | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| eda4f1da-d05b-3679-8504-2e9d27aa11fd | -3.54792 | -50.0949 | 2026-10-08 05:23:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| ed3aeaf2-7601-3fef-8da2-754764432916 | -2.48798 | -56.11549 | 2026-10-08 05:23:00 | NPP-375D | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 2db5d0b5-7eba-38a6-8242-fa1ba545e2d3 | -3.01098 | -57.17023 | 2026-10-08 05:23:00 | NPP-375D | BARREIRINHA | AMAZONAS | Brasil | 1300508 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 7772d54a-5625-392e-908c-fd2c5a3dc60d | -3.54006 | -54.64456 | 2026-10-08 05:23:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| e7ce50dc-0876-35cf-bd88-44ad67a95676 | -3.68218 | -55.94007 | 2026-10-08 05:23:00 | NPP-375D | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| d7918592-7aa3-31e5-ac9b-31559446b56b | -4.91657 | -55.858 | 2026-10-08 05:23:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| ab56a033-e358-3449-ba5c-cd40a76c5936 | -2.4913 | -56.11602 | 2026-10-08 05:23:00 | NPP-375D | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| bd865d25-c655-3bc1-acbd-3dee3e0210c2 | -3.02546 | -54.23166 | 2026-10-08 05:23:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 44871627-52be-3669-84b0-7ca182e5869b | -3.04569 | -54.26195 | 2026-10-08 05:23:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 6.5 |
| b2d18264-df2b-32a7-884a-c24522bdb7cd | -3.30189 | -54.05487 | 2026-10-08 05:23:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 5241ddb4-9fd6-37ef-a617-cd596b99047e | -2.48579 | -56.12932 | 2026-10-08 05:23:00 | NPP-375D | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 7.9 |
| 8d146a9c-9d66-325b-bd8e-d150635b3c4f | -5.04647 | -49.76713 | 2026-10-08 05:23:00 | NPP-375D | ITUPIRANGA | PARÁ | Brasil | 1503705 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 32fb8894-d996-34d2-acc0-b2ce59b6acad | -2.1698 | -54.46087 | 2026-10-08 05:23:00 | NPP-375D | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 59cecb14-d8da-3d6f-8fca-f1e5ce0eab23 | -3.22973 | -54.30833 | 2026-10-08 05:23:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 33d2dde2-44e8-3c41-8db4-cf8f48e001ca | -3.61577 | -55.51126 | 2026-10-08 05:23:00 | NPP-375D | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| e2680900-4761-3d7e-8ca5-b675acdb2709 | -2.78422 | -56.5091 | 2026-10-08 05:23:00 | NPP-375D | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 9d61def3-a166-365f-aa17-771b4130e117 | -1.53295 | -54.55548 | 2026-10-08 05:23:00 | NPP-375D | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 35.7 |
| 37ae747e-a38b-3666-967a-bd6d282f5aeb | -3.48122 | -54.72707 | 2026-10-08 05:23:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 9e18d686-81a4-33f8-b3b7-6903e930c7c1 | -1.18905 | -55.66681 | 2026-10-08 05:23:00 | NPP-375D | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| cea13430-71e6-3bdd-9f94-0c1afaba01fa | -3.54651 | -54.66422 | 2026-10-08 05:23:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 0f4f8136-01a2-3986-97ec-6c900fa809f5 | -4.92385 | -55.85553 | 2026-10-08 05:23:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 2c0256a8-a9fc-3254-813a-d311e0cb383c | -7.202 | -55.13306 | 2026-10-08 05:23:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 3205a482-33ea-3f04-8958-3015829d3cd7 | -2.75629 | -54.0382 | 2026-10-08 05:23:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 07de0f37-b3d5-32c3-afbb-1a319d92aaeb | -6.95084 | -45.2827 | 2026-10-08 05:23:00 | NPP-375D | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 18.9 |
| 3cbff37d-7d02-3112-ac48-51cc70e80733 | -4.26985 | -54.86494 | 2026-10-08 05:23:00 | NPP-375D | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| ae46ff79-16a5-39b3-8c50-1725ad1bec5a | -2.98913 | -54.14339 | 2026-10-08 05:23:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| dc9542e1-3544-37b6-bbff-5a87f100913f | -9.48674 | -64.36754 | 2026-10-08 05:23:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 8968f232-6ae0-350f-bf14-39684af8e0d2 | -4.15173 | -55.14818 | 2026-10-08 05:23:00 | NPP-375D | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| e9152838-8277-3232-98aa-95f20dd9281a | -1.20408 | -55.70107 | 2026-10-08 05:23:00 | NPP-375D | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 43773886-ffb4-38a2-8abb-41b8cfceaa1d | -6.1215 | -51.95641 | 2026-10-08 05:23:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 4e6568ea-4854-3d00-9dfb-c23786f0b201 | -3.00381 | -54.11805 | 2026-10-08 05:23:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 6d3edee5-9739-3abf-b745-4ff115462565 | -3.27657 | -50.03352 | 2026-10-08 05:23:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| a8d2160c-9909-3058-850f-bbc7040a5afa | -2.58403 | -56.14809 | 2026-10-08 05:23:00 | NPP-375D | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| adbfe2d9-380a-39c8-af56-1709cafef7cf | -2.95664 | -59.31775 | 2026-10-08 05:23:00 | NPP-375D | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 34246408-e69a-36e3-beb3-08f442b3be86 | -3.89541 | -59.44695 | 2026-10-08 05:23:00 | NPP-375D | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 17acb454-7691-3c89-80a0-fc3dd82b94f7 | -3.08232 | -54.39882 | 2026-10-08 05:23:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 9262d5b4-ec0c-34fa-b796-157639e28ead | -3.09156 | -53.71627 | 2026-10-08 05:23:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 798d62f6-2d03-3096-a5ef-7c84f0673f47 | -2.13488 | -54.45927 | 2026-10-08 05:23:00 | NPP-375D | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| ea593194-73bb-356e-850c-4719e7212f5f | -11.75458 | -61.058 | 2026-10-08 05:23:00 | NPP-375D | PIMENTA BUENO | RONDÔNIA | Brasil | 1100189 | 11 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 17377da8-9841-3043-a7d0-8719104396d8 | -3.06934 | -54.25302 | 2026-10-08 05:23:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 72a23852-23b2-3df5-aa4e-d6a38ba7dc81 | -3.36397 | -50.48251 | 2026-10-08 05:23:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| f748f2ac-72a0-3478-a7c4-5253276f4148 | -1.10541 | -54.17177 | 2026-10-08 05:23:00 | NPP-375D | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 0415b5bd-c09c-3721-bdd8-dab79cea7872 | -3.02835 | -54.23602 | 2026-10-08 05:23:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 091d5f07-cbf2-396d-ae9b-d24e35c41841 | -3.40087 | -60.8462 | 2026-10-08 05:23:00 | NPP-375D | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| cdb79f1f-1576-39e4-9863-d4c27666fbae | -5.24369 | -50.90894 | 2026-10-08 05:23:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 10861702-681f-3779-8b83-5a722f8f99be | -9.1638 | -61.40573 | 2026-10-08 05:23:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 0633b70f-476d-3551-9e52-111d97d8ab32 | -3.26877 | -54.28712 | 2026-10-08 05:23:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 3aede9a7-923c-3575-8979-d8e2c9df6048 | -2.7739 | -54.06777 | 2026-10-08 05:23:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 74d0f0b6-4556-3f8e-908e-46d79c4afc13 | -4.11842 | -54.01552 | 2026-10-08 05:23:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 9fb696cc-074d-33b4-bd3e-5fc52fec11aa | -3.2846 | -54.00408 | 2026-10-08 05:23:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| d2eb0ca0-4f3a-3956-8777-2d7f423844fd | -3.86805 | -50.41002 | 2026-10-08 05:23:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 5.5 |
| d9915d1f-e412-3dd6-ba8b-e6327610b133 | -3.0769 | -54.25033 | 2026-10-08 05:23:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| e2047b8e-5594-3258-864e-2dced2e4df35 | -5.23573 | -56.11018 | 2026-10-08 05:23:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| a9b43cdb-8fd4-3cd4-ae3e-0e176df5d5e3 | -3.29441 | -54.03367 | 2026-10-08 05:23:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| d8b254df-f5c6-34b6-a698-2bfea53eb1eb | -6.14272 | -47.92316 | 2026-10-08 05:23:00 | NPP-375D | CACHOEIRINHA | TOCANTINS | Brasil | 1703826 | 17 | 33 | nan | nan | nan | Cerrado | 6.0 |
| 35bed975-1256-309c-a604-10850ff1669b | -3.75106 | -60.58935 | 2026-10-08 05:23:00 | NPP-375D | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 51f22dea-06e8-3c87-9f2b-f1e60ebd107c | -6.04222 | -51.73086 | 2026-10-08 05:23:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 3d8a63d4-212e-3f9c-8d45-d4bb8f3510f8 | -4.05903 | -59.83866 | 2026-10-08 05:23:00 | NPP-375D | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 6fae865d-f19b-358f-a44d-c7b7c10ace04 | -3.12303 | -53.79488 | 2026-10-08 05:23:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 11.0 |
| a8252f83-c780-3296-8f6b-0238fbcf5357 | -3.19759 | -50.56991 | 2026-10-08 05:23:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| cb9aea99-10b6-3005-aa93-0f714b88c711 | -4.26809 | -54.87605 | 2026-10-08 05:23:00 | NPP-375D | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 34d1a3f8-493b-3845-b339-ef1057dbc23d | -2.77793 | -54.08814 | 2026-10-08 05:23:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| a7a6c6da-d665-3d0b-b7ac-a6c3c06f5417 | -6.12572 | -53.06126 | 2026-10-08 05:23:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 70d0b8f5-58d2-316b-bd51-99b222193e70 | -3.18073 | -50.44918 | 2026-10-08 05:23:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| c4178e51-a220-3e29-a63d-7cce9a332264 | -3.51078 | -54.62857 | 2026-10-08 05:23:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 8f4219ea-54c4-3187-94d8-c3e1bb1490a5 | -2.57281 | -57.44945 | 2026-10-08 05:23:00 | NPP-375D | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 5125f178-425f-3f58-a832-b4cd73f7f489 | -3.41214 | -58.91215 | 2026-10-08 05:23:00 | NPP-375D | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 516ca299-e007-3c4d-8b70-4c6e37c36a36 | -4.44362 | -54.97875 | 2026-10-08 05:23:00 | NPP-375D | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 014cc49d-4d13-36be-9676-e7b404f34f5f | -1.47865 | -54.54718 | 2026-10-08 05:23:00 | NPP-375D | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| f5cf46de-a668-364d-95dd-3791f7f6c7f8 | -1.51131 | -54.82534 | 2026-10-08 05:23:00 | NPP-375D | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 350ae7c3-9738-3c9c-985f-f9a755e45780 | -2.61356 | -57.58288 | 2026-10-08 05:23:00 | NPP-375D | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| a8f9bdb1-f502-3d60-abf5-821f04b27f7e | -3.57928 | -54.65779 | 2026-10-08 05:23:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 2e90a607-985b-329c-bd08-0c3250b5ca72 | -3.0045 | -54.09043 | 2026-10-08 05:23:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 9.6 |
| ebc4e0be-f4d2-3210-9989-b12d7982e26d | -3.02572 | -53.9299 | 2026-10-08 05:23:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 11.6 |


[Clique aqui para ver as próximas entradas](README150.md)
