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

## Dados Diários - Página 52

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 691b5bee-2b87-3457-b9e1-950396ccfa43 | -3.65404 | -59.15873 | 2026-10-06 05:23:00 | NOAA-21 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| b286038b-3e9d-3fcb-8af8-15b248f4a696 | -2.79246 | -54.09392 | 2026-10-06 05:23:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| ed0abe44-2b30-3a1b-9983-2f85b3f69016 | -3.06254 | -59.26644 | 2026-10-06 05:23:00 | NOAA-21 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 6a1305a5-5fc8-33b7-b62d-d30772c22006 | -2.89889 | -59.20224 | 2026-10-06 05:23:00 | NOAA-21 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 30cd5a7b-9aa2-3dcd-89af-36cb01129e48 | -3.36198 | -59.41941 | 2026-10-06 05:23:00 | NOAA-21 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| d126d502-46d7-3436-9363-233e9ed9ccca | -3.05073 | -54.21894 | 2026-10-06 05:23:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| efb8e7b5-516e-3a95-a16d-2c698d5ee033 | -8.77824 | -62.8734 | 2026-10-06 05:23:00 | NOAA-21 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 4260678f-15a9-38fc-acda-6016eb4f5864 | -8.96983 | -65.44049 | 2026-10-06 05:23:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 332d1574-b29e-3baa-b5c6-936f349dcdf0 | -8.77891 | -63.0725 | 2026-10-06 05:23:00 | NOAA-21 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 670a25af-f918-36a2-9a71-e978f5770b45 | -1.61389 | -55.11868 | 2026-10-06 05:23:00 | NOAA-21 | CURUÁ | PARÁ | Brasil | 1502855 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 79a49134-b1b6-3c4b-92d6-61bc31bbbd2e | -2.77677 | -54.11169 | 2026-10-06 05:23:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| fca38212-8df1-3683-8d5a-c46199079a12 | -2.99043 | -54.13013 | 2026-10-06 05:23:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 90d585df-ae0a-3d21-87be-19e9ba7a2173 | -8.97818 | -65.43707 | 2026-10-06 05:23:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 7627c87c-754c-3996-b035-85870400d534 | -3.05438 | -54.22354 | 2026-10-06 05:23:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 7.7 |
| 22836eb9-45c0-3f66-b934-73b450c62e56 | -4.06283 | -56.33365 | 2026-10-06 05:23:00 | NOAA-21 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| deebf276-8667-3511-8fb0-51637c494309 | -3.08106 | -54.24772 | 2026-10-06 05:23:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 9.0 |
| c563ae85-08a5-3cdf-8527-f83078fbac96 | -3.23895 | -53.88296 | 2026-10-06 05:23:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| e2ad984c-8fd8-3765-acae-e33b7f4f173d | -3.09268 | -53.71295 | 2026-10-06 05:23:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 6.3 |
| 8584968a-c3a8-34b5-beea-6bb86b03e44b | -3.01262 | -57.74269 | 2026-10-06 05:23:00 | NOAA-21 | BOA VISTA DO RAMOS | AMAZONAS | Brasil | 1300680 | 13 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 063e05a8-1dd8-3be4-a2d5-c351493efcc2 | -2.88016 | -54.14346 | 2026-10-06 05:23:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 5.5 |
| d43292b5-95d7-3240-a8e2-457aafc967c4 | -2.9572 | -54.14919 | 2026-10-06 05:23:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 548b7e6f-df0f-3921-b158-874f1eab6cf2 | -8.62703 | -67.00159 | 2026-10-06 05:23:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 4b17b159-d306-3f42-9655-40857fceea47 | -2.98136 | -54.13267 | 2026-10-06 05:23:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 30.9 |
| 9d7a0c1f-39c1-32bf-a8ae-37c276b211ba | -2.78785 | -57.67486 | 2026-10-06 05:23:00 | NOAA-21 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 451f139d-5fd0-3278-89df-d5ed97956aa9 | -3.05323 | -54.23141 | 2026-10-06 05:23:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| fff38814-5ec1-36cb-a510-e98c9a2cb1bc | -2.95774 | -54.14706 | 2026-10-06 05:23:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 88a76a0e-d3ac-34a5-b98f-d394d0416079 | 1.86441 | -55.76696 | 2026-10-06 05:23:00 | NOAA-21 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 9bf0e633-4511-347d-84c0-508e4b3e4237 | -2.90068 | -54.12238 | 2026-10-06 05:23:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 2a9f58ec-329f-3fd1-bfa2-aacde7c88c6c | -3.37414 | -58.19748 | 2026-10-06 05:23:00 | NOAA-21 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 3.3 |
| a02184c2-553f-3b1d-ba3f-e5a07c2bb131 | -2.05417 | -56.88247 | 2026-10-06 05:23:00 | NOAA-21 | NHAMUNDÁ | AMAZONAS | Brasil | 1303007 | 13 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 66ff8491-fd74-3b32-8bd9-dcc9d0b96157 | -3.12096 | -53.70647 | 2026-10-06 05:23:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 326f9c72-08d8-3861-bca3-825e8dfeeea1 | -3.00742 | -54.13281 | 2026-10-06 05:23:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 13.5 |
| cb508876-699c-3577-b610-bf8ee4aa95b6 | -3.07933 | -54.2594 | 2026-10-06 05:23:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 7.7 |
| bcfae462-8067-3a8d-ab69-807e1393db85 | -4.1484 | -54.03292 | 2026-10-06 05:23:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 83705302-9e72-389b-baf1-2786c178fb2c | -2.13618 | -56.69858 | 2026-10-06 05:23:00 | NOAA-21 | FARO | PARÁ | Brasil | 1503002 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 837bb0b8-628b-3960-b798-8a1f506c3309 | -2.99645 | -54.11889 | 2026-10-06 05:23:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 3b69a085-92f2-38a7-adf8-45c8b8409cdc | -3.07158 | -54.1654 | 2026-10-06 05:23:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 57512b50-12bc-3bfb-92a2-dfc8cbb90c3a | -3.12667 | -53.75946 | 2026-10-06 05:23:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| dde6ab09-c747-3014-8ce8-0c853e3eb0d1 | -8.76442 | -63.68629 | 2026-10-06 05:23:00 | NOAA-21 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 0645a796-0d5a-32c8-bcc3-7ec7aeee674b | -2.9512 | -54.16054 | 2026-10-06 05:23:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| a19e1d7e-ea6e-38f3-9fe8-174a1f651153 | -3.10067 | -53.74887 | 2026-10-06 05:23:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| a06b4945-c4e3-3937-99e9-e621c5bcf828 | -3.49688 | -53.44232 | 2026-10-06 05:23:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| eb2e9a0e-2b6f-3b0b-a2dc-dee9a7ec83e6 | 1.56179 | -55.98093 | 2026-10-06 05:23:00 | NOAA-21 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 6.3 |
| 2b6d4aeb-95d7-3961-a956-795b84a738b0 | -3.37188 | -58.23472 | 2026-10-06 05:23:00 | NOAA-21 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 775920bb-3f5e-3f48-8f8e-e700f2ff287b | -2.86688 | -54.14532 | 2026-10-06 05:23:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 35e31fa8-e04d-3191-b4e5-4724a65b46a6 | -3.5484 | -59.48756 | 2026-10-06 05:23:00 | NOAA-21 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| d24ccb41-9843-3e09-8720-1cbd1a8294c3 | -3.08223 | -54.23987 | 2026-10-06 05:23:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 072bde1c-c48c-3d0b-9572-66b69e9db8fe | -3.10568 | -53.74533 | 2026-10-06 05:23:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| a9cf0fbb-8540-3f4f-a375-ccfd7625a5b0 | 3.08417 | -60.56752 | 2026-10-06 05:23:00 | NOAA-21 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 343582f5-651b-3d87-841b-84327071de87 | 3.07735 | -60.56856 | 2026-10-06 05:23:00 | NOAA-21 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 1.4 |
| f3120539-0cf4-3b6b-89a4-47a978cb7edd | 3.12802 | -60.5798 | 2026-10-06 05:23:00 | NOAA-21 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 0.8 |
| ccaa9f05-8394-3ad8-ac80-22715afc3782 | -9.51585 | -54.74167 | 2026-10-06 05:23:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 6f9271af-fbd1-3a51-a533-546fb89746ff | -3.05131 | -54.215 | 2026-10-06 05:23:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 99e0424f-4b31-3b36-afdf-0c4ea8d524f4 | -2.80406 | -54.13216 | 2026-10-06 05:23:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 8b087742-3730-3f60-8362-2ceb4fc182d0 | -2.98522 | -54.04751 | 2026-10-06 05:23:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 329378f2-7d43-3264-baa9-8de4a6ab5e3a | -3.02297 | -53.97038 | 2026-10-06 05:23:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 261f718b-ed48-3b2f-abe9-f17f4fed9ad4 | -2.95838 | -54.11473 | 2026-10-06 05:23:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 962ee592-67a9-394c-87be-47d4300580cd | -2.8064 | -54.08796 | 2026-10-06 05:23:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 262b373d-924d-31f5-9cfc-a32ef1bb7673 | -3.46479 | -50.10662 | 2026-10-06 05:23:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 19d17286-2b8b-3983-a1b9-54011a954548 | -3.71385 | -51.14031 | 2026-10-06 05:23:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 4621f4ec-5834-3eef-91a0-3cab29593e82 | -1.12635 | -57.27802 | 2026-10-06 05:23:00 | NOAA-21 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 4b9011df-e482-3cdb-a2d0-b3d386b2c419 | -2.78846 | -51.67053 | 2026-10-06 05:23:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| ae5fde1b-7759-3195-83ab-b3e090826c51 | -8.78897 | -62.94604 | 2026-10-06 05:23:00 | NOAA-21 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| b0224330-302f-31a0-95d7-bf802b75f620 | -3.03971 | -54.2648 | 2026-10-06 05:23:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| e105db92-dbe1-306c-828b-dc8c6f0fa172 | -3.72036 | -48.88438 | 2026-10-06 05:23:00 | NOAA-21 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| b156f5f5-7347-3607-8db8-c6b6633463dd | -2.53991 | -58.03054 | 2026-10-06 05:23:00 | NOAA-21 | SÃO SEBASTIÃO DO UATUMÃ | AMAZONAS | Brasil | 1303957 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 224280a9-db7a-30a5-81b7-adabd16af960 | -1.80542 | -53.75325 | 2026-10-06 05:23:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 6e44c417-ed35-30a3-bbf0-3363c3420fc0 | -3.00742 | -57.75352 | 2026-10-06 05:23:00 | NOAA-21 | BOA VISTA DO RAMOS | AMAZONAS | Brasil | 1300680 | 13 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 940822b2-1e92-3927-8630-bf90451f8d94 | 2.4537 | -50.83582 | 2026-10-06 05:23:00 | NOAA-21 | CALÇOENE | AMAPÁ | Brasil | 1600204 | 16 | 33 | nan | nan | nan | Amazônia | 9.3 |
| b9f75f0a-2333-3a3c-b94d-ebcb197ccc3c | -4.29351 | -54.8017 | 2026-10-06 05:23:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| df52e181-f5db-30da-9652-3df500f46153 | -3.11234 | -53.76586 | 2026-10-06 05:23:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 436c6610-2a55-33ba-a9ab-d87d08edce7e | -3.08763 | -59.19215 | 2026-10-06 05:23:00 | NOAA-21 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 4d88936f-dc6c-383d-9713-0cd42ee7bcd5 | -3.6123 | -55.47508 | 2026-10-06 05:23:00 | NOAA-21 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 16072171-d940-3657-aac4-70af305bcfcc | -9.00613 | -62.10128 | 2026-10-06 05:23:00 | NOAA-21 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 180c8dca-263c-3b5d-b33d-a2355980e975 | -3.37187 | -58.1896 | 2026-10-06 05:23:00 | NOAA-21 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 4.1 |
| b575b056-4ff1-3282-8c90-3d9eb493cf06 | 3.06595 | -60.58542 | 2026-10-06 05:23:00 | NOAA-21 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 6.9 |
| 2646c7d9-ce03-3ce3-a4b7-b2a4ee2eea37 | -8.54444 | -66.97934 | 2026-10-06 05:23:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 57286ebe-549b-3685-9b71-d628e00d598a | -3.08432 | -54.16733 | 2026-10-06 05:23:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| f59b177e-4cda-3d72-9c73-c100ed436ec4 | -2.83782 | -59.24603 | 2026-10-06 05:23:00 | NOAA-21 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 85e83ace-33fb-3863-ad54-8ba6381af0fa | -3.73048 | -57.14925 | 2026-10-06 05:23:00 | NOAA-21 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| d3936411-5d5d-34b3-bbc9-6ccda79ecc5e | -2.80215 | -54.0873 | 2026-10-06 05:23:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 70e99420-6d23-3b69-a0fa-9b026a49ad30 | -3.16224 | -50.60447 | 2026-10-06 05:23:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 05b69668-a584-306e-bcfc-d8be63549863 | -2.94924 | -54.14587 | 2026-10-06 05:23:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| c2c29bd4-fcff-37bf-86e4-717280ad78c8 | -3.73439 | -48.87223 | 2026-10-06 05:23:00 | NOAA-21 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 5.6 |
| 522017c8-7b91-3974-8a52-008fa0d5d693 | -3.10015 | -53.72279 | 2026-10-06 05:23:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| cac26b0d-c0f2-37b4-90a6-d74a8499ee8e | -3.73368 | -48.87701 | 2026-10-06 05:23:00 | NOAA-21 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 5.6 |
| d151e17d-fc9c-3f92-b75c-192486b1cfaf | -3.04569 | -54.22359 | 2026-10-06 05:23:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| b104cbbb-1016-3195-bb71-fe4751c71d79 | -3.05418 | -54.16836 | 2026-10-06 05:23:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| e6df3aa7-16e2-3266-9e30-502e2fea801c | -3.07627 | -54.25092 | 2026-10-06 05:23:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 13.8 |
| 7e1d6f41-d612-3d5e-aa0a-c1932fce99f0 | -2.90255 | -54.13882 | 2026-10-06 05:23:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 18af85f3-402b-3a57-bdd7-015c2c0f1343 | -2.7605 | -54.66772 | 2026-10-06 05:23:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 67e863e9-77be-364f-b860-ce47451486ff | -3.28085 | -50.01747 | 2026-10-06 05:23:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 79a158bd-1ee4-3572-bfbc-7f2a5f1dc6d5 | -2.99527 | -54.12683 | 2026-10-06 05:23:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 3eb295cc-e762-348a-b5b3-ba6c8639b1bc | -3.04508 | -54.22752 | 2026-10-06 05:23:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 03f75b4c-1248-38a1-a749-d130a3521e42 | -3.55265 | -59.48468 | 2026-10-06 05:23:00 | NOAA-21 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 4f5d7021-1831-3735-9d3e-d8ab6aaf7e0b | -2.94135 | -54.14067 | 2026-10-06 05:23:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| a35e5e17-13e0-3d69-967a-40fae601d2d3 | -3.23645 | -53.86976 | 2026-10-06 05:23:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 34dcf038-8fc9-3a21-9263-cc9dbbfa94a9 | -3.45815 | -54.59511 | 2026-10-06 05:23:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 26f32945-18c2-3fb4-b594-84b34613e08b | -3.45914 | -50.10576 | 2026-10-06 05:23:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| c9eb72e3-c927-329a-9a2a-bcbe696478d1 | -3.10259 | -53.7362 | 2026-10-06 05:23:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |


[Clique aqui para ver as próximas entradas](README53.md)
