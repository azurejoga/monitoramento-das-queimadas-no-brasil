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

## Dados Diários - Página 98

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| fa9c8ccf-dfc3-3cc6-ab99-021cbdf484c3 | -4.21005 | -48.55249 | 2024-11-09 04:55:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| c818ef66-b21b-3628-96ac-924c35b4adb4 | -1.41668 | -54.7715 | 2024-11-09 04:55:00 | NPP-375D | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 8de6e62b-6eb3-3ed1-8f59-bddaacb98920 | 0.60584 | -51.86928 | 2024-11-09 04:55:00 | NPP-375D | PORTO GRANDE | AMAPÁ | Brasil | 1600535 | 16 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 46fcf1d1-68e7-3a40-83ef-818422a246f5 | -2.10422 | -46.21271 | 2024-11-09 04:55:00 | NPP-375D | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| a99dd6f7-8c79-38a0-86c0-ac746bfbbf54 | -1.51627 | -51.61011 | 2024-11-09 04:55:00 | NPP-375D | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 268c8ec3-e3d1-3ebd-9094-5296268c695a | -2.47325 | -53.98142 | 2024-11-09 04:55:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 968e1ce6-9a55-35a0-9cd7-608983890810 | -2.92074 | -51.67289 | 2024-11-09 04:55:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| bf9663f4-178c-31a9-93b8-f7d6d915fb65 | -3.58998 | -50.27425 | 2024-11-09 04:55:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 844ce1f9-f37e-35da-95cc-8b01dcb11dbc | -3.1918 | -50.44035 | 2024-11-09 04:55:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| d0cc225a-e5b9-379c-94be-c004f7f4659b | -2.21589 | -53.7206 | 2024-11-09 04:55:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 41beece7-0725-3a54-9371-397c514e9307 | -3.63709 | -50.18488 | 2024-11-09 04:55:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 10.5 |
| 479686f0-c457-3cba-80f1-0c8cdb291edc | -2.28319 | -53.81289 | 2024-11-09 04:55:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| fc4b5e1f-6acf-324b-8ad3-36e3d30ee166 | -1.52011 | -52.189 | 2024-11-09 04:55:00 | NPP-375D | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 17.3 |
| 950458a7-04cf-3161-8398-5017a1ce6fcf | -1.39049 | -51.56857 | 2024-11-09 04:55:00 | NPP-375D | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| e853e7ce-9ad7-3e97-a0f8-8d42d9c09d92 | -2.89085 | -49.38577 | 2024-11-09 04:55:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| e28a40d2-b856-3ab6-81e0-a90aede9ba3a | -1.18984 | -53.66301 | 2024-11-09 04:55:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 3f4abe63-f62a-30f2-b45d-ceb763865294 | -2.67374 | -51.82356 | 2024-11-09 04:55:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 8.1 |
| df865aeb-ae21-3cc9-8264-585b50e74288 | -3.27615 | -53.41614 | 2024-11-09 04:55:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 5a65af7e-c4fd-3d99-9825-ba7a792536c8 | -4.29484 | -48.64904 | 2024-11-09 04:55:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 59f3914a-93be-363a-ba73-fea42096c046 | -2.31177 | -47.43028 | 2024-11-09 04:55:00 | NPP-375D | CAPITÃO POÇO | PARÁ | Brasil | 1502301 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| ba8e3503-f69c-3d99-b27c-542a5d086d46 | -2.15623 | -53.65104 | 2024-11-09 04:55:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| e0230527-2340-3d1f-9119-8be26233401c | 1.08593 | -51.30399 | 2024-11-09 04:55:00 | NPP-375D | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 1.5 |
| ba778bb0-acac-3c95-8f1e-4e117c774c85 | -3.04459 | -50.37426 | 2024-11-09 04:55:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 1c0b0754-e521-3048-aa5e-f3070d882ad1 | -3.28892 | -53.24859 | 2024-11-09 04:55:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 2fbb2a11-4358-33bf-8696-bc33a7cf2329 | -2.61121 | -51.75159 | 2024-11-09 04:55:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| cc40f8e1-4a46-3f7b-af3f-b7433c91061d | -2.92971 | -54.43463 | 2024-11-09 04:55:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| e4bd5cf6-7cde-3af5-b6b7-7fb691456bc8 | -3.10095 | -53.71023 | 2024-11-09 04:55:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| c1717f3a-184e-320c-8951-feb745aca56a | -1.61222 | -48.67582 | 2024-11-09 04:55:00 | NPP-375D | BARCARENA | PARÁ | Brasil | 1501303 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| cb7fafe4-6f40-38b4-9173-2a713ee57fee | -3.18813 | -54.31176 | 2024-11-09 04:55:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| c81452be-f784-3bdf-910c-b9757b952763 | -2.96842 | -49.28483 | 2024-11-09 04:55:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 98b1198e-0e6e-314b-b0a7-5940cb75aa7b | -2.18388 | -52.7432 | 2024-11-09 04:55:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| d1f3f501-3451-32d7-8102-c4565600ce68 | -2.11779 | -50.13378 | 2024-11-09 04:55:00 | NPP-375D | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| e2cb1e37-0cf5-382f-bdce-aec7e9243bde | -4.21147 | -50.62138 | 2024-11-09 04:55:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| af3d1265-ad94-3dfc-b386-7d470b334e91 | -4.22188 | -48.61184 | 2024-11-09 04:55:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| f37735fa-e0d5-3ded-8c1d-953c4e1da9e6 | -2.67158 | -53.02164 | 2024-11-09 04:55:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 157d942b-0d6e-3820-b0c7-ca6cad6b7055 | -2.23707 | -50.69569 | 2024-11-09 04:55:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| cbc1ce1d-1cee-3423-bca0-8b64d20ea1a5 | -4.12828 | -54.89826 | 2024-11-09 04:55:00 | NPP-375D | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| f225d194-064c-3c63-ab12-5225ba4c50cf | -0.04015 | -50.7833 | 2024-11-09 04:55:00 | NPP-375D | AFUÁ | PARÁ | Brasil | 1500305 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| be172d26-620e-371e-848c-aced630c89ff | -1.44951 | -55.31481 | 2024-11-09 04:55:00 | NPP-375D | CURUÁ | PARÁ | Brasil | 1502855 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 18eebb9f-d207-37c8-8af4-b8ce7f1e0191 | -3.07926 | -50.56511 | 2024-11-09 04:55:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 15.2 |
| 59e7794f-5738-3b3a-974b-c3f43976399e | -2.79601 | -48.28313 | 2024-11-09 04:55:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 92245f3f-93f9-3791-a81b-ea54c83b9bcf | -2.9567 | -53.72341 | 2024-11-09 04:55:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 607c99e7-8d0e-3bf0-b5bf-d0e206b74f1d | -4.60705 | -49.58027 | 2024-11-09 04:55:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 552f8847-fe30-37df-b3db-59a353241db5 | -4.07842 | -49.29231 | 2024-11-09 04:55:00 | NPP-375D | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| bd461886-9ced-3dc3-b18a-39b21f8a47cb | -3.63965 | -45.89178 | 2024-11-09 04:55:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 0055d1c6-7b1f-36ae-8a7b-744d2ac2fb45 | -2.36296 | -54.75345 | 2024-11-09 04:55:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 8.7 |
| a8af3d45-36ae-382d-998e-6e635ba977b4 | -2.36073 | -54.74567 | 2024-11-09 04:55:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 8b858a00-9f9a-3ea6-8308-dc1cd5d00c13 | -3.95367 | -48.15886 | 2024-11-09 04:55:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 74e6f4fc-a311-3247-b1c7-467ca942b377 | -4.78207 | -48.68626 | 2024-11-09 04:55:00 | NPP-375D | BOM JESUS DO TOCANTINS | PARÁ | Brasil | 1501576 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 879f4b84-93f0-3cc5-823c-7b2f2d992758 | -3.05064 | -53.2787 | 2024-11-09 04:55:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| fa99da4c-6418-36bd-82d7-3b91de329434 | -4.66798 | -44.33733 | 2024-11-09 04:55:00 | NPP-375D | CAPINZAL DO NORTE | MARANHÃO | Brasil | 2102754 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 4d5cc60f-45f8-3fd3-9938-6d9994d04f74 | -1.60245 | -53.32311 | 2024-11-09 04:55:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 9566df82-946e-312f-9381-73114475906d | -4.07169 | -48.31609 | 2024-11-09 04:55:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 7ac65b79-270a-3ef8-b8ca-9e495d434dfa | -6.27325 | -41.65312 | 2024-11-09 04:55:00 | NPP-375D | AROAZES | PIAUÍ | Brasil | 2200905 | 22 | 33 | nan | nan | nan | Caatinga | 4.5 |
| 13e30eeb-5b76-3652-b978-95281408491d | -2.3148 | -53.86767 | 2024-11-09 04:55:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| b5d0158d-a9ea-3e7b-8598-65dbee6d93c6 | -3.15229 | -54.48355 | 2024-11-09 04:55:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| ab96def7-7e29-3dcd-9db6-b228b202dc1d | -2.18888 | -53.63839 | 2024-11-09 04:55:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| de4c9768-1964-353f-adbc-505f8fc54dac | -3.14261 | -52.97489 | 2024-11-09 04:55:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 23.1 |
| 1ca6ee95-2db5-3f50-987f-a510421d2763 | -3.02181 | -53.87188 | 2024-11-09 04:55:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| a96cc936-9c2b-39be-b22c-327ca9cc5475 | -3.0806 | -49.55821 | 2024-11-09 04:55:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| ad9de17c-8c48-3173-bf3b-d257e7ea8190 | -4.05992 | -48.31052 | 2024-11-09 04:55:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 479a579f-2859-3ab1-9d1e-0b61f85feb79 | -0.90934 | -51.65586 | 2024-11-09 04:55:00 | NPP-375D | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 2f66cebf-e51e-3d12-aed4-a70c46077519 | -2.48176 | -54.05137 | 2024-11-09 04:55:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 06fa536b-1ca6-3a7b-8f07-b00a75064cf7 | -3.23709 | -50.45572 | 2024-11-09 04:55:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| d3d67da9-9df1-37eb-9ee2-736a55ed8089 | -2.57326 | -47.34565 | 2024-11-09 04:55:00 | NPP-375D | CAPITÃO POÇO | PARÁ | Brasil | 1502301 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 8d537595-87b9-3c5c-ada7-7f1f7702e60e | -1.19659 | -53.70698 | 2024-11-09 04:55:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 2ebaea1c-437b-33be-a674-2b7f1ef2446d | -2.80742 | -52.99655 | 2024-11-09 04:55:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 3faa99c6-a22d-3ed0-b42e-f4fd4d49f274 | -2.55899 | -53.97392 | 2024-11-09 04:55:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 29bec584-f29f-3b7a-a897-2ae30d2da565 | -2.29846 | -46.73981 | 2024-11-09 04:55:00 | NPP-375D | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| b821eec0-bf1f-36e2-932e-122c559420ec | -2.45731 | -50.29852 | 2024-11-09 04:55:00 | NPP-375D | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| cb105e61-92f7-37da-b119-98b83623c526 | -2.0804 | -50.33971 | 2024-11-09 04:55:00 | NPP-375D | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 098d5192-8756-38b6-b57c-b47e72e857a5 | -2.38422 | -49.80338 | 2024-11-09 04:55:00 | NPP-375D | OEIRAS DO PARÁ | PARÁ | Brasil | 1505205 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 4d72de7b-a204-3e62-b1df-3ae79313a901 | -3.04087 | -50.32765 | 2024-11-09 04:55:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 951d029f-9720-359e-b505-d1fe0abff502 | -2.93403 | -51.05419 | 2024-11-09 04:55:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 8c749bfc-ed4d-3cd0-90b8-23375a0aa2d6 | -2.63394 | -46.7921 | 2024-11-09 04:55:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| caa8ad98-2f2d-3471-b54a-c430952df6e0 | -6.23031 | -47.2828 | 2024-11-09 04:55:00 | NPP-375D | CAMPESTRE DO MARANHÃO | MARANHÃO | Brasil | 2102556 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 777d747b-0489-3404-b332-e71f420255bc | -1.23936 | -51.77499 | 2024-11-09 04:55:00 | NPP-375D | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| a4c9ff12-f334-3263-9efa-6543a3093e57 | -2.7997 | -51.96022 | 2024-11-09 04:55:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| af47473c-bd0f-33d8-93be-d817bb1b7926 | -3.33205 | -50.08668 | 2024-11-09 04:55:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| b774083c-9e19-3f4e-9df5-9f26078b74eb | -5.27523 | -44.77037 | 2024-11-09 04:55:00 | NPP-375D | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| e1748330-ddc8-3240-89d5-f96de1a51528 | -4.22571 | -50.64854 | 2024-11-09 04:55:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| bbde48a4-dffa-3e12-ad34-886e4fa24769 | -4.62178 | -46.5393 | 2024-11-09 04:55:00 | NPP-375D | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 99f29a96-48a7-3864-af36-35c013873ea2 | -2.98601 | -51.45776 | 2024-11-09 04:55:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| c6f20191-b1c1-3311-b28c-b771f8e53731 | -3.44174 | -52.07286 | 2024-11-09 04:55:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| dfdf406e-3498-38bf-8cf5-d3a2e7130c1d | -2.72424 | -53.97462 | 2024-11-09 04:55:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 0627aa69-d54a-3bb0-a35a-a7cba9913cc7 | -2.83716 | -49.43572 | 2024-11-09 04:55:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| d27cdd91-1ec6-34e5-9d47-063accc44bc6 | -1.56432 | -51.66497 | 2024-11-09 04:55:00 | NPP-375D | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 527aa4d3-12ee-3b7b-aa65-b96347464c8d | -2.61506 | -51.30299 | 2024-11-09 04:55:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 3be9bfef-5450-3023-997e-fd07bd4a4835 | -3.89525 | -50.08071 | 2024-11-09 04:55:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 69b853a4-913e-3d41-b62b-2ede82ab1324 | -4.70815 | -55.99006 | 2024-11-09 04:55:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| d441f8e4-8309-31d3-9c30-873173755f3e | -2.94708 | -53.93486 | 2024-11-09 04:55:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 9e053255-4a8e-3016-b032-56b063a86f1e | -2.39838 | -48.49743 | 2024-11-09 04:55:00 | NPP-375D | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| e2bcb1e6-9526-3df1-970c-1e28080226a0 | -2.74279 | -51.96196 | 2024-11-09 04:55:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 4dcf1a98-7208-38e6-b8a8-87b5c048cb13 | -4.24921 | -48.54038 | 2024-11-09 04:55:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| e599b3c9-a9a1-331e-8f41-118eb2b0c896 | -4.38043 | -48.5752 | 2024-11-09 04:55:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| ced848b6-96eb-303b-8d98-f0ff71798ab1 | -5.13449 | -60.36686 | 2024-11-09 04:55:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 46fb0a3b-f37a-3e71-8b09-5b4e9f2e2a46 | -3.09389 | -53.3278 | 2024-11-09 04:55:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 554e5d81-2e83-3125-8a1f-e0db0b65b632 | -7.6308 | -43.54577 | 2024-11-09 04:55:00 | NPP-375D | CANAVIEIRA | PIAUÍ | Brasil | 2202251 | 22 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 2d01f811-9500-3fe4-bfae-26520f9b1435 | -2.65192 | -49.23841 | 2024-11-09 04:55:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| c5840a4b-0bfd-331c-95eb-b1739b9e8906 | -2.20886 | -50.34135 | 2024-11-09 04:55:00 | NPP-375D | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |


[Clique aqui para ver as próximas entradas](README99.md)
