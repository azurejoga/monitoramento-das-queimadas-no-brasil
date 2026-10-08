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

## Dados Diários - Página 142

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 387b828d-3681-3051-bc46-319d01e2d2db | -3.07737 | -54.29336 | 2026-10-08 05:23:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| e69d041d-0d43-384f-81a1-17c9abfc6b29 | -3.05866 | -54.22505 | 2026-10-08 05:23:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 31676b12-3fc5-3aeb-8637-5da02d78f852 | -3.6536 | -58.89088 | 2026-10-08 05:23:00 | NPP-375D | NOVA OLINDA DO NORTE | AMAZONAS | Brasil | 1303106 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 0a289740-354d-3efb-a281-462e15bc4633 | -3.51642 | -54.6601 | 2026-10-08 05:23:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 16598e63-ca8a-3fa2-8fa4-c9df1e7749de | -3.24688 | -56.81246 | 2026-10-08 05:23:00 | NPP-375D | PARINTINS | AMAZONAS | Brasil | 1303403 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 70cd121c-4027-3ad3-8fe3-ec3f01ff0d6a | -3.8744 | -55.99503 | 2026-10-08 05:23:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 94cdde69-c392-30f0-bbf8-d9f7340a33ad | -3.17816 | -58.63868 | 2026-10-08 05:23:00 | NPP-375D | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 697277ab-fc75-35f4-b6ef-1b96b64c3e85 | -3.50053 | -59.16807 | 2026-10-08 05:23:00 | NPP-375D | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 0fbec814-f3a2-30bd-8277-dfe991d273e6 | -3.17008 | -54.73308 | 2026-10-08 05:23:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| c42382bb-6c19-303c-a21a-0a5f2301458d | -5.68936 | -53.47864 | 2026-10-08 05:23:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 79d6891c-7016-33fd-a64c-ad034b73dfe0 | -3.03897 | -54.09972 | 2026-10-08 05:23:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 7e0456db-33f6-3e3a-888c-6863f7f5f5db | -8.14518 | -49.45029 | 2026-10-08 05:23:00 | NPP-375D | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 0aa26c21-a125-3bbd-be84-284889baf9f5 | -3.53585 | -59.47911 | 2026-10-08 05:23:00 | NPP-375D | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 990bd7f8-b569-39a0-9e05-efa7d21c0dff | -4.11636 | -59.876 | 2026-10-08 05:23:00 | NPP-375D | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 87d873f4-b618-31c7-bfc4-24df06759ff0 | -9.0433 | -65.93369 | 2026-10-08 05:23:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 046b2c8d-eab9-3996-90e0-5128199ce4b9 | -3.40928 | -58.90776 | 2026-10-08 05:23:00 | NPP-375D | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| f736b448-44a9-3b02-b3d7-1d50be701fa0 | -3.57924 | -54.68074 | 2026-10-08 05:23:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 15.6 |
| 9f9dcbd8-44ca-30db-94f3-8bcf71cfff00 | -2.47071 | -56.07381 | 2026-10-08 05:23:00 | NPP-375D | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 74bf0dff-efa7-3398-a8c9-ee8add84c606 | -4.27826 | -55.7663 | 2026-10-08 05:23:00 | NPP-375D | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 881a330f-fc02-3a9c-ba05-c9a319ac2cb0 | -2.48743 | -56.11895 | 2026-10-08 05:23:00 | NPP-375D | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 2a8b049b-e0e8-31ce-84a8-20206f051ed6 | -4.29551 | -54.80385 | 2026-10-08 05:23:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 991dc4bc-cabb-359c-bbf2-d76ed74d4f62 | -1.26548 | -55.39402 | 2026-10-08 05:23:00 | NPP-375D | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 7e1d4709-7232-322d-8696-868912b15f5a | -5.67443 | -46.35532 | 2026-10-08 05:23:00 | NPP-375D | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| b9275d98-a3a9-3858-a56e-4de4a844f343 | -2.93161 | -53.93161 | 2026-10-08 05:23:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 978d3a12-844e-3de0-9eb5-87390c287bfc | -4.14795 | -54.03645 | 2026-10-08 05:23:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| ced1af48-2034-3dda-84be-fe1b1e0e26db | -3.23021 | -53.8916 | 2026-10-08 05:23:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 4e48db6e-b5f1-3188-ae28-c29ebdb1956f | -2.77058 | -54.08393 | 2026-10-08 05:23:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| b742bb0f-0e7b-32df-bcfd-a57700c0299f | -3.26196 | -54.67839 | 2026-10-08 05:23:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 6.8 |
| a7bae473-1e1a-3eaf-b23a-c36ddf24cba3 | -3.51077 | -59.95095 | 2026-10-08 05:23:00 | NPP-375D | CAREIRO | AMAZONAS | Brasil | 1301100 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 93c3ce31-7b29-33bb-9397-7a9b558eef2c | -3.31758 | -54.0441 | 2026-10-08 05:23:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 6.2 |
| 5194414c-91ba-3c08-a8a3-035500e3818c | -2.81264 | -59.24679 | 2026-10-08 05:23:00 | NPP-375D | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 4390a290-6773-375f-8741-06fb9d336863 | -2.92831 | -58.30249 | 2026-10-08 05:23:00 | NPP-375D | SILVES | AMAZONAS | Brasil | 1304005 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 940c58f5-b661-3141-bccf-d98f911cb639 | -3.51423 | -54.62911 | 2026-10-08 05:23:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| e4e3cfb9-c562-3e70-b6db-9e311f29c668 | -2.98424 | -54.05569 | 2026-10-08 05:23:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| d59a201b-4ddb-3b0b-9179-a56b5de3dbe9 | -3.09188 | -54.29178 | 2026-10-08 05:23:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| b5ca39b9-1ee4-33f2-99e5-15852c34275a | -4.72694 | -56.15669 | 2026-10-08 05:23:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| b66d08a3-8036-3146-ae83-2d5c6dca8dd0 | -3.52113 | -54.63018 | 2026-10-08 05:23:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 5ecb1258-57aa-3231-a5bf-a74bf1a31039 | -2.90026 | -56.67613 | 2026-10-08 05:23:00 | NPP-375D | PARINTINS | AMAZONAS | Brasil | 1303403 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| c3fbe075-0f59-36b7-a169-e0461221fe0b | -4.1591 | -55.14569 | 2026-10-08 05:23:00 | NPP-375D | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| fdf8ebec-b283-3330-b751-8f118fb50e1e | -3.59779 | -61.63615 | 2026-10-08 05:23:00 | NPP-375D | ANAMÃ | AMAZONAS | Brasil | 1300086 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 97e9aa58-946a-387c-b114-2a6ad245d4ed | -3.31307 | -54.05262 | 2026-10-08 05:23:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 8.7 |
| 0c121c6e-fc4e-3cdd-bf32-db5ed4b10e92 | -3.99022 | -59.21925 | 2026-10-08 05:23:00 | NPP-375D | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| ba1f67db-5a52-3639-bb3d-f1c5862d917a | -3.1695 | -54.73678 | 2026-10-08 05:23:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 88cc8e65-804f-301a-832f-be760ca571c4 | -4.34288 | -43.79916 | 2026-10-08 05:23:00 | NPP-375D | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 10.0 |
| 3d10aed0-571e-3a0d-80d3-0e606c5b73b5 | -3.28399 | -54.008 | 2026-10-08 05:23:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| b47296b0-8c1f-32b1-bc8d-8ce800902b7a | -11.92311 | -46.79826 | 2026-10-08 05:23:00 | NPP-375D | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 4d3a230c-e7c1-3721-8851-ac0192a40f2d | -3.97981 | -56.22187 | 2026-10-08 05:23:00 | NPP-375D | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| c7c881e5-d585-39c1-8090-3f53abae829a | -3.12263 | -53.70461 | 2026-10-08 05:23:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 725fd043-fb53-3b3c-bede-ea3ce0653e01 | -3.40865 | -58.91159 | 2026-10-08 05:23:00 | NPP-375D | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| e8008718-1d7d-3ba1-8723-7d4266ebeb7e | -3.58817 | -54.5323 | 2026-10-08 05:23:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| b036dc37-6709-386d-a76c-b1ee293d8b20 | -11.94229 | -62.38172 | 2026-10-08 05:23:00 | NPP-375D | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 2.9 |
| e3a3f2a7-e3a8-3e97-83ba-40340792929e | -0.85319 | -51.8536 | 2026-10-08 05:23:00 | NPP-375D | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 9ed614d5-9bff-3b6a-87b0-8e91dd7eb733 | -6.291 | -56.03733 | 2026-10-08 05:23:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 0af21579-348a-30a5-81c9-02d873ea39c8 | -8.06162 | -44.81088 | 2026-10-08 05:23:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 4c456b6d-7394-3cab-a333-71edff11de14 | -6.13583 | -47.93258 | 2026-10-08 05:23:00 | NPP-375D | CACHOEIRINHA | TOCANTINS | Brasil | 1703826 | 17 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 45c72c13-aa38-3c69-b99d-a4c13733db8a | -4.93841 | -55.80673 | 2026-10-08 05:23:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 11192993-88cb-37bb-8a86-22c6c2a2bf2c | -3.54173 | -54.65632 | 2026-10-08 05:23:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 40281382-82dc-3d7e-afbe-e46b647d4e92 | -3.95884 | -56.1224 | 2026-10-08 05:23:00 | NPP-375D | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 44b04370-500b-347d-95bf-95402f5bd71c | -3.0161 | -54.24582 | 2026-10-08 05:23:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| c852e7a6-4ae4-3379-a94d-73a4e9720d3e | -3.94425 | -56.02008 | 2026-10-08 05:23:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| ff3c5eb9-4878-3c7d-9068-b207b019fc17 | -5.2977 | -60.09174 | 2026-10-08 05:23:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 67cc99f5-8cfb-3a34-97c1-2969b8c746e7 | -3.28446 | -59.41305 | 2026-10-08 05:23:00 | NPP-375D | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 3.2 |
| b6627bc6-fcef-386e-8405-061fd4c47d5d | -2.94768 | -54.19611 | 2026-10-08 05:23:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 0ba5aba3-5f2b-3402-b9fa-74f21307b768 | -3.07448 | -54.28902 | 2026-10-08 05:23:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 6b9d6c53-7b68-3ede-85e8-dd0a8131dacb | -3.58496 | -54.68927 | 2026-10-08 05:23:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 0e163b07-18f0-3c22-9869-f02531a51248 | -2.83112 | -59.24555 | 2026-10-08 05:23:00 | NPP-375D | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 049da254-c7ff-3e58-8710-e44e83c90446 | -4.39812 | -55.26805 | 2026-10-08 05:23:00 | NPP-375D | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 9d46e3d3-39f9-32d1-830a-caac538aaa57 | -6.62872 | -43.73882 | 2026-10-08 05:23:00 | NPP-375D | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 5.8 |
| f85796f5-7375-3037-9b01-afca3c854b99 | -3.58273 | -54.65831 | 2026-10-08 05:23:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 35b5f090-76c8-3f8a-9cf2-e63898b5f910 | -3.10534 | -57.65656 | 2026-10-08 05:23:00 | NPP-375D | BOA VISTA DO RAMOS | AMAZONAS | Brasil | 1300680 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 6af294c2-c384-3d5a-a776-a06126bb2055 | -2.84506 | -57.46675 | 2026-10-08 05:23:00 | NPP-375D | BOA VISTA DO RAMOS | AMAZONAS | Brasil | 1300680 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 2ed59e46-0b1a-3231-92fb-01c0f21cd783 | -4.93504 | -55.80619 | 2026-10-08 05:23:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| bd09b26d-7266-3372-b5a5-531e17f8ebe1 | -5.81918 | -53.82893 | 2026-10-08 05:23:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| a65e2578-aa22-3f3c-bf08-d62ac36ef048 | -3.53611 | -59.49987 | 2026-10-08 05:23:00 | NPP-375D | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| c9d394ad-894e-35f2-b662-c2f2a49ced73 | -3.12025 | -54.17839 | 2026-10-08 05:23:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 17.7 |
| 63bfc933-5f66-3158-a321-b704ab69b2e1 | -3.06527 | -54.25628 | 2026-10-08 05:23:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| f27e80f5-e225-3cf8-adf8-a3b22d0a7314 | -3.54593 | -54.66795 | 2026-10-08 05:23:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 68970d36-9649-3021-b281-2f7beb6077ea | -3.91457 | -59.10437 | 2026-10-08 05:23:00 | NPP-375D | NOVA OLINDA DO NORTE | AMAZONAS | Brasil | 1303106 | 13 | 33 | nan | nan | nan | Amazônia | 0.5 |
| e25dddd7-e52b-3c63-861c-161a83dafdb7 | -3.30487 | -54.69654 | 2026-10-08 05:23:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 403bd4be-20c7-3810-8e06-fcad1f609e16 | -3.56838 | -59.45954 | 2026-10-08 05:23:00 | NPP-375D | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| e38ba9f2-c1ab-3ea5-9559-b8a06b89c2f0 | -3.22715 | -54.3702 | 2026-10-08 05:23:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 2b1dabc5-10a7-3d11-8336-651a4ff89fe1 | -3.67829 | -55.94304 | 2026-10-08 05:23:00 | NPP-375D | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| e200c28f-7ca1-358d-bf9a-360cf54f940d | -6.74433 | -55.06592 | 2026-10-08 05:23:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 6d943fe8-781c-3ac7-974d-75f30e9a3b89 | -2.79373 | -54.07874 | 2026-10-08 05:23:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| a55b98b3-9a14-3fbb-9ea7-507c51dcb643 | -9.13671 | -65.29565 | 2026-10-08 05:23:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.3 |
| de9c4f70-d42e-37ca-b781-8fdcbb856021 | -4.77701 | -55.74216 | 2026-10-08 05:23:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 2ade7b4f-ee13-3e69-a098-183e97683c66 | -3.30628 | -53.86577 | 2026-10-08 05:23:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 941f421f-8e83-3983-b896-9d39eca8de05 | -3.04909 | -53.96569 | 2026-10-08 05:23:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 26.6 |
| bb0cc358-925e-3549-a214-c91a0e5d1568 | -3.06199 | -54.15866 | 2026-10-08 05:23:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| df524509-39f5-3b20-96c4-e8b4f85c2a54 | -2.56521 | -56.15931 | 2026-10-08 05:23:00 | NPP-375D | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 04b9c560-a088-3d49-ad4e-0989cbea5655 | -3.26031 | -50.39561 | 2026-10-08 05:23:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 1f24afce-f68d-3b21-ac59-80a6a6a192f5 | -2.94441 | -54.05748 | 2026-10-08 05:23:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 5dcdb4a4-80fb-3d9e-879b-449a5bcb877a | -7.20317 | -55.12544 | 2026-10-08 05:23:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| c2aa2746-5d40-3265-92af-0ec68aa47f1a | -2.98942 | -54.06842 | 2026-10-08 05:23:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| aa855e0c-970c-3e1e-b7a2-2462aa9ea069 | -3.40163 | -60.84142 | 2026-10-08 05:23:00 | NPP-375D | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 012f7513-bd3c-3bd7-8469-e68691e0f84d | -2.75556 | -57.68137 | 2026-10-08 05:23:00 | NPP-375D | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 34aef8c2-bfb8-3ddc-8125-65ac20aedc88 | -2.82282 | -54.09907 | 2026-10-08 05:23:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| b4060f1b-1452-32a1-aa47-a754d3c65ea1 | -4.76069 | -55.67042 | 2026-10-08 05:23:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 216008b3-b62b-3a79-8d76-cfab3d83adc5 | -3.36024 | -50.47765 | 2026-10-08 05:23:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| c0ae7b3c-d3a2-3c43-8a58-94ad55af7b42 | -3.08216 | -54.2394 | 2026-10-08 05:23:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |


[Clique aqui para ver as próximas entradas](README143.md)
