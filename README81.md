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

## Dados Diários - Página 81

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| bd5b2d27-cd5d-3dc8-9c63-2767b25bc90f | -6.86703 | -51.98781 | 2024-11-24 05:16:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| f6e1e45b-7d04-32ce-9720-ef9eeb2a9353 | -3.33826 | -54.62366 | 2024-11-24 05:16:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 5c634a82-80fb-3c00-bb21-c14bc943b32c | -3.25772 | -54.2156 | 2024-11-24 05:16:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 8fcc5f76-087d-3bcf-86aa-555476de2a21 | -4.03315 | -54.18863 | 2024-11-24 05:16:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| fad96423-5b9c-38f4-9ec2-c23b5dff85ef | -4.25981 | -48.69667 | 2024-11-24 05:16:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| f63e52c8-1cf2-3cdb-856d-7e4c56aa4160 | -3.52189 | -53.51374 | 2024-11-24 05:16:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 96dce220-0923-3894-b12b-fad6b4c3401e | -5.1931 | -49.15165 | 2024-11-24 05:16:00 | NPP-375D | NOVA IPIXUNA | PARÁ | Brasil | 1504976 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| fa9ab51c-bbe8-374d-a906-f5447fb24780 | -3.82525 | -52.23551 | 2024-11-24 05:16:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 4c61e962-6d9e-3e73-a8c8-92b13e626d69 | -4.16536 | -54.57943 | 2024-11-24 05:16:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| cb285042-d5a2-3ab0-bd2b-1cc935330604 | -5.95342 | -48.04318 | 2024-11-24 05:16:00 | NPP-375D | SÃO BENTO DO TOCANTINS | TOCANTINS | Brasil | 1720101 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 7a426f1d-a00f-38e3-84b8-9e813e5629a3 | -3.61154 | -54.74215 | 2024-11-24 05:16:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| cc4aa670-4117-3010-a6d7-15044d89c4de | -3.52584 | -53.5144 | 2024-11-24 05:16:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 0832e6e9-f7d5-3f58-9048-bfe0e7832513 | -3.24357 | -54.23202 | 2024-11-24 05:16:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| ae6e4db5-87f6-3fff-9295-f28acfa5dbcf | -4.12867 | -54.2082 | 2024-11-24 05:16:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 8e76edf9-fd6f-3d7d-91fd-89430600949f | -3.57849 | -54.51314 | 2024-11-24 05:16:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| a3b0b64e-c09c-32f7-a3cc-11525ef4e4d9 | -3.97691 | -49.931 | 2024-11-24 05:16:00 | NPP-375D | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| ce7e0311-1b96-371a-aaf0-ddb2bb21b488 | -3.25324 | -54.21953 | 2024-11-24 05:16:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| e328a26a-4e4f-359b-bfee-f8ddb363f96e | -4.53311 | -46.42586 | 2024-11-24 05:16:00 | NPP-375D | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 85a2d2c2-ce82-3b02-b460-1b052e596937 | -3.2497 | -54.24227 | 2024-11-24 05:16:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| a94e0304-8fc9-31af-a542-672f2df6f433 | -4.53376 | -46.42657 | 2024-11-24 05:16:00 | NPP-375D | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 484c8155-93d4-3f2c-942a-dd7cb79988c6 | -3.18544 | -54.76929 | 2024-11-24 05:16:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 65823203-668c-3c71-9689-25ff0777c03f | -4.89107 | -48.9087 | 2024-11-24 05:16:00 | NPP-375D | BOM JESUS DO TOCANTINS | PARÁ | Brasil | 1501576 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 1ff75e84-7a83-3ed1-a00b-fe3b0ed7b8c5 | -3.51334 | -53.80696 | 2024-11-24 05:16:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| d8d04cf3-e8f8-329a-9811-e39427ae862a | -3.57714 | -54.52206 | 2024-11-24 05:16:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| aadc7324-9964-321d-8056-247dc4a184d1 | -3.88223 | -54.21549 | 2024-11-24 05:16:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| bcf42e13-f9d4-386f-9f68-0b5cc49d2840 | -4.40844 | -49.65054 | 2024-11-24 05:16:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| bcdf2aca-3efc-3f1d-80e6-3c5664eb5f2a | -3.50406 | -53.81562 | 2024-11-24 05:16:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 13.5 |
| 6fb1d266-cb16-3432-b968-d0aa1e093cd7 | -3.24946 | -54.21895 | 2024-11-24 05:16:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 176d1ee8-4091-34b3-a59e-4d07457b660d | -3.61886 | -54.79165 | 2024-11-24 05:16:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 08058b2e-6f40-3210-b5e6-5b2af0479227 | -3.84937 | -52.19288 | 2024-11-24 05:16:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| e4b7d927-9ccd-319d-ac75-840da5d739ba | -3.51533 | -54.68887 | 2024-11-24 05:16:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 284a5c1a-9560-38e7-9f76-716efc8f13ab | -3.15265 | -54.95988 | 2024-11-24 05:16:00 | NPP-375D | BELTERRA | PARÁ | Brasil | 1501451 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 41c9ef69-8342-3be6-9816-14eea250426c | -4.16229 | -54.57446 | 2024-11-24 05:16:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| b2e2e242-3d9a-3eaf-b6ad-6cec7089fa90 | -3.6669 | -51.73277 | 2024-11-24 05:16:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| f0d4a134-f684-33f4-bfbf-dade3efa17f6 | -3.2556 | -54.2292 | 2024-11-24 05:16:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 60c740ea-5b0c-3a64-a764-65870bc07d01 | -3.51794 | -54.7631 | 2024-11-24 05:16:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 4d852779-78a1-37bd-8f67-04b17dd327b8 | -3.57192 | -53.31809 | 2024-11-24 05:16:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| a7c9216e-bb4c-35c0-8605-f7a9507b83ba | -3.96247 | -50.20077 | 2024-11-24 05:16:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 397c973f-a26b-3f64-81cc-236789ff394d | -3.77858 | -52.09905 | 2024-11-24 05:16:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| beaff5fe-be4f-3e27-9151-93f829d1719e | -3.67906 | -54.58531 | 2024-11-24 05:16:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 700a4644-330e-3213-9228-72162a70a9b2 | -3.98199 | -49.93182 | 2024-11-24 05:16:00 | NPP-375D | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 681d8fef-c8ab-3c67-b294-93ce95ba57f1 | -3.24663 | -54.23717 | 2024-11-24 05:16:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 39ec03d7-2c01-33cf-90b3-b5281498fd0c | -4.34736 | -55.7765 | 2024-11-24 05:16:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| b6daa956-d24f-38b4-9cfa-3e8a7bc0b343 | -15.41755 | -60.28006 | 2024-11-24 05:18:00 | NPP-375D | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 5b52938c-18c3-3dd5-ad13-9a46ff4644ab | -15.67722 | -59.15258 | 2024-11-24 05:18:00 | NPP-375D | PORTO ESPERIDIÃO | MATO GROSSO | Brasil | 5106828 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 53e6d53a-95aa-374a-9baf-4466b18ceb02 | -15.21936 | -60.37709 | 2024-11-24 05:18:00 | NPP-375D | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 94fbc169-a5dd-3617-a7e0-c198e28234c1 | -15.5829 | -59.29263 | 2024-11-24 05:18:00 | NPP-375D | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 5a9b222f-d9d8-3ce1-8991-62cb1d7463b2 | -16.0856 | -60.08952 | 2024-11-24 05:18:00 | NPP-375D | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| bd8747db-dafb-376c-9128-e7f5f39bd2d3 | -15.58631 | -59.29319 | 2024-11-24 05:18:00 | NPP-375D | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 0.4 |
| b7a6b90b-f6d4-3545-b139-a2d49e28cdf1 | -3.5159 | -53.8132 | 2024-11-24 05:20:00 | GOES-16 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 77.6 |
| 22b86726-9af8-389e-88e3-7135649cd57e | -20.72025 | -53.54634 | 2024-11-24 05:20:00 | NPP-375D | RIBAS DO RIO PARDO | MATO GROSSO DO SUL | Brasil | 5007109 | 50 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 253d119a-316f-3de3-a992-9eaf7bfd8b7b | -21.12193 | -50.58871 | 2024-11-24 05:20:00 | NPP-375D | ARAÇATUBA | SÃO PAULO | Brasil | 3502804 | 35 | 33 | nan | nan | nan | Mata Atlântica | 5.0 |
| a63bd730-641d-3226-b984-2e9233e0b44e | -23.07263 | -49.80144 | 2024-11-24 05:20:00 | NPP-375D | CHAVANTES | SÃO PAULO | Brasil | 3557204 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.9 |
| 7ed1ab32-9d7b-3fda-bfac-8f63133c5594 | -17.75737 | -52.4353 | 2024-11-24 05:20:00 | NPP-375D | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| e8b5b0cb-a742-3dbb-8453-4a8bcc51cbea | -22.17216 | -55.72768 | 2024-11-24 05:20:00 | NPP-375D | ANTÔNIO JOÃO | MATO GROSSO DO SUL | Brasil | 5000906 | 50 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 6d28d48c-e45f-3c0d-925b-fe0d8ba633c9 | -21.31891 | -55.94921 | 2024-11-24 05:20:00 | NPP-375D | NIOAQUE | MATO GROSSO DO SUL | Brasil | 5005806 | 50 | 33 | nan | nan | nan | Cerrado | 1.2 |
| cd143c21-48a4-3c38-a527-07377839475a | -21.12157 | -50.58741 | 2024-11-24 05:20:00 | NPP-375D | ARAÇATUBA | SÃO PAULO | Brasil | 3502804 | 35 | 33 | nan | nan | nan | Mata Atlântica | 6.2 |
| 6ba7e6a7-d7ac-347a-9370-626231584224 | -20.72373 | -53.54817 | 2024-11-24 05:20:00 | NPP-375D | RIBAS DO RIO PARDO | MATO GROSSO DO SUL | Brasil | 5007109 | 50 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 47267eec-a5f8-39dd-bd0e-1ef029b1ea4e | -23.0722 | -49.80683 | 2024-11-24 05:20:00 | NPP-375D | CHAVANTES | SÃO PAULO | Brasil | 3557204 | 35 | 33 | nan | nan | nan | Mata Atlântica | 3.2 |
| 1bc3b7dc-e6ed-3b7e-8dcf-013c5b6040c9 | -23.07196 | -49.80688 | 2024-11-24 05:20:00 | NPP-375D | CHAVANTES | SÃO PAULO | Brasil | 3557204 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.8 |
| 32a94dab-68bb-3a7f-b994-62e19b0d26bb | -21.12235 | -50.58388 | 2024-11-24 05:20:00 | NPP-375D | ARAÇATUBA | SÃO PAULO | Brasil | 3502804 | 35 | 33 | nan | nan | nan | Mata Atlântica | 3.7 |
| b22d6094-475f-3fe5-be48-156e622c3e7e | -23.07236 | -49.80148 | 2024-11-24 05:20:00 | NPP-375D | CHAVANTES | SÃO PAULO | Brasil | 3557204 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.8 |
| 1bb95977-43b1-319c-8bd1-3b26b1f3fc36 | -17.75789 | -52.4354 | 2024-11-24 05:20:00 | NPP-375D | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 713ce6ef-b1ec-3203-9a3a-2975cbd9b7f1 | -21.31839 | -55.95359 | 2024-11-24 05:20:00 | NPP-375D | NIOAQUE | MATO GROSSO DO SUL | Brasil | 5005806 | 50 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 7f12bac3-278d-39d7-bd90-563fa633853a | -22.16985 | -55.72972 | 2024-11-24 05:20:00 | NPP-375D | ANTÔNIO JOÃO | MATO GROSSO DO SUL | Brasil | 5000906 | 50 | 33 | nan | nan | nan | Cerrado | 0.9 |
| faf3c789-060e-3c5b-99da-838e64c39bc6 | -17.757 | -52.43853 | 2024-11-24 05:20:00 | NPP-375D | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 40af8796-78af-3644-a750-407331356434 | -17.75266 | -52.43494 | 2024-11-24 05:20:00 | NPP-375D | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 0.3 |
| e0e6a6ee-e7c4-3e40-973c-3228aeb919f2 | -17.75754 | -52.43865 | 2024-11-24 05:20:00 | NPP-375D | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 2cefd508-5ba0-3788-ba36-05d0862ee159 | -3.5159 | -53.8132 | 2024-11-24 05:30:00 | GOES-16 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 85.1 |
| ecb6571a-a9ce-33ce-9879-95420206c51d | -2.16781 | -53.77944 | 2024-11-24 05:37:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 8836c618-5f71-3a1c-9ff3-6a5708d85423 | -2.16843 | -53.77527 | 2024-11-24 05:37:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 92bdf5aa-506e-3d0f-80cd-d5441cb4b685 | -3.11276 | -54.00835 | 2024-11-24 05:37:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| e7d48d49-06e0-3d0e-b74d-ec32eb9906b4 | 0.40811 | -50.86318 | 2024-11-24 05:37:00 | NOAA-20 | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 9dc5cb18-6240-391e-a7dc-945134df8268 | -3.11936 | -53.10926 | 2024-11-24 05:37:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 23ca466f-5e13-3016-8874-dcf11cc221e5 | 0.42268 | -50.85255 | 2024-11-24 05:37:00 | NOAA-20 | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 0.9 |
| cea380db-94e4-303c-84e1-27ee5ee2bd79 | -1.51702 | -54.1872 | 2024-11-24 05:37:00 | NOAA-20 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| a6c79658-cbc1-3843-80f1-2e2ed759a30d | -1.40981 | -54.47695 | 2024-11-24 05:37:00 | NOAA-20 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 923dff39-d31d-35e9-82b8-42901f0b762d | -1.51902 | -51.62268 | 2024-11-24 05:37:00 | NOAA-20 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 856c3821-be19-3e37-807b-c94d11e53e63 | -3.10754 | -54.00321 | 2024-11-24 05:37:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 9e466d0e-f719-33e7-9d9f-35748d3f44f9 | -1.41007 | -54.47654 | 2024-11-24 05:37:00 | NOAA-20 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| e4d53d4b-d9d0-35b8-976b-4aa6599ee5ef | -2.94186 | -54.08185 | 2024-11-24 05:37:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 25b5c62b-4b96-3211-84cb-5d74cf6db73e | 0.01128 | -51.19213 | 2024-11-24 05:37:00 | NOAA-20 | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 4.3 |
| b7d0c665-76bc-3f4c-94aa-5e31d9d5511c | -1.04322 | -51.7466 | 2024-11-24 05:37:00 | NOAA-20 | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | 2.5 |
| f0c20cb0-6b68-3db0-9775-1bc94b7b3b2b | -3.2459 | -53.27219 | 2024-11-24 05:37:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 6e473b81-231a-3d46-bf3f-f58bd9f1344e | -1.59948 | -52.58898 | 2024-11-24 05:37:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 12.8 |
| e4e409d6-c2e0-3a3c-a2b9-e9c45f77f746 | -2.17805 | -53.6417 | 2024-11-24 05:37:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 23f6f0af-0420-3ae9-a70c-65682c110b04 | -1.40537 | -54.47051 | 2024-11-24 05:37:00 | NOAA-20 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 6286eba1-8e68-34b8-a50b-8359cf3a1804 | -3.56967 | -51.11505 | 2024-11-24 05:37:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 4a2fee60-2dff-3f65-9e38-eb555515cb4a | -1.11685 | -53.58358 | 2024-11-24 05:37:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 1c9bf422-d907-38fd-b68a-94f7d4d7e0de | -1.11744 | -53.57967 | 2024-11-24 05:37:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 2f702cee-c835-388f-81a9-642a54f63d72 | -2.17827 | -53.78957 | 2024-11-24 05:37:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| afd5d9a8-c493-3dd0-9c44-4128d4f500ed | -1.7245 | -53.25624 | 2024-11-24 05:37:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| b293466b-93d8-38c0-b615-a2cb63410055 | -1.45186 | -53.4058 | 2024-11-24 05:37:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 5.7 |
| 9b4ddb60-06e8-3cc8-8afd-3e28357fc14b | -2.58085 | -54.23062 | 2024-11-24 05:37:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| b4fc0782-234b-38dd-aa12-c96115909807 | -2.3213 | -53.86567 | 2024-11-24 05:37:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 7.5 |
| 59b955a1-1e7c-31c3-b612-f258f6e699b6 | -2.84771 | -53.99822 | 2024-11-24 05:37:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| a0071437-7b41-35ac-9895-2c410645fd91 | -0.81563 | -52.83307 | 2024-11-24 05:37:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| fc9a7f6b-1f7f-3663-a8f4-c517913b017b | -2.9985 | -52.51283 | 2024-11-24 05:37:00 | NOAA-20 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 82251dda-0722-3e0e-87f5-74a8b1e97cbf | -1.42698 | -53.3878 | 2024-11-24 05:37:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 994ef1b2-ebd9-36fa-bd6a-c130b9bb991e | -2.9996 | -52.51558 | 2024-11-24 05:37:00 | NOAA-20 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |


[Clique aqui para ver as próximas entradas](README82.md)
