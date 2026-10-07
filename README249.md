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

## Dados Diários - Página 249

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 28ad8fb6-e4e4-3e89-bb5b-fb2cda2aa45c | -2.9271 | -53.9295 | 2026-10-07 18:30:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 68.1 |
| 68c1e3e8-b3cc-31cb-b23c-bb20c7226bb9 | -3.203 | -53.8823 | 2026-10-07 18:30:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 66.0 |
| c3b8c1b2-3706-3c2a-8abc-596809958c18 | -6.3163 | -43.3614 | 2026-10-07 18:30:00 | GOES-19 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 139.7 |
| 3a51c21a-d801-3451-a03b-056f3a37ec08 | -11.7335 | -43.649 | 2026-10-07 18:30:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 134.1 |
| 39a1e6e4-ef4f-3be0-aae3-1d835cb6a513 | -9.9589 | -43.5516 | 2026-10-07 18:30:00 | GOES-19 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 217.7 |
| 8ef01ff7-a27c-3296-9ca8-95c1917b0d63 | -12.0457 | -43.3864 | 2026-10-07 18:30:00 | GOES-19 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 121.1 |
| c98a262b-5ac8-3d63-b2a5-9c8f1d6fe227 | -9.8061 | -64.9979 | 2026-10-07 18:30:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 69.8 |
| e0c2bd1a-1267-3e11-935b-f261b776be0c | -3.1971 | -50.5801 | 2026-10-07 18:30:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 109.7 |
| 8e5bffeb-b034-3e62-b380-04566814e751 | -3.0605 | -58.4145 | 2026-10-07 18:30:00 | GOES-19 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 73.0 |
| 1f231820-35e6-3d66-96c1-78cf6f17e234 | -3.4731 | -55.4335 | 2026-10-07 18:30:00 | GOES-19 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 45.4 |
| 49525f9c-c37b-3c50-9364-754070b0f19e | -3.2213 | -53.9019 | 2026-10-07 18:30:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 48.6 |
| e71a67c8-9e22-3907-aa22-10cf5b6426b0 | -3.6611 | -54.2916 | 2026-10-07 18:30:00 | GOES-19 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 66.1 |
| 8e00488f-654f-3cc6-b53f-dedb474d3b1b | -9.1711 | -65.7682 | 2026-10-07 18:30:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 92.4 |
| 5aa41081-cb6a-3b98-a8b3-1a4bde1826c1 | -6.6784 | -52.9664 | 2026-10-07 18:30:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 61.9 |
| 5abd67e1-3e45-32fe-b87c-de81d897971a | -3.2398 | -53.8813 | 2026-10-07 18:30:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 58.8 |
| 9492261c-7895-3b57-b8e9-70d5d5377bd1 | -9.3395 | -65.4451 | 2026-10-07 18:30:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 71.4 |
| 3d88e66d-ca6c-3655-ab90-ad94d277c2d0 | -9.9596 | -43.5045 | 2026-10-07 18:30:00 | GOES-19 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 98.9 |
| e5cfcd47-4557-393b-bac0-6abd394d4e1a | -13.885 | -44.1365 | 2026-10-07 18:30:00 | GOES-19 | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 105.6 |
| 18d9a524-54e8-3191-beea-89fbe0a23b7f | -6.0075 | -53.5122 | 2026-10-07 18:30:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 61.2 |
| 00e3fd25-6f9e-33b6-ac3c-6e842a4ae621 | -6.1937 | -42.4785 | 2026-10-07 18:30:00 | GOES-19 | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | 213.4 |
| 07d500f0-7d30-3237-8080-58ebbaf90166 | -5.2473 | -50.9149 | 2026-10-07 18:30:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 80.8 |
| edaac226-bf65-3ace-b027-1e0949fa2b6f | -11.6181 | -43.6669 | 2026-10-07 18:30:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 71.4 |
| f8ce2780-2da7-390c-a1b1-01e5f581f0a3 | -1.8011 | -57.0967 | 2026-10-07 18:30:00 | GOES-19 | NHAMUNDÁ | AMAZONAS | Brasil | 1303007 | 13 | 33 | nan | nan | nan | Amazônia | 117.5 |
| 9b7d22b9-27aa-3250-a141-dfd1d27f2e8d | -9.1363 | -65.2835 | 2026-10-07 18:30:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 72.1 |
| 86bb45fb-bf57-392a-acc8-be5f69498db1 | -7.3085 | -73.0269 | 2026-10-07 18:30:00 | GOES-19 | GUAJARÁ | AMAZONAS | Brasil | 1301654 | 13 | 33 | nan | nan | nan | Amazônia | 94.0 |
| 3d2e3561-ef5b-38fc-877b-29dcbe17520a | -8.8696 | -67.0049 | 2026-10-07 18:30:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 88.8 |
| 44dcf0ea-d617-321e-9ce3-7602f178f97d | -5.7927 | -45.2626 | 2026-10-07 18:30:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 270.5 |
| 56681939-e812-3c36-bd1c-799a53c3ea74 | -5.6748 | -53.4879 | 2026-10-07 18:30:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 148.2 |
| 5d92fbda-3e6f-3097-9318-7eba8624d9b8 | -5.2288 | -50.9158 | 2026-10-07 18:30:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 55.1 |
| 90d896a0-8b65-3f0b-95c5-dec810f4157c | -4.2348 | -49.9749 | 2026-10-07 18:30:00 | GOES-19 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 49.7 |
| 8181e384-a6a4-3d53-b6d0-72ccd03fd4fe | -9.9787 | -43.502 | 2026-10-07 18:30:00 | GOES-19 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 123.1 |
| 768d91c9-0b69-37ed-8d72-80472d8810bc | -9.5469 | -64.8008 | 2026-10-07 18:30:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 62.3 |
| c6c85705-6edf-3f15-a6c6-ce3f86584e11 | -6.0181 | -49.5435 | 2026-10-07 18:30:00 | GOES-19 | CURIONÓPOLIS | PARÁ | Brasil | 1502772 | 15 | 33 | nan | nan | nan | Amazônia | 53.8 |
| 26af3037-5b39-326e-8401-a0ea2054ede9 | -6.9328 | -43.6799 | 2026-10-07 18:30:00 | GOES-19 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 93.1 |
| ca7aa68b-58fe-3c58-b899-c98aa9c8f67f | -6.0632 | -53.4891 | 2026-10-07 18:30:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 48.4 |
| 2da6da76-537f-336c-8fd1-61e509582a9e | -4.1039 | -54.0164 | 2026-10-07 18:30:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 49.3 |
| c332c3ee-7a14-358d-ac1e-3c4d79cacd0e | -3.2717 | -50.4102 | 2026-10-07 18:30:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 50.3 |
| 955bdd3c-72e2-317e-b95b-096c3a578982 | -5.2682 | -47.911 | 2026-10-07 18:30:00 | GOES-19 | SAMPAIO | TOCANTINS | Brasil | 1718808 | 17 | 33 | nan | nan | nan | Cerrado | 48.3 |
| db225164-bc5e-3dbf-8df7-0342fccbfa53 | -6.914 | -43.6816 | 2026-10-07 18:30:00 | GOES-19 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 101.8 |
| feb59706-5259-3a2a-b8b7-86d2bd18f312 | -2.5307 | -58.0956 | 2026-10-07 18:30:00 | GOES-19 | SÃO SEBASTIÃO DO UATUMÃ | AMAZONAS | Brasil | 1303957 | 13 | 33 | nan | nan | nan | Amazônia | 64.6 |
| 3d19963c-63fb-32ee-837f-cbeab139e0d6 | -5.6746 | -53.5082 | 2026-10-07 18:30:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 52.3 |
| 7a9e4346-74df-3246-a1ea-1a46c41ab516 | -5.8204 | -53.8457 | 2026-10-07 18:30:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 133.1 |
| ad07bf56-7605-31be-9ef4-b87b3a6b5351 | -2.0447 | -54.3085 | 2026-10-07 18:30:00 | GOES-19 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 119.4 |
| f0e1f4ec-f50b-34e0-8fb2-3be52defb367 | -3.1787 | -50.5597 | 2026-10-07 18:30:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 191.1 |
| cc8c4ff2-a1d5-3071-b7c6-44de6c066ebc | -6.8952 | -43.6833 | 2026-10-07 18:30:00 | GOES-19 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 281.5 |
| 5d0787d9-7193-3eab-8b13-d528ad08e901 | -9.8245 | -65.0348 | 2026-10-07 18:30:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 77.6 |
| 0de3e1ca-1634-32ff-9b91-641c2f3304bc | -8.8573 | -71.4625 | 2026-10-07 18:30:00 | GOES-19 | TARAUACÁ | ACRE | Brasil | 1200609 | 12 | 33 | nan | nan | nan | Amazônia | 107.7 |
| e7480e7b-9098-39c4-bf23-6c15dcbec464 | -3.7166 | -54.2096 | 2026-10-07 18:30:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 66.1 |
| 406cb8ba-812d-3396-bd59-0c20327f54de | -5.5148 | -42.8164 | 2026-10-07 18:30:00 | GOES-19 | TERESINA | PIAUÍ | Brasil | 2211001 | 22 | 33 | nan | nan | nan | Caatinga | 93.2 |
| 6cf37984-1c70-3d4f-abfb-b323562ceabc | -3.7481 | -51.2079 | 2026-10-07 18:30:00 | GOES-19 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 55.1 |
| 04143bf7-6ec1-3d0b-aa90-7fd251759873 | -9.4819 | -66.7836 | 2026-10-07 18:30:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 82.2 |
| 5dc7e76e-ee9c-3069-be8b-6856a8160684 | -7.47 | -42.8078 | 2026-10-07 18:30:00 | GOES-19 | FLORES DO PIAUÍ | PIAUÍ | Brasil | 2203800 | 22 | 33 | nan | nan | nan | Caatinga | 77.1 |
| 79b2262d-0135-3b47-baf0-c8af7e64510b | -8.5367 | -67.032 | 2026-10-07 18:30:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 111.1 |
| 7d4da3c2-82cb-3bef-a7ce-428bdba76625 | -3.1788 | -50.5388 | 2026-10-07 18:30:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 91.8 |
| 4c0be22c-0bb0-36d1-af5e-9ce8d887578e | -2.9327 | -58.3204 | 2026-10-07 18:30:00 | GOES-19 | SILVES | AMAZONAS | Brasil | 1304005 | 13 | 33 | nan | nan | nan | Amazônia | 263.7 |
| 002459c5-8f1c-38b7-bf5e-e97d840942ce | -8.2184 | -46.3396 | 2026-10-07 18:30:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 123.0 |
| f95bcd1e-4342-39bd-891e-55bcb12d5051 | -3.7296 | -51.2086 | 2026-10-07 18:30:00 | GOES-19 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 56.9 |
| 08f77bc7-436c-3f57-9416-c49f7623fab0 | -5.9647 | -40.9383 | 2026-10-07 18:30:00 | GOES-19 | ASSUNÇÃO DO PIAUÍ | PIAUÍ | Brasil | 2201051 | 22 | 33 | nan | nan | nan | Caatinga | 223.2 |
| 70383b9a-2cd8-3d6a-be94-202306936e41 | -5.7374 | -45.176 | 2026-10-07 18:30:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 38.7 |
| a7a32e97-54b1-3529-b66f-f299a120ad53 | -11.7143 | -43.652 | 2026-10-07 18:30:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 232.4 |
| 20de0099-e5ed-3366-b9b5-317155c4c8f8 | -4.3471 | -43.8021 | 2026-10-07 18:30:00 | GOES-19 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 120.3 |
| b82e17c6-0a82-39fa-9448-d590c5d9c7a0 | -7.1825 | -52.6283 | 2026-10-07 18:30:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 135.6 |
| cd170dcc-221f-323a-9853-02863c8aca7b | -9.0988 | -65.3596 | 2026-10-07 18:30:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 97.4 |
| 156e06e6-e3c3-393b-a1ae-360ebaefa026 | -4.2744 | -46.3846 | 2026-10-07 18:30:00 | GOES-19 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 135.8 |
| 27acbe46-74aa-3f3c-b6e8-8bc0bd1d2925 | -11.619 | -43.6196 | 2026-10-07 18:30:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 97.4 |
| 9b4a605a-dd43-3814-8f5f-2c6f77c5e3cd | -3.3134 | -53.8592 | 2026-10-07 18:30:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 113.7 |
| 575f5f38-2640-353b-8d4f-781a6003abe5 | -6.9925 | -45.1223 | 2026-10-07 18:30:00 | GOES-19 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 68.1 |
| 4bc666c2-2bf4-36c9-886b-700241eaa734 | -4.2859 | -50.7916 | 2026-10-07 18:30:00 | GOES-19 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 55.8 |
| f031222e-9b62-3e2b-a6c8-255b31565a2c | -3.1116 | -53.7436 | 2026-10-07 18:30:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 70.4 |
| c7d2e947-6b79-34da-8fed-2d80dcccf22d | -3.5865 | -54.5742 | 2026-10-07 18:30:00 | GOES-19 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 197.8 |
| 95bfde43-713a-316a-9b55-e68a10528d6c | -8.5183 | -67.0139 | 2026-10-07 18:30:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 115.8 |
| cf9ad54a-f27f-3ec1-bf5f-ed88b03fc382 | -9.96 | -43.481 | 2026-10-07 18:30:00 | GOES-19 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 105.5 |
| 32ea0f7d-6402-3203-ac04-079147bc7215 | -6.1974 | -52.8295 | 2026-10-07 18:30:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 54.4 |
| 60cfbdca-ec83-3fac-83af-6e044443ec5d | -11.6946 | -43.6787 | 2026-10-07 18:30:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 107.7 |
| 7a195985-52b8-3dd1-b360-ad193cfa304c | 1.7671 | -55.5661 | 2026-10-07 18:30:00 | GOES-19 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 60.8 |
| 2b820289-eca8-3a83-936e-68c6f2c5bc51 | -6.6037 | -53.0321 | 2026-10-07 18:30:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 187.6 |
| de308a52-b42a-32ae-8b51-dd8be7407b23 | -6.6599 | -52.9675 | 2026-10-07 18:30:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 110.5 |
| c0619ed8-cba4-3d61-92df-0249e1794db1 | -5.7659 | -42.0389 | 2026-10-07 18:30:00 | GOES-19 | SANTA CRUZ DOS MILAGRES | PIAUÍ | Brasil | 2209153 | 22 | 33 | nan | nan | nan | Caatinga | 159.3 |
| 1461fac6-c705-3eef-a3d5-a922898a0f84 | -13.3676 | -43.8504 | 2026-10-07 18:30:00 | GOES-19 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 108.5 |
| 45edac7f-072e-39ef-836f-f18ff23b2f7b | -3.4762 | -50.0883 | 2026-10-07 18:30:00 | GOES-19 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 117.4 |
| a9b8f8a4-9888-372f-b3fb-58ccab3d3a08 | -13.3671 | -43.8742 | 2026-10-07 18:30:00 | GOES-19 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 382.0 |
| e5f08dbb-2204-3af8-878c-c614d12758cf | -3.1301 | -53.7028 | 2026-10-07 18:30:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 53.6 |
| 81e433db-3ef9-3575-bf3a-ab38eaa43ffa | -9.6757 | -65.0401 | 2026-10-07 18:30:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 91.6 |
| 9787ec48-3d40-36da-a934-19e899928529 | -5.496 | -42.8178 | 2026-10-07 18:30:00 | GOES-19 | NAZÁRIA | PIAUÍ | Brasil | 2206720 | 22 | 33 | nan | nan | nan | Caatinga | 115.2 |
| 6da41073-78af-3a5a-8bd5-014ca8bc55a1 | -17.4361 | -43.6393 | 2026-10-07 18:30:00 | GOES-19 | OLHOS-D'ÁGUA | MINAS GERAIS | Brasil | 3145455 | 31 | 33 | nan | nan | nan | Cerrado | 133.4 |
| 9c22e637-871f-3948-97e9-08c98b3d86ae | -9.0406 | -65.9401 | 2026-10-07 18:30:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 158.7 |
| ea820798-ad3e-352a-a2cf-3f3d78f79d68 | -3.55 | -54.4952 | 2026-10-07 18:30:00 | GOES-19 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 65.0 |
| a3f4bf54-e3e0-396a-9623-0560d4487c61 | -9.8246 | -65.016 | 2026-10-07 18:30:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 79.3 |
| e89514a1-9fdf-388c-b6fc-26b008157e46 | -3.13 | -53.7229 | 2026-10-07 18:30:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 93.8 |
| 7a172408-7288-3af3-adbe-f7d7830423e1 | -6.2714 | -52.846 | 2026-10-07 18:30:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 147.4 |
| fd5ea0c8-5dd5-3fc6-9d09-d52aa317ab33 | -5.9649 | -40.914 | 2026-10-07 18:30:00 | GOES-19 | ASSUNÇÃO DO PIAUÍ | PIAUÍ | Brasil | 2201051 | 22 | 33 | nan | nan | nan | Caatinga | 132.3 |
| fb2ce885-2dc8-3242-a493-cd49349a02a9 | -5.4958 | -42.8413 | 2026-10-07 18:30:00 | GOES-19 | TERESINA | PIAUÍ | Brasil | 2211001 | 22 | 33 | nan | nan | nan | Caatinga | 275.0 |
| 1f8005c2-5d4e-3462-b760-f12465eeed4d | -6.2713 | -52.8665 | 2026-10-07 18:30:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 57.8 |
| 04059e5c-5a7d-37cb-be0a-4d1955ad703c | -4.2558 | -46.3855 | 2026-10-07 18:30:00 | GOES-19 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 90.0 |
| 4ced2f4e-9fd4-3734-b71f-ad95e400148d | -6.1502 | -39.4158 | 2026-10-07 18:30:00 | GOES-19 | ACOPIARA | CEARÁ | Brasil | 2300309 | 23 | 33 | nan | nan | nan | Caatinga | 144.3 |
| 47a96656-57da-349a-a6a1-eccceb49e6b8 | 1.6937 | -55.6263 | 2026-10-07 18:30:00 | GOES-19 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 91.0 |
| 41dd612b-ef39-3530-9946-14b67172cfca | -9.0987 | -65.3783 | 2026-10-07 18:30:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 81.7 |
| 2b5deb3b-6fff-3980-a0e6-a5812be603be | -11.2333 | -44.8678 | 2026-10-07 18:30:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 295.3 |
| e4873132-3133-336c-b45f-c85ed09fa9a6 | -11.6951 | -43.655 | 2026-10-07 18:30:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 102.8 |
| 64bb9305-519d-3ae4-bb8b-5fedb8f92d3f | -3.1951 | -42.9538 | 2026-10-07 18:30:00 | GOES-19 | SANTA QUITÉRIA DO MARANHÃO | MARANHÃO | Brasil | 2110104 | 21 | 33 | nan | nan | nan | Cerrado | 99.8 |


[Clique aqui para ver as próximas entradas](README250.md)
