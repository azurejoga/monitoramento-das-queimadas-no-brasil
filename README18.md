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

## Dados Diários - Página 18

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| ba2e5d87-f128-3f22-b298-5df9178a014b | -3.073 | -54.2674 | 2026-10-06 03:10:00 | GOES-19 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 53.2 |
| 1ffe4527-f28d-347a-a83e-9992aff8af00 | -3.6731 | -55.9622 | 2026-10-06 03:10:00 | GOES-19 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 62.8 |
| 1b279a93-64e5-3825-a2c7-624bf6eca4ce | -3.0375 | -53.9066 | 2026-10-06 03:10:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 54.2 |
| bc7dbae0-b75b-3cce-bec8-7e5683cd6a4b | -3.0734 | -54.147 | 2026-10-06 03:10:00 | GOES-19 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 53.4 |
| f46afad6-81c4-3e91-a241-2ccd13900d12 | -3.0731 | -54.2473 | 2026-10-06 03:10:00 | GOES-19 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 156.8 |
| 2adc788e-3d58-3262-8db1-500c7839a388 | -11.2607 | -45.5078 | 2026-10-06 03:10:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 122.1 |
| 3dc7322c-3c35-332f-9262-79b4b326a3db | -3.0734 | -54.167 | 2026-10-06 03:10:00 | GOES-19 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 82.1 |
| 2a7fd596-5389-3bc1-80a5-49fb165e98ee | -3.0917 | -54.1666 | 2026-10-06 03:10:00 | GOES-19 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 123.6 |
| 69875cb5-c88c-3bd0-b58d-a58fa84bf775 | -11.2802 | -45.4823 | 2026-10-06 03:10:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 71.4 |
| 08b38e52-2880-3e7c-ae94-8dd01bd15932 | -2.9448 | -54.1501 | 2026-10-06 03:10:00 | GOES-19 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 74.8 |
| d58b946a-4fea-3653-b7bd-7e80d6bc1d15 | -3.0917 | -54.1867 | 2026-10-06 03:10:00 | GOES-19 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 65.0 |
| 4c022e55-3229-338e-90c8-19e55c8d55f3 | -3.0731 | -54.2473 | 2026-10-06 03:20:00 | GOES-19 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 106.8 |
| 1533c023-df52-3250-ad8e-3e7eb2bbd24e | -3.0548 | -54.2076 | 2026-10-06 03:20:00 | GOES-19 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 71.1 |
| 38807d5c-6b08-30ec-a1f0-657a0f9b20c0 | -3.6731 | -55.9622 | 2026-10-06 03:20:00 | GOES-19 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 63.6 |
| f28d3bbf-2aa7-3ba2-902b-d40e5c598855 | -2.7879 | -57.6843 | 2026-10-06 03:20:00 | GOES-19 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 92.6 |
| fbaeac58-403b-31f5-a30a-929ae5df20ff | -11.2794 | -45.5281 | 2026-10-06 03:20:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 59.1 |
| 99f38e1e-c072-3cf2-9ead-1320e7f2e899 | -3.0375 | -53.8865 | 2026-10-06 03:20:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 76.8 |
| 4d5a12b8-cbe7-3a27-8885-a31df915d166 | -3.1101 | -54.1661 | 2026-10-06 03:20:00 | GOES-19 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 53.1 |
| f510eb6d-54cd-3d3c-b9de-adb9668dce4c | -3.6732 | -55.9425 | 2026-10-06 03:20:00 | GOES-19 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 69.9 |
| eba13b12-0817-39e0-afbe-cb842af6e5bb | -3.0375 | -53.9066 | 2026-10-06 03:20:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 66.5 |
| 7d237b6c-b672-31e5-8aed-5ee3aa3d4a58 | -9.7312 | -65.0944 | 2026-10-06 03:20:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 75.5 |
| 7d57eb31-2496-3a69-bf8f-df1085c0a2f5 | -11.2798 | -45.5052 | 2026-10-06 03:20:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 235.9 |
| 29d49413-2b06-3ebb-9334-adfc6f933f50 | -3.6915 | -55.9618 | 2026-10-06 03:20:00 | GOES-19 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 61.9 |
| b099a145-8852-3e65-98c2-e00e6d8bd326 | -11.2607 | -45.5078 | 2026-10-06 03:20:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 121.1 |
| 7d152fe1-66df-3e20-ba10-9759939ef94b | -3.0548 | -54.2277 | 2026-10-06 03:20:00 | GOES-19 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 81.7 |
| 9e5e609a-70ea-3fc3-a01f-7a8d3996f57f | -2.9816 | -54.1291 | 2026-10-06 03:20:00 | GOES-19 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 55.5 |
| 6eb63b29-3069-3b7d-8a0c-887e7ded2d9d | -11.299 | -45.5025 | 2026-10-06 03:20:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 65.3 |
| 1616a7c5-8c0d-30ef-b660-90b98b03925d | -3.0734 | -54.167 | 2026-10-06 03:20:00 | GOES-19 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 76.9 |
| 71745da6-0c6f-39ba-85df-7e55d23fbc86 | -3.0 | -54.1287 | 2026-10-06 03:20:00 | GOES-19 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 81.4 |
| 427c4ffd-c4b0-3e0e-835e-db35ac899db0 | -3.0192 | -53.887 | 2026-10-06 03:20:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 86.2 |
| c88e9619-afa8-34b5-a9fa-c5d1c7212e2f | -3.6915 | -55.942 | 2026-10-06 03:20:00 | GOES-19 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 55.7 |
| 46ad20ab-3239-3252-8912-229166fb5361 | -3.0932 | -53.7239 | 2026-10-06 03:20:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 87.2 |
| 347c3942-5eb2-319b-b535-fd7a0149e818 | -2.8714 | -54.1318 | 2026-10-06 03:20:00 | GOES-19 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 66.4 |
| 2cc0715d-7420-3b89-8e33-1af8170c618b | -3.0917 | -54.1867 | 2026-10-06 03:20:00 | GOES-19 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 72.5 |
| e2f54436-3dcf-3519-bbdb-0aed24688071 | -2.8713 | -54.1518 | 2026-10-06 03:20:00 | GOES-19 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 84.6 |
| 830ef594-57e6-3726-b824-e6f3ce946bf0 | -2.9448 | -54.1501 | 2026-10-06 03:20:00 | GOES-19 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 71.5 |
| 8925111b-1f89-31bc-8943-1ce52f6a8569 | -5.8511 | -45.0091 | 2026-10-06 03:20:00 | GOES-19 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 76.7 |
| 3e4155c6-d2b8-346b-bd2f-e28c5381b8e4 | -2.9449 | -54.13 | 2026-10-06 03:20:00 | GOES-19 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 61.7 |
| 07ff869e-5be8-3cd3-90bc-51f99d8a3816 | -3.0732 | -54.2273 | 2026-10-06 03:20:00 | GOES-19 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 61.6 |
| e39a460f-1b2b-3357-937a-122588fc4491 | -3.0917 | -54.1666 | 2026-10-06 03:20:00 | GOES-19 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 119.8 |
| 740f0e2e-2599-382b-8ad7-498db744efb4 | -2.7796 | -54.0937 | 2026-10-06 03:20:00 | GOES-19 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 56.0 |
| d7485ee7-76b4-3384-86f7-2a332e117855 | -5.8323 | -45.0105 | 2026-10-06 03:20:00 | GOES-19 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 110.5 |
| ef6a1a78-08a3-3848-85df-56d1d79ca6e7 | -3.0915 | -54.2469 | 2026-10-06 03:20:00 | GOES-19 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 64.7 |
| 6116a085-e8fc-33aa-b65e-5f0bcad4a48d | -2.9265 | -54.1305 | 2026-10-06 03:20:00 | GOES-19 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 61.6 |
| efde6d02-2832-3533-93fa-f111010e68af | -3.0191 | -53.9071 | 2026-10-06 03:20:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 73.4 |
| c6243546-cdc7-312a-b11e-81a8e01e2d6e | -3.0932 | -53.7441 | 2026-10-06 03:20:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 61.4 |
| 54be1902-2135-3768-84e6-c0a4fb58a010 | -11.2802 | -45.4823 | 2026-10-06 03:20:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 93.0 |
| a7b9ee2b-729b-3496-ba10-473a2057e18f | -3.1115 | -53.7637 | 2026-10-06 03:20:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 73.5 |
| acfb7bcb-e835-37c1-87a6-8a8d23fe4ce4 | -11.2611 | -45.4849 | 2026-10-06 03:20:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 61.8 |
| 9caca907-0d72-37db-8834-dabc240465ff | -3.0 | -54.1287 | 2026-10-06 03:30:00 | GOES-19 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 83.3 |
| d708e619-b4a1-3cb7-b1e7-8d4e3da89523 | -9.7312 | -65.0944 | 2026-10-06 03:30:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 246.9 |
| de1c0f63-ee80-3da1-add4-ef8381af9318 | -2.9448 | -54.1501 | 2026-10-06 03:30:00 | GOES-19 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 68.4 |
| eab449c2-c358-3837-b217-52c622d7a8e7 | -3.6731 | -55.9622 | 2026-10-06 03:30:00 | GOES-19 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 75.8 |
| d0f2dc89-9dfa-3bc7-a6a0-7da071bbbc1a | -9.7313 | -65.0757 | 2026-10-06 03:30:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 105.5 |
| 085c31b3-1fe3-35de-9374-f5a354fe5708 | -3.0932 | -53.7441 | 2026-10-06 03:30:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 63.8 |
| 784a8f42-8fae-3bac-bfcb-0529d9f0e4d1 | -2.9265 | -54.1305 | 2026-10-06 03:30:00 | GOES-19 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 62.7 |
| 3af95d96-52b9-3e99-8f59-f5dbb978b507 | -2.9449 | -54.13 | 2026-10-06 03:30:00 | GOES-19 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 56.0 |
| 499852ff-362a-3594-a39c-7fff19837eef | -3.0932 | -53.7239 | 2026-10-06 03:30:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 83.2 |
| cc30d3e1-30f1-301a-ad62-6807e3598b47 | -9.7126 | -65.0951 | 2026-10-06 03:30:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 57.3 |
| 47083120-0f33-38d9-af46-873dc57d2481 | -2.9816 | -54.1291 | 2026-10-06 03:30:00 | GOES-19 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 56.2 |
| 2bd64417-4b3e-33f9-82ab-d826452ece6a | -3.0375 | -53.9066 | 2026-10-06 03:30:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 106.9 |
| 448af1da-5e1b-3f75-a24c-bdb63b1de2b2 | -3.6915 | -55.9618 | 2026-10-06 03:30:00 | GOES-19 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 68.7 |
| f48f5074-c456-382c-9d25-4622a357010e | -3.0191 | -53.9071 | 2026-10-06 03:30:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 121.5 |
| 4f725fae-5690-37e4-b340-c66813d2fe87 | -3.0192 | -53.887 | 2026-10-06 03:30:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 92.2 |
| cf29062e-8713-3042-b5ca-916b6700c1f1 | -3.0375 | -53.8865 | 2026-10-06 03:30:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 82.4 |
| 580c09e5-6741-3982-8efd-5d628f24cf91 | -5.8323 | -45.0105 | 2026-10-06 03:30:00 | GOES-19 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 90.7 |
| dbb5014c-7538-3b1d-8858-7e94b93d3064 | -9.7311 | -65.1132 | 2026-10-06 03:30:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 55.3 |
| 7bcf67ba-7d3a-3a5f-b596-5e7c009b6077 | -2.8713 | -54.1518 | 2026-10-06 03:30:00 | GOES-19 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 81.0 |
| 27358220-d416-3491-aaa9-34c788be49ad | -5.8511 | -45.0091 | 2026-10-06 03:30:00 | GOES-19 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 68.9 |
| adf141e4-4d17-388d-aef6-9ef6a0b75870 | -3.6732 | -55.9425 | 2026-10-06 03:30:00 | GOES-19 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 68.8 |
| 7a0d348b-6361-3327-a4dd-ceb3cb4c0dc8 | -2.7879 | -57.6843 | 2026-10-06 03:30:00 | GOES-19 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 72.5 |
| 7278bbcd-06b3-3d4a-a21e-50391a62fb28 | -2.7796 | -54.0937 | 2026-10-06 03:30:00 | GOES-19 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 51.9 |
| 1fe5756c-fcfc-397f-80fa-1efd731ab3c4 | -3.3723 | -58.1957 | 2026-10-06 03:30:00 | GOES-19 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 69.7 |
| 1f88fa82-277a-3d7e-b2de-b060c2979ecf | -2.8714 | -54.1318 | 2026-10-06 03:30:00 | GOES-19 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 58.4 |
| b496b36a-6f3c-35af-a446-3c51f547249a | -3.1115 | -53.7637 | 2026-10-06 03:30:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 71.6 |
| 7400ec35-6c94-304b-8efb-670183282d3a | -9.7498 | -65.0938 | 2026-10-06 03:30:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 45.6 |
| d1d1b699-9294-3aeb-8cb0-a14944356632 | -2.8897 | -54.1514 | 2026-10-06 03:40:00 | GOES-19 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 54.3 |
| 8eac46fe-502c-3722-807a-5ac807bd74d9 | -3.0191 | -53.9071 | 2026-10-06 03:40:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 62.0 |
| da154cee-9b6e-3a49-b48f-43f5b8006fa4 | -5.8511 | -45.0091 | 2026-10-06 03:40:00 | GOES-19 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 65.2 |
| f433af35-1071-3685-abf5-2c93f5fde244 | -3.0932 | -53.7239 | 2026-10-06 03:40:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 74.2 |
| 03f5a019-0f11-3dfb-b4ba-b0b619646cac | -9.7313 | -65.0757 | 2026-10-06 03:40:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 54.3 |
| 5ebe03c9-e2e2-3f65-bd33-1aacd03daa4a | -9.7126 | -65.0951 | 2026-10-06 03:40:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 66.4 |
| 84a387de-d31b-3ca2-a7e1-6360a39db54a | -9.7312 | -65.0944 | 2026-10-06 03:40:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 131.7 |
| c144834e-af2b-309d-8a1a-421df85be92a | -2.8713 | -54.1518 | 2026-10-06 03:40:00 | GOES-19 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 75.4 |
| 03d765aa-5245-3b70-850e-accd4c65638d | -3.0932 | -53.7441 | 2026-10-06 03:40:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 60.1 |
| 325e796d-dfb4-3cb0-8a49-9cd501a3849d | -2.9265 | -54.1305 | 2026-10-06 03:40:00 | GOES-19 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 58.3 |
| e955c92f-8c5d-34b2-8ffe-947f2e0a8b3b | -3.6915 | -55.942 | 2026-10-06 03:40:00 | GOES-19 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 58.8 |
| fe562a31-5612-3313-83a9-8355e34c2e46 | -3.6731 | -55.9622 | 2026-10-06 03:40:00 | GOES-19 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 64.7 |
| 3bb8feb2-cc06-3a4e-87c2-472758572e1a | -3.0192 | -53.887 | 2026-10-06 03:40:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 59.6 |
| 26d23217-9902-36e6-9bf1-003d99a31d11 | -5.8323 | -45.0105 | 2026-10-06 03:40:00 | GOES-19 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 84.1 |
| e775b3ec-840d-3780-961e-15e94e6924d0 | -3.1115 | -53.7637 | 2026-10-06 03:40:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 61.1 |
| e713ed47-af0a-3f30-8f42-921645ec5717 | -2.9448 | -54.1501 | 2026-10-06 03:40:00 | GOES-19 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 67.5 |
| 7ee291a5-a319-36d8-a160-de03c679b112 | -3.6732 | -55.9425 | 2026-10-06 03:40:00 | GOES-19 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 61.2 |
| a49514c0-efb1-3bee-b4ce-f84ac8611eb6 | -3.6915 | -55.9618 | 2026-10-06 03:40:00 | GOES-19 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 77.4 |
| b3946af6-399c-31c2-8f57-e3747c765506 | -3.0 | -54.1287 | 2026-10-06 03:40:00 | GOES-19 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 64.7 |
| 65a63bc7-65ba-34f9-8d44-7f9324f3bb2c | -3.39736 | -44.48636 | 2026-10-06 03:42:00 | NOAA-21 | ITAPECURU MIRIM | MARANHÃO | Brasil | 2105401 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| accc1759-c6d0-32db-b680-36b98dfca0ce | -5.84726 | -45.0168 | 2026-10-06 03:42:00 | NOAA-21 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 13.3 |
| 0f65d3a7-9c51-3fe5-b92f-cad2c531c4e5 | -5.60259 | -45.37317 | 2026-10-06 03:42:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 4ff3e6b8-5e3f-3f43-80a4-8fb3680ffc6b | -5.43599 | -43.44301 | 2026-10-06 03:42:00 | NOAA-21 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 2d398022-e60e-3c00-872f-40536b42dc33 | -4.72229 | -44.0852 | 2026-10-06 03:42:00 | NOAA-21 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |


[Clique aqui para ver as próximas entradas](README19.md)
