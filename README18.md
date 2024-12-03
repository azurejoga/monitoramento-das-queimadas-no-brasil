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
| ef3fe427-a5ee-35fd-a1b2-9fd011177459 | -3.0944 | -53.3804 | 2024-12-03 02:30:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 128.8 |
| ae308626-10e6-3559-ac9c-20744c9e3e6d | -3.2775 | -53.6181 | 2024-12-03 02:30:00 | GOES-16 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 60.5 |
| 27fe2ad4-be3d-3e56-a77a-5d40c6464892 | -3.0761 | -53.3606 | 2024-12-03 02:30:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 62.2 |
| df15e701-fcbe-395a-b2ff-cb9b8087b3bd | -2.7378 | -45.1976 | 2024-12-03 02:30:00 | GOES-16 | PINHEIRO | MARANHÃO | Brasil | 2108603 | 21 | 33 | nan | nan | nan | Amazônia | 292.4 |
| c35bcde7-b702-332e-85f9-e382a04ab31a | -3.259 | -53.6388 | 2024-12-03 02:30:00 | GOES-16 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 82.2 |
| a60a9097-42b3-3890-b6b3-b12323e32501 | -3.259 | -53.659 | 2024-12-03 02:30:00 | GOES-16 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 111.4 |
| 7ff66f71-e925-3222-9b99-b28b96778ff4 | -2.8854 | -45.44 | 2024-12-03 02:30:00 | GOES-16 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 69.3 |
| 365f41c1-b711-3cb7-a687-ba6b9cfb80f6 | -2.7192 | -45.1982 | 2024-12-03 02:30:00 | GOES-16 | PINHEIRO | MARANHÃO | Brasil | 2108603 | 21 | 33 | nan | nan | nan | Amazônia | 381.4 |
| d01c3b91-a169-3038-879f-cb50c921f6b9 | -6.1229 | -43.9578 | 2024-12-03 02:30:00 | GOES-16 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 70.5 |
| f47439f7-5f85-3099-82cb-60e491cd9588 | -1.7867 | -46.6714 | 2024-12-03 02:30:00 | GOES-16 | VISEU | PARÁ | Brasil | 1508308 | 15 | 33 | nan | nan | nan | Amazônia | 68.5 |
| f8df1b7d-9d15-3d19-bf93-be5aa834d97d | -3.0945 | -53.3601 | 2024-12-03 02:30:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 67.3 |
| 366d3f7e-f290-3645-ba82-0accb96d26e5 | -3.2774 | -53.6383 | 2024-12-03 02:30:00 | GOES-16 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 57.6 |
| cdf19756-2f6f-3348-9614-e3d08c9c303c | -5.8195 | -46.4929 | 2024-12-03 02:30:00 | GOES-16 | SÍTIO NOVO | MARANHÃO | Brasil | 2111805 | 21 | 33 | nan | nan | nan | Cerrado | 61.5 |
| ae28601b-d4f1-3742-9594-94d87ba6d518 | -2.8485 | -45.3963 | 2024-12-03 02:30:00 | GOES-16 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 100.8 |
| 8956178f-4041-39a4-9b7c-af39b6507c57 | -5.8197 | -46.4706 | 2024-12-03 02:30:00 | GOES-16 | SÍTIO NOVO | MARANHÃO | Brasil | 2111805 | 21 | 33 | nan | nan | nan | Cerrado | 103.9 |
| 3a4b3d1c-f1d6-3b31-8872-2722a4b9e27a | -2.8196 | -53.0629 | 2024-12-03 02:30:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 75.1 |
| 101c421b-e2ed-31a7-ac8c-bddcc909d904 | -2.8013 | -53.043 | 2024-12-03 02:30:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 63.3 |
| 53e0b9a4-6197-3b3c-a944-e3ad9fd34e7d | -2.8012 | -53.0633 | 2024-12-03 02:30:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 59.3 |
| cb6b8703-373c-3ef0-b3e6-b265214e325d | -5.801 | -46.4719 | 2024-12-03 02:30:00 | GOES-16 | SÍTIO NOVO | MARANHÃO | Brasil | 2111805 | 21 | 33 | nan | nan | nan | Cerrado | 184.9 |
| 74edaca6-d51e-3586-9345-1e42899ba60a | -1.7868 | -46.6494 | 2024-12-03 02:30:00 | GOES-16 | VISEU | PARÁ | Brasil | 1508308 | 15 | 33 | nan | nan | nan | Amazônia | 131.0 |
| df51b556-ca7c-37c6-aa89-bb9a470ebb34 | -5.8009 | -46.4941 | 2024-12-03 02:30:00 | GOES-16 | SÍTIO NOVO | MARANHÃO | Brasil | 2111805 | 21 | 33 | nan | nan | nan | Cerrado | 99.0 |
| 93dd0a0d-5efe-3c56-8557-43c18c688b79 | -1.7541 | -52.7993 | 2024-12-03 02:30:00 | GOES-16 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 56.6 |
| 66b6ea48-3a4b-37f5-8ce5-a8620f8b1142 | -3.347 | -46.0486 | 2024-12-03 02:30:00 | GOES-16 | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 88.7 |
| 20585055-21a1-3a6e-b30e-4979d0692307 | -2.7191 | -45.2208 | 2024-12-03 02:30:00 | GOES-16 | PINHEIRO | MARANHÃO | Brasil | 2108603 | 21 | 33 | nan | nan | nan | Amazônia | 324.6 |
| 9e3da7d8-9afc-3e7e-a7b6-4482b5c44e87 | -3.2591 | -53.6186 | 2024-12-03 02:30:00 | GOES-16 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 69.6 |
| 5f42d151-2a4d-33be-a3e8-cff434ba675c | -3.076 | -53.3808 | 2024-12-03 02:30:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 119.3 |
| 70c530b5-dd73-36aa-aa51-3300677cd37d | -2.8486 | -45.3739 | 2024-12-03 02:30:00 | GOES-16 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 62.1 |
| 0ec7f48e-c871-3d7f-b6ab-cc71cc4e3f79 | -1.8052 | -46.671 | 2024-12-03 02:30:00 | GOES-16 | VISEU | PARÁ | Brasil | 1508308 | 15 | 33 | nan | nan | nan | Amazônia | 120.8 |
| a4690ffc-8609-3487-8a2f-0aa0457837b9 | -1.8053 | -46.649 | 2024-12-03 02:30:00 | GOES-16 | VISEU | PARÁ | Brasil | 1508308 | 15 | 33 | nan | nan | nan | Amazônia | 252.2 |
| e45b643e-27c9-3a40-b3b4-beeebdac1731 | -2.8197 | -53.0425 | 2024-12-03 02:30:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 69.7 |
| c52d2fb5-7fa5-399f-bbc8-b4d44258b79a | -11.4355 | -55.9098 | 2024-12-03 02:30:00 | GOES-16 | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 64.8 |
| 26ef8171-8045-3f9a-8675-0e48a8f0549c | -2.7192 | -45.1982 | 2024-12-03 02:40:00 | GOES-16 | PINHEIRO | MARANHÃO | Brasil | 2108603 | 21 | 33 | nan | nan | nan | Amazônia | 133.1 |
| 5087f669-6b9d-3430-a143-15a99c1244be | -2.8013 | -53.043 | 2024-12-03 02:40:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 60.7 |
| 866873f4-c7bc-37c7-8b15-558ba1c20c59 | -2.2111 | -53.7835 | 2024-12-03 02:40:00 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 84.9 |
| 21d5fdb9-5032-3880-a2ee-71901f857ad2 | -3.2591 | -53.6186 | 2024-12-03 02:40:00 | GOES-16 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 62.7 |
| 5e864b23-1e6d-3f86-ac62-0cde5b45b3f2 | -2.7377 | -45.2201 | 2024-12-03 02:40:00 | GOES-16 | PINHEIRO | MARANHÃO | Brasil | 2108603 | 21 | 33 | nan | nan | nan | Amazônia | 264.8 |
| 8a8b4c52-dc22-3743-97a0-1c56203fbc29 | -3.076 | -53.3808 | 2024-12-03 02:40:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 161.0 |
| dd22b143-c1a1-3b8e-92d0-ed8b52b1ef8d | -5.8009 | -46.4941 | 2024-12-03 02:40:00 | GOES-16 | SÍTIO NOVO | MARANHÃO | Brasil | 2111805 | 21 | 33 | nan | nan | nan | Cerrado | 136.5 |
| 42d71c94-b0b6-30b3-8531-81944511b9f0 | -11.4355 | -55.9098 | 2024-12-03 02:40:00 | GOES-16 | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 51.7 |
| 9bfd6938-430a-370d-952d-0f07168c6ac8 | -5.7824 | -46.4732 | 2024-12-03 02:40:00 | GOES-16 | SÍTIO NOVO | MARANHÃO | Brasil | 2111805 | 21 | 33 | nan | nan | nan | Cerrado | 58.9 |
| 6758ade7-6736-33d0-9a88-5f5aa658d385 | -3.0944 | -53.3804 | 2024-12-03 02:40:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 98.4 |
| b67fe91a-f6fc-31fd-9eb5-75068ef33d75 | -3.2406 | -53.6595 | 2024-12-03 02:40:00 | GOES-16 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 55.9 |
| a0a22647-e1cd-3b5d-b4e5-7ac609d164b1 | -3.259 | -53.659 | 2024-12-03 02:40:00 | GOES-16 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 99.1 |
| 36be77b7-c1e9-3b54-95cd-4404380a1d19 | -3.347 | -46.0486 | 2024-12-03 02:40:00 | GOES-16 | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 83.8 |
| 27915b56-2fce-34eb-9b0d-da107e674c3f | -5.8197 | -46.4706 | 2024-12-03 02:40:00 | GOES-16 | SÍTIO NOVO | MARANHÃO | Brasil | 2111805 | 21 | 33 | nan | nan | nan | Cerrado | 114.1 |
| 505de751-c1c5-32b7-9cec-129368a031a8 | -2.8196 | -53.0629 | 2024-12-03 02:40:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 66.9 |
| d9726889-f5d5-353f-b6f9-6fb3843fdb90 | -6.1229 | -43.9578 | 2024-12-03 02:40:00 | GOES-16 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 68.9 |
| 8c93081b-4801-3021-a432-6d9261369da5 | -2.8485 | -45.3963 | 2024-12-03 02:40:00 | GOES-16 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 96.0 |
| ea8de425-48ec-3e58-a89a-efefcc11268a | -2.7378 | -45.1976 | 2024-12-03 02:40:00 | GOES-16 | PINHEIRO | MARANHÃO | Brasil | 2108603 | 21 | 33 | nan | nan | nan | Amazônia | 292.6 |
| 27393194-59d4-3f74-aadc-0ab2c6f76e9d | -3.259 | -53.6388 | 2024-12-03 02:40:00 | GOES-16 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 70.4 |
| 03581a29-42a4-38f2-b77a-ca9450283c0c | -2.2112 | -53.7634 | 2024-12-03 02:40:00 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 56.5 |
| 1bdc2dd8-4bdb-3452-b8da-685be1dfb743 | -1.7867 | -46.6714 | 2024-12-03 02:40:00 | GOES-16 | VISEU | PARÁ | Brasil | 1508308 | 15 | 33 | nan | nan | nan | Amazônia | 59.6 |
| 74cf95cc-c79b-3283-b975-e690096d5fd1 | -1.8052 | -46.671 | 2024-12-03 02:40:00 | GOES-16 | VISEU | PARÁ | Brasil | 1508308 | 15 | 33 | nan | nan | nan | Amazônia | 102.5 |
| c308bf45-5113-3182-a6e2-f644e0a8ebe2 | -1.8053 | -46.649 | 2024-12-03 02:40:00 | GOES-16 | VISEU | PARÁ | Brasil | 1508308 | 15 | 33 | nan | nan | nan | Amazônia | 185.6 |
| 439e54df-95b2-38f7-ad34-80205f6b1684 | -3.0376 | -53.8664 | 2024-12-03 02:40:00 | GOES-16 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 63.4 |
| 5d357535-ba93-3a08-9755-62acf077d87f | -2.8012 | -53.0633 | 2024-12-03 02:40:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 56.6 |
| 00367736-5733-3cda-9a4e-4d0ca74fa7c9 | -3.0761 | -53.3606 | 2024-12-03 02:40:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 61.5 |
| cfe8fbd4-d31a-3cd9-b4b8-2b489bbc525c | -2.7191 | -45.2208 | 2024-12-03 02:40:00 | GOES-16 | PINHEIRO | MARANHÃO | Brasil | 2108603 | 21 | 33 | nan | nan | nan | Amazônia | 141.5 |
| f453f952-9e7e-3421-9d8c-11aa75ee77d0 | -5.8195 | -46.4929 | 2024-12-03 02:40:00 | GOES-16 | SÍTIO NOVO | MARANHÃO | Brasil | 2111805 | 21 | 33 | nan | nan | nan | Cerrado | 81.5 |
| c4dc090d-08e4-338c-878c-5cb08b842460 | 1.1072 | -55.9874 | 2024-12-03 02:40:00 | GOES-16 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 53.9 |
| ed860787-5488-3c2c-be5b-f419a701e2bb | -3.076 | -53.4011 | 2024-12-03 02:40:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 58.2 |
| ae9d5593-432a-393f-be5e-8554de3844e3 | -1.7868 | -46.6494 | 2024-12-03 02:40:00 | GOES-16 | VISEU | PARÁ | Brasil | 1508308 | 15 | 33 | nan | nan | nan | Amazônia | 78.2 |
| 458ddd7f-4db5-35bc-92fa-f1a639bb38aa | -1.8238 | -46.6486 | 2024-12-03 02:40:00 | GOES-16 | VISEU | PARÁ | Brasil | 1508308 | 15 | 33 | nan | nan | nan | Amazônia | 46.5 |
| ddc8df3d-70cf-3953-89dd-d6bfaecf9972 | -5.801 | -46.4719 | 2024-12-03 02:40:00 | GOES-16 | SÍTIO NOVO | MARANHÃO | Brasil | 2111805 | 21 | 33 | nan | nan | nan | Cerrado | 190.5 |
| fde4f436-dc4a-306b-8bf4-6a07bb0cea0a | -2.8197 | -53.0425 | 2024-12-03 02:40:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 69.3 |
| 39c9b5bf-552e-33dc-9758-d3b1592187e7 | -6.83091 | -35.32941 | 2024-12-03 02:49:00 | NOAA-20 | ARAÇAGI | PARAÍBA | Brasil | 2500809 | 25 | 33 | nan | nan | nan | Caatinga | 3.8 |
| d86ad6ac-ce16-3d5d-9c50-7ee00c680793 | -6.832 | -35.32354 | 2024-12-03 02:49:00 | NOAA-20 | ARAÇAGI | PARAÍBA | Brasil | 2500809 | 25 | 33 | nan | nan | nan | Caatinga | 3.8 |
| 72df12ed-75a3-3535-b6fd-8903af715fc2 | -1.8052 | -46.671 | 2024-12-03 02:50:00 | GOES-16 | VISEU | PARÁ | Brasil | 1508308 | 15 | 33 | nan | nan | nan | Amazônia | 54.1 |
| e0f4c22c-57da-3b2a-aec2-244fda3a5053 | -11.4355 | -55.9098 | 2024-12-03 02:50:00 | GOES-16 | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 54.9 |
| 1079cfec-a194-3a34-9f7a-3313d63266f9 | -2.7192 | -45.1982 | 2024-12-03 02:50:00 | GOES-16 | PINHEIRO | MARANHÃO | Brasil | 2108603 | 21 | 33 | nan | nan | nan | Amazônia | 93.2 |
| 63c302fd-e0e3-3a57-8caa-aa69feccc826 | -2.8013 | -53.043 | 2024-12-03 02:50:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 60.2 |
| 5deb6578-fde5-3694-a0f1-bd990645e438 | -3.0944 | -53.3804 | 2024-12-03 02:50:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 114.6 |
| edf9462a-a313-3cb8-84cd-683a2ea30554 | -5.8009 | -46.4941 | 2024-12-03 02:50:00 | GOES-16 | SÍTIO NOVO | MARANHÃO | Brasil | 2111805 | 21 | 33 | nan | nan | nan | Cerrado | 137.6 |
| 1461a59c-7a74-3c01-87c6-07b807d563b9 | -2.8197 | -53.0425 | 2024-12-03 02:50:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 71.4 |
| 85c9716a-00f4-33ff-bf25-3227d490d2f1 | -3.259 | -53.6388 | 2024-12-03 02:50:00 | GOES-16 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 83.8 |
| 6b79a741-ce15-395e-b37c-300fbc780bcc | -3.0761 | -53.3606 | 2024-12-03 02:50:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 68.0 |
| 263693d5-a294-36a1-957b-01aa10f5d73c | -1.0735 | -53.4562 | 2024-12-03 02:50:00 | GOES-16 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 46.2 |
| 7ba9fe08-2a9a-3b11-99a9-345c2990065d | -2.1928 | -53.7839 | 2024-12-03 02:50:00 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 55.2 |
| a8ec404c-cf2d-34f2-b3b4-23ce1f27f073 | -3.076 | -53.3808 | 2024-12-03 02:50:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 149.4 |
| d640a8ce-dcce-3828-94c3-bbfc9f8f8764 | -3.076 | -53.4011 | 2024-12-03 02:50:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 58.3 |
| 94478767-25bc-3300-ac14-6d14493d94dd | -3.347 | -46.0486 | 2024-12-03 02:50:00 | GOES-16 | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 79.2 |
| 0c0f8794-394d-3ee0-a003-a72031045e3b | -2.7378 | -45.1976 | 2024-12-03 02:50:00 | GOES-16 | PINHEIRO | MARANHÃO | Brasil | 2108603 | 21 | 33 | nan | nan | nan | Amazônia | 118.4 |
| 292859e6-0b71-3236-8f12-cccd571c300c | -1.7868 | -46.6494 | 2024-12-03 02:50:00 | GOES-16 | VISEU | PARÁ | Brasil | 1508308 | 15 | 33 | nan | nan | nan | Amazônia | 57.0 |
| 1ea9ed36-52cb-36ff-b08d-f081fd6c753a | -2.8012 | -53.0633 | 2024-12-03 02:50:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 58.4 |
| 59b6f688-8664-33ef-9bfb-5cb06a5fe9d1 | -2.2112 | -53.7634 | 2024-12-03 02:50:00 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 58.7 |
| 8ccd0e30-e29a-3986-9fce-3bac73fc4e01 | -6.1229 | -43.9578 | 2024-12-03 02:50:00 | GOES-16 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 68.5 |
| c8c06511-99b4-357b-ac89-986e465fea02 | -3.0945 | -53.3601 | 2024-12-03 02:50:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 56.6 |
| 7d417731-ade6-3a72-b334-d6328cdfc838 | -5.8197 | -46.4706 | 2024-12-03 02:50:00 | GOES-16 | SÍTIO NOVO | MARANHÃO | Brasil | 2111805 | 21 | 33 | nan | nan | nan | Cerrado | 127.3 |
| 3fbf989d-3274-3bc3-bc1d-f13c5936857d | -3.2775 | -53.6181 | 2024-12-03 02:50:00 | GOES-16 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 70.0 |
| 4b59c21c-81cf-355a-81b6-e33834635eec | -1.0919 | -53.4561 | 2024-12-03 02:50:00 | GOES-16 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 59.2 |
| 41d531b8-7c3c-3df3-aa2e-8a2dea456156 | -3.259 | -53.659 | 2024-12-03 02:50:00 | GOES-16 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 113.7 |
| ead01a50-ad73-3462-8c6c-074becb448a5 | -2.8485 | -45.3963 | 2024-12-03 02:50:00 | GOES-16 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 74.5 |
| f063ccfd-40ee-34e9-ad84-a7b6967f23cc | -2.8196 | -53.0629 | 2024-12-03 02:50:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 70.7 |
| d617ec6f-3722-30fe-a002-15d3d10cd5d7 | -2.7377 | -45.2201 | 2024-12-03 02:50:00 | GOES-16 | PINHEIRO | MARANHÃO | Brasil | 2108603 | 21 | 33 | nan | nan | nan | Amazônia | 121.4 |
| 10fee2ce-664b-3aa8-be74-e5b022c5d9a3 | -5.801 | -46.4719 | 2024-12-03 02:50:00 | GOES-16 | SÍTIO NOVO | MARANHÃO | Brasil | 2111805 | 21 | 33 | nan | nan | nan | Cerrado | 208.6 |
| 73779c3b-0213-3417-9fa7-b6e663aee714 | -3.2591 | -53.6186 | 2024-12-03 02:50:00 | GOES-16 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 74.3 |
| 2658114e-0372-3d82-9e20-abbc258e815c | -3.0376 | -53.8664 | 2024-12-03 02:50:00 | GOES-16 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 59.4 |
| 523fd86b-cd38-3487-8e64-11e71d92c734 | -3.2774 | -53.6383 | 2024-12-03 02:50:00 | GOES-16 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 61.5 |
| 692244f1-d29c-34b2-a909-43215c4f71f7 | -5.8195 | -46.4929 | 2024-12-03 02:50:00 | GOES-16 | SÍTIO NOVO | MARANHÃO | Brasil | 2111805 | 21 | 33 | nan | nan | nan | Cerrado | 81.0 |
| cd9457f3-59fa-3fcd-9a89-031975b3c94c | -1.8053 | -46.649 | 2024-12-03 02:50:00 | GOES-16 | VISEU | PARÁ | Brasil | 1508308 | 15 | 33 | nan | nan | nan | Amazônia | 95.6 |


[Clique aqui para ver as próximas entradas](README19.md)
