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

## Dados Diários - Página 20

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 8ad0da12-99ce-3959-b38c-61d9a7682926 | -10.735 | -50.063 | 2026-06-25 14:50:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 64.6 |
| 4406f762-ead6-3056-ad28-27f23ef861e5 | -6.3036 | -44.6557 | 2026-06-25 15:00:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 83.4 |
| e3fad85d-9d1f-3483-88c7-078f6a34078a | -6.9979 | -42.9016 | 2026-06-25 15:00:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 100.4 |
| d01c543e-5c37-3286-ae01-88c37e7f0a00 | -7.7498 | -44.6184 | 2026-06-25 15:00:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 99.8 |
| 44575d6e-e59d-38fb-8b11-7d5642ee0f74 | -6.1431 | -45.8003 | 2026-06-25 15:00:00 | GOES-19 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 98.9 |
| 440c8507-2d2f-3e7a-b7ba-ca5391f681c3 | -6.9793 | -42.8798 | 2026-06-25 15:00:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 98.5 |
| a50a31b6-313d-366f-ad6b-4d7c2b93ac8c | -11.8868 | -51.7452 | 2026-06-25 15:00:00 | GOES-19 | ALTO BOA VISTA | MATO GROSSO | Brasil | 5100359 | 51 | 33 | nan | nan | nan | Amazônia | 95.8 |
| ae8d81be-b59d-3c02-9b0a-af9ce115af0e | -6.1433 | -45.7778 | 2026-06-25 15:00:00 | GOES-19 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 72.7 |
| e8946fa7-9dbe-3500-a9f3-f91090e97077 | -9.9917 | -47.7316 | 2026-06-25 15:10:00 | GOES-19 | NOVO ACORDO | TOCANTINS | Brasil | 1715101 | 17 | 33 | nan | nan | nan | Cerrado | 136.8 |
| c748ce56-39b8-30ed-bfa7-8f66bfd043ea | -6.3036 | -44.6557 | 2026-06-25 15:10:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 65.1 |
| 94cad8cd-50a9-39cc-a176-d391607e6ee1 | -6.1431 | -45.8003 | 2026-06-25 15:10:00 | GOES-19 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 80.7 |
| 5b02b350-d581-3ed3-9864-0d85605d6ebc | -7.7498 | -44.6184 | 2026-06-25 15:10:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 95.8 |
| 81274e04-e76b-3c01-bdc5-a2c61c038ae9 | -6.1433 | -45.7778 | 2026-06-25 15:20:00 | GOES-19 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 68.5 |
| 3a01d727-07c7-3ab7-bade-f930606ed6f6 | -7.7498 | -44.6184 | 2026-06-25 15:20:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 92.4 |
| 8ad1d3f2-7e9d-334a-8ee9-e60bc9c7e4f9 | -10.6061 | -47.1727 | 2026-06-25 15:20:00 | GOES-19 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 150.6 |
| 1e2368b3-5acf-3529-b546-16fbc6263bbb | -6.1246 | -45.7792 | 2026-06-25 15:20:00 | GOES-19 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 61.3 |
| 8fd4b08b-117f-3421-a1cf-ff1b2d605da3 | -6.9275 | -47.8432 | 2026-06-25 15:20:00 | GOES-19 | WANDERLÂNDIA | TOCANTINS | Brasil | 1722081 | 17 | 33 | nan | nan | nan | Cerrado | 96.9 |
| 1b8d99ee-5f4c-3a56-9f8a-eeda003e9ea9 | -6.3036 | -44.6557 | 2026-06-25 15:20:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 72.3 |
| e267cf4a-f6f6-30ad-9a0a-8c1e2b3e65d6 | -6.9979 | -42.9016 | 2026-06-25 15:20:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 102.1 |
| 60d3e4b9-470c-3fa0-82a7-cd8583f46942 | -6.1431 | -45.8003 | 2026-06-25 15:20:00 | GOES-19 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 131.6 |
| 0c673f1f-c1b4-316d-8949-42d5875b5e4d | -6.9793 | -42.8798 | 2026-06-25 15:20:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 90.0 |
| 27a3869a-17f5-311a-832e-78fcd8004c9f | -6.1093 | -47.509 | 2026-06-25 15:30:00 | GOES-19 | TOCANTINÓPOLIS | TOCANTINS | Brasil | 1721208 | 17 | 33 | nan | nan | nan | Cerrado | 73.7 |
| 662effd7-5f1b-33a5-9a1a-ea8028c2de56 | -6.1431 | -45.8003 | 2026-06-25 15:30:00 | GOES-19 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 85.1 |
| d2187e6f-a115-3acd-b210-5eaea60d5f79 | -10.6061 | -47.1727 | 2026-06-25 15:30:00 | GOES-19 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 142.1 |
| 99eda5f3-9896-3be1-9e75-0ea452cf0df4 | -6.9275 | -47.8432 | 2026-06-25 15:30:00 | GOES-19 | WANDERLÂNDIA | TOCANTINS | Brasil | 1722081 | 17 | 33 | nan | nan | nan | Cerrado | 96.3 |
| 2c499e68-f9f1-39e6-8629-835317642c9b | -7.7498 | -44.6184 | 2026-06-25 15:30:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 89.8 |
| a79d64b0-aa1a-3325-93a3-754519d0e9d6 | -6.3036 | -44.6557 | 2026-06-25 15:30:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 68.0 |
| 52922bb7-7aa3-332d-83a0-ad754e2f043b | -6.1431 | -45.8003 | 2026-06-25 15:40:00 | GOES-19 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 140.1 |
| f554639b-632b-3350-8f66-e1d359195cb2 | -6.9275 | -47.8432 | 2026-06-25 15:40:00 | GOES-19 | WANDERLÂNDIA | TOCANTINS | Brasil | 1722081 | 17 | 33 | nan | nan | nan | Cerrado | 86.8 |
| 0e4e14b4-0902-31d3-a107-3fd99e91c81c | -11.2604 | -43.3197 | 2026-06-25 15:40:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Caatinga | 93.9 |
| 6c3a07d9-eab7-30a8-a935-e96d415de0f8 | -7.7498 | -44.6184 | 2026-06-25 15:40:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 90.0 |
| b2a27a88-44c2-3437-9977-18c8fa572dc5 | -8.3218 | -47.1307 | 2026-06-25 15:50:00 | GOES-19 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 116.5 |
| 917e90aa-4678-3dbe-8c25-80de671d6e03 | -7.7498 | -44.6184 | 2026-06-25 15:50:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 92.0 |
| 0cbdd31e-773a-3482-89c6-d6fc625a4f04 | -7.7498 | -44.6184 | 2026-06-25 16:00:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 101.0 |
| 9d199f92-7d16-3cff-83bd-7f7f988726dc | -6.9275 | -47.8432 | 2026-06-25 16:00:00 | GOES-19 | WANDERLÂNDIA | TOCANTINS | Brasil | 1722081 | 17 | 33 | nan | nan | nan | Cerrado | 78.3 |
| 2258a0fe-fbe6-387d-be81-d3c86a5ca53e | -6.5924 | -43.8957 | 2026-06-25 16:10:00 | GOES-19 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 72.4 |
| b461d432-0286-3d4c-a4f6-3ca7678143ff | -7.7498 | -44.6184 | 2026-06-25 16:10:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 92.2 |
| 38142ca1-f8a5-313f-aff1-c02af7a40a2d | -8.3218 | -47.1307 | 2026-06-25 16:10:00 | GOES-19 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 217.3 |
| 95ea7086-6150-386f-a0df-3cd443441fc1 | -6.9275 | -47.8432 | 2026-06-25 16:10:00 | GOES-19 | WANDERLÂNDIA | TOCANTINS | Brasil | 1722081 | 17 | 33 | nan | nan | nan | Cerrado | 98.2 |
| 074a0e35-b403-32d3-ae44-b70dae30afd7 | -8.3218 | -47.1307 | 2026-06-25 16:20:00 | GOES-19 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 106.6 |
| 8d07c9af-786f-3cbc-8804-9d4f920da6d7 | -7.7498 | -44.6184 | 2026-06-25 16:20:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 106.5 |
| f53e4e54-1181-3eb7-92e3-82b6263e07c1 | -6.5924 | -43.8957 | 2026-06-25 16:20:00 | GOES-19 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 98.0 |
| 29ee2e65-b477-3b6a-827b-80983773451b | -7.7498 | -44.6184 | 2026-06-25 16:30:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 80.9 |
| d282e414-6e01-3266-9c63-fdb9652e39db | -6.3036 | -44.6557 | 2026-06-25 16:30:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 68.6 |
| 3e0d8a53-4f89-39e7-be64-32b549e9368b | -6.5924 | -43.8957 | 2026-06-25 16:30:00 | GOES-19 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 108.1 |
| 1e4a6d72-f3fe-31b0-bead-f4f78895e271 | -6.9979 | -42.9016 | 2026-06-25 16:40:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 64.7 |
| 989a9125-cd0e-3bb1-a41d-70ad58d9a34e | -6.3036 | -44.6557 | 2026-06-25 16:40:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 149.5 |
| 6c2ab2ed-0b39-3b2e-9186-ade04201a84b | -5.776 | -45.0372 | 2026-06-25 16:40:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 89.2 |
| a73bfce8-d273-3ef7-85d1-b77a4a8dc749 | -6.5924 | -43.8957 | 2026-06-25 16:40:00 | GOES-19 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 84.9 |


