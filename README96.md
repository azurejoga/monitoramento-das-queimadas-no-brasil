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

## Dados Diários - Página 96

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 717000a5-da28-3df3-9ae7-f13ab7506a45 | -6.7503 | -58.7462 | 2025-09-04 08:10:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 64.3 |
| 9dae9384-e3e6-3c7e-ba16-daf86a47f556 | -6.7782 | -44.0876 | 2025-09-04 08:10:00 | GOES-19 | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 64.0 |
| 326d6eef-3e24-36e5-a825-d996d019acad | -5.871 | -57.7715 | 2025-09-04 08:10:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 44.9 |
| 8cd4535e-d71b-31d7-9714-68babb402412 | -6.7504 | -58.7268 | 2025-09-04 08:10:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 77.0 |
| f2fd756f-a10e-3b01-bf24-f6bc9995f1a7 | -5.8525 | -57.7722 | 2025-09-04 08:10:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 49.9 |
| 987e9b17-f4a0-3fb9-92ee-f8113e48fc52 | -8.0417 | -45.3882 | 2025-09-04 08:10:00 | GOES-19 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 58.0 |
| cb6a0cdd-fb7a-3b18-8115-3f2276e1edb7 | -9.6043 | -47.0437 | 2025-09-04 08:20:00 | GOES-19 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 61.3 |
| 8f4d0fc3-3154-323a-9068-8eff86da456c | -5.8525 | -57.7722 | 2025-09-04 08:20:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 56.1 |
| 3f37ce8f-1540-3554-baf3-3803147c2d5f | -6.7503 | -58.7462 | 2025-09-04 08:20:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 57.5 |
| c0392740-2239-3c8b-936f-2d92d140acf2 | -7.6851 | -48.7386 | 2025-09-04 08:20:00 | GOES-19 | BANDEIRANTES DO TOCANTINS | TOCANTINS | Brasil | 1703057 | 17 | 33 | nan | nan | nan | Amazônia | 53.5 |
| f29b743e-dff0-362e-8e55-a4658e8ea2cc | -4.9951 | -56.256 | 2025-09-04 08:20:00 | GOES-19 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 40.0 |
| 2b055f42-3b61-3303-be6a-02ea8b95174b | -8.0228 | -45.39 | 2025-09-04 08:20:00 | GOES-19 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 56.1 |
| e80a7de6-8b05-3d17-ade1-deb854d19bbe | -6.7504 | -58.7268 | 2025-09-04 08:20:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 72.6 |
| a8294fe1-ffae-31f8-a231-ce1d932b1fe4 | -5.908 | -57.7311 | 2025-09-04 08:20:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 76.1 |
| 06762696-ea1e-3c93-8c53-c868def1dc6e | -7.7252 | -50.3174 | 2025-09-04 08:20:00 | GOES-19 | PAU D'ARCO | PARÁ | Brasil | 1505551 | 15 | 33 | nan | nan | nan | Amazônia | 29.6 |
| e5233ebc-ea1e-3b91-8002-701fc862b12f | -4.9951 | -56.256 | 2025-09-04 08:30:00 | GOES-19 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 38.8 |
| b6050875-f9e6-37cf-aa91-27a022553d9d | -6.7503 | -58.7462 | 2025-09-04 08:30:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 58.6 |
| 1c28693f-ab46-3a41-9695-ce4bff14c5b8 | -9.6043 | -47.0437 | 2025-09-04 08:30:00 | GOES-19 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 75.9 |
| 6169b414-7552-3751-bf3c-4bbae4849e22 | -5.8525 | -57.7722 | 2025-09-04 08:30:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 56.5 |
| 7afcea6c-4780-3b58-8835-bb46cf5d52cf | -7.7252 | -50.3174 | 2025-09-04 08:30:00 | GOES-19 | PAU D'ARCO | PARÁ | Brasil | 1505551 | 15 | 33 | nan | nan | nan | Amazônia | 30.6 |
| bf24f21a-80ed-359b-8762-1df140eba47a | -6.7504 | -58.7268 | 2025-09-04 08:30:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 73.1 |
| 8a490dd0-40c4-3352-b151-cce743a24179 | -5.908 | -57.7311 | 2025-09-04 08:30:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 67.1 |
| 19307623-60a4-3dc9-96be-55b63181fa81 | -23.7574 | -51.9145 | 2025-09-04 08:40:00 | GOES-19 | SÃO PEDRO DO IVAÍ | PARANÁ | Brasil | 4125803 | 41 | 33 | nan | nan | nan | Mata Atlântica | 115.8 |
| 7af75183-17ab-3b24-92f4-6267c993450b | -5.908 | -57.7311 | 2025-09-04 08:40:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 51.8 |
| 10b17f38-3d97-37a0-a79a-b9edfbeb1d65 | -23.7362 | -51.9193 | 2025-09-04 08:40:00 | GOES-19 | SÃO PEDRO DO IVAÍ | PARANÁ | Brasil | 4125803 | 41 | 33 | nan | nan | nan | Mata Atlântica | 154.8 |
| bc508a38-7ee8-3e1d-9722-bccbc223c711 | -5.871 | -57.7715 | 2025-09-04 08:40:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 52.9 |
| b9b2fd39-5a2c-3080-a6ff-dde5dff4e371 | -4.9951 | -56.256 | 2025-09-04 08:40:00 | GOES-19 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 42.0 |
| ea37940e-7b66-3ca7-85b9-94e5c6f1e7c9 | -23.7369 | -51.8964 | 2025-09-04 08:40:00 | GOES-19 | BOM SUCESSO | PARANÁ | Brasil | 4103206 | 41 | 33 | nan | nan | nan | Mata Atlântica | 105.3 |
| 302668f6-3bf5-315c-9872-4b8a8c2d453b | -23.758 | -51.8917 | 2025-09-04 08:40:00 | GOES-19 | BOM SUCESSO | PARANÁ | Brasil | 4103206 | 41 | 33 | nan | nan | nan | Mata Atlântica | 84.9 |
| bf3cf81d-4f97-3187-94c9-d2b406b3e97e | -6.7504 | -58.7268 | 2025-09-04 08:40:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 62.9 |
| 8c1768b6-21c5-3ecf-a708-44082e0fa432 | -5.8896 | -57.7318 | 2025-09-04 08:40:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 36.9 |
| fa63c544-ad8e-33ad-ad18-fb57c54329cd | -6.7504 | -58.7268 | 2025-09-04 08:50:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 67.5 |
| 91edfa6e-bf52-3882-a612-84e87b22dce3 | -5.908 | -57.7311 | 2025-09-04 08:50:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 56.2 |
| ff7a870e-7b05-307d-8ffb-a617d160eb3e | -5.871 | -57.7715 | 2025-09-04 08:50:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 50.2 |
| b65c18b3-ce9e-3fbc-8d74-eb7c55079b26 | -4.9951 | -56.256 | 2025-09-04 08:50:00 | GOES-19 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 37.8 |
| ad935bd7-791f-3b78-afba-12840485057f | -5.8525 | -57.7722 | 2025-09-04 08:50:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 45.3 |
| 51edba59-ee7e-3d07-ade6-79e23f8ddf4c | -5.871 | -57.7715 | 2025-09-04 09:00:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 35.3 |
| 2d8d794c-7a84-389e-bdd1-4dad1295763a | -4.9951 | -56.256 | 2025-09-04 09:00:00 | GOES-19 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 39.9 |
| bbe52888-3f1c-3f4c-b241-d9317cec0d63 | -5.908 | -57.7311 | 2025-09-04 09:00:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 64.1 |
| 1e8ae419-7a6c-3b81-bf83-5e2fc27e3d93 | -6.7504 | -58.7268 | 2025-09-04 09:00:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 61.1 |
| efdd7f6b-1596-365b-99de-8799352f20e6 | -5.871 | -57.7715 | 2025-09-04 09:10:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 45.3 |
| 46734f4e-d906-3c50-940d-8362b5e81fc0 | -5.8525 | -57.7722 | 2025-09-04 09:10:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 41.8 |
| 06db54f8-4922-35e5-9f28-c6cd9aefb337 | -5.908 | -57.7311 | 2025-09-04 09:10:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 67.2 |
| 7c0fec0a-8b7e-3924-ab1c-719b529ac6e9 | -6.7504 | -58.7268 | 2025-09-04 09:10:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 58.9 |
| 493e0289-1a12-3071-9c95-8639bc5f3020 | -8.0417 | -45.3882 | 2025-09-04 10:30:00 | GOES-19 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 86.6 |
| 2e9a2abe-f3f0-3780-8882-d1a1c38f7bcb | -8.0417 | -45.3882 | 2025-09-04 10:40:00 | GOES-19 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 91.2 |
| d6569179-d3f9-3697-ab58-d9cf0f63bee9 | -11.853 | -51.453 | 2025-09-04 10:50:00 | GOES-19 | ALTO BOA VISTA | MATO GROSSO | Brasil | 5100359 | 51 | 33 | nan | nan | nan | Cerrado | 131.2 |
| a506df64-1557-384d-b1cb-078a36e91f11 | -11.853 | -51.453 | 2025-09-04 11:00:00 | GOES-19 | ALTO BOA VISTA | MATO GROSSO | Brasil | 5100359 | 51 | 33 | nan | nan | nan | Cerrado | 99.6 |
| 3bc8fbe2-463a-388d-8fb2-9cfe34acd53a | -6.3692 | -45.6258 | 2025-09-04 11:00:00 | GOES-19 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 106.7 |
| d2637c78-a6e5-3705-aeda-85888b61f8f5 | -11.853 | -51.453 | 2025-09-04 11:10:00 | GOES-19 | ALTO BOA VISTA | MATO GROSSO | Brasil | 5100359 | 51 | 33 | nan | nan | nan | Cerrado | 125.8 |
| a0bb9606-4ae4-3a8b-a2f2-47ad3093c5ac | -6.3692 | -45.6258 | 2025-09-04 11:10:00 | GOES-19 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 92.7 |
| 480b6111-eb31-309c-9f6f-872682d5e330 | -10.4469 | -50.3926 | 2025-09-04 11:20:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 130.3 |
| be568766-5fd8-3293-9208-86abe3bc614a | -7.974 | -46.3406 | 2025-09-04 11:20:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 109.3 |
| c5a9c043-a4e6-3b99-b6d6-580d14ca0940 | -11.853 | -51.453 | 2025-09-04 11:20:00 | GOES-19 | ALTO BOA VISTA | MATO GROSSO | Brasil | 5100359 | 51 | 33 | nan | nan | nan | Cerrado | 109.4 |
| 428cba55-dfb4-3380-9cdd-ddc275b06fc0 | -6.2318 | -42.4278 | 2025-09-04 11:20:00 | GOES-19 | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | 90.5 |
| 0b69fd17-cf33-354f-acd8-90ce1f438201 | -8.0417 | -45.3882 | 2025-09-04 11:20:00 | GOES-19 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 77.1 |
| 4c37198c-3312-3b1c-83a2-261cd21920b9 | -10.4658 | -50.3907 | 2025-09-04 11:20:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 131.0 |
| c7234bc1-1ead-3551-9af2-d5c9780a1c5d | -8.0228 | -45.39 | 2025-09-04 11:20:00 | GOES-19 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 78.7 |
| 4ff6d293-e9ed-33ac-9bee-e6e71df69a15 | -6.2315 | -42.4515 | 2025-09-04 11:20:00 | GOES-19 | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 89.9 |
| e44c0ffa-ff6d-3a33-b012-f54ecff5b254 | -6.2318 | -42.4278 | 2025-09-04 11:30:00 | GOES-19 | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | 99.3 |
| 30e7639c-d72a-394b-8735-7e4cb86c60fe | -6.2315 | -42.4515 | 2025-09-04 11:30:00 | GOES-19 | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 129.7 |
| 784323ac-b454-38d2-a4bc-5935d473789f | -5.7 | -45.1786 | 2025-09-04 11:30:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 84.5 |
| 72891b59-af21-3b07-9178-3a03926fc905 | -10.4469 | -50.3926 | 2025-09-04 11:30:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 95.3 |
| c2be8df0-19a8-3872-8fdc-2234124e085f | -11.853 | -51.453 | 2025-09-04 11:30:00 | GOES-19 | ALTO BOA VISTA | MATO GROSSO | Brasil | 5100359 | 51 | 33 | nan | nan | nan | Cerrado | 85.9 |
| 0a597dca-8d77-3b29-b91e-54db0eec63b7 | -5.6963 | -45.6076 | 2025-09-04 11:30:00 | GOES-19 | JENIPAPO DOS VIEIRAS | MARANHÃO | Brasil | 2105476 | 21 | 33 | nan | nan | nan | Cerrado | 96.8 |
| c9cff80a-266d-3749-ab2f-196f13ea62b0 | -7.6851 | -48.7386 | 2025-09-04 11:30:00 | GOES-19 | BANDEIRANTES DO TOCANTINS | TOCANTINS | Brasil | 1703057 | 17 | 33 | nan | nan | nan | Amazônia | 75.8 |
| 175b7aca-8d57-3408-9e35-883b41669651 | -10.4658 | -50.3907 | 2025-09-04 11:30:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 164.0 |
| 488feb1a-b148-361a-8e3b-e138e997589f | -10.4658 | -50.3907 | 2025-09-04 11:40:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 146.3 |
| 3e8742ea-aa09-3c3e-83fd-626499e2fbc4 | -10.9855 | -49.7562 | 2025-09-04 11:40:00 | GOES-19 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 76.8 |
| d989d68a-d1e8-3a80-adb5-038946e0482c | -6.2318 | -42.4278 | 2025-09-04 11:40:00 | GOES-19 | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | 139.1 |
| c5686235-b4b7-311e-8ead-e7b4c2c3fbf9 | -7.7039 | -48.7371 | 2025-09-04 11:40:00 | GOES-19 | BANDEIRANTES DO TOCANTINS | TOCANTINS | Brasil | 1703057 | 17 | 33 | nan | nan | nan | Amazônia | 72.6 |
| 1cced61d-15ce-3b69-9d31-bfa1335a1207 | -10.4469 | -50.3926 | 2025-09-04 11:40:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 100.9 |
| 41c65bec-8924-386a-ac61-56e9800d3c66 | -7.7036 | -48.7587 | 2025-09-04 11:40:00 | GOES-19 | ARAPOEMA | TOCANTINS | Brasil | 1702307 | 17 | 33 | nan | nan | nan | Amazônia | 109.6 |
| 6eb04831-3135-3b20-854a-f6f791cf343c | -11.853 | -51.453 | 2025-09-04 11:40:00 | GOES-19 | ALTO BOA VISTA | MATO GROSSO | Brasil | 5100359 | 51 | 33 | nan | nan | nan | Cerrado | 110.2 |
| 644afcf5-48cd-3896-bdce-e495d0de978b | -6.2315 | -42.4515 | 2025-09-04 11:40:00 | GOES-19 | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 154.2 |
| bef47cda-9e63-3daf-8da8-ec5dbfe6b9f9 | -7.6849 | -48.7602 | 2025-09-04 11:40:00 | GOES-19 | ARAPOEMA | TOCANTINS | Brasil | 1702307 | 17 | 33 | nan | nan | nan | Amazônia | 74.3 |
| 771a0b92-419d-3194-a0c5-715b48eb76c5 | -5.6777 | -45.6089 | 2025-09-04 11:50:00 | GOES-19 | JENIPAPO DOS VIEIRAS | MARANHÃO | Brasil | 2105476 | 21 | 33 | nan | nan | nan | Cerrado | 78.6 |
| 4ae65a5e-0591-3ec4-b458-6a4da92d917e | -5.7 | -45.1786 | 2025-09-04 11:50:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 194.4 |
| a9afd855-31d8-3e3e-a405-c23c072b7e57 | -5.7002 | -45.156 | 2025-09-04 11:50:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 106.3 |
| f946fc7f-2353-3bb4-a107-94f3607718f0 | -13.8457 | -47.9764 | 2025-09-04 11:50:00 | GOES-19 | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 76.5 |
| c9828fae-4b4b-3ff9-a223-8a9d4f81710d | -7.7036 | -48.7587 | 2025-09-04 11:50:00 | GOES-19 | ARAPOEMA | TOCANTINS | Brasil | 1702307 | 17 | 33 | nan | nan | nan | Amazônia | 204.3 |
| f98e5696-63c6-36e4-8b6f-8a7900f17e18 | -6.3692 | -45.6258 | 2025-09-04 11:50:00 | GOES-19 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 77.5 |
| 1aa303f0-e8c5-312c-a1bd-282a755afd9d | -10.4658 | -50.3907 | 2025-09-04 11:50:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 92.1 |
| 6c3b3f7f-370d-3a28-b7ee-7c6ca2298815 | -17.0652 | -46.449 | 2025-09-04 11:50:00 | GOES-19 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 134.8 |
| 250c264b-39e8-3568-bc55-d0bb395b74bb | -11.853 | -51.453 | 2025-09-04 11:50:00 | GOES-19 | ALTO BOA VISTA | MATO GROSSO | Brasil | 5100359 | 51 | 33 | nan | nan | nan | Cerrado | 78.7 |
| 84759986-a6d6-3baf-aafd-9f8335edaaf8 | -6.2315 | -42.4515 | 2025-09-04 11:50:00 | GOES-19 | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 136.1 |
| d7ad1fb7-a6e0-3b42-8b32-fb01dcd3dfe1 | -8.0417 | -45.3882 | 2025-09-04 11:50:00 | GOES-19 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 91.5 |
| 148466f2-0fdf-390c-94fa-f66e66e765fb | -7.7039 | -48.7371 | 2025-09-04 11:50:00 | GOES-19 | BANDEIRANTES DO TOCANTINS | TOCANTINS | Brasil | 1703057 | 17 | 33 | nan | nan | nan | Amazônia | 93.1 |
| 75aafe37-15e6-387e-b4e8-50d1008cdb3b | -8.0799 | -45.339 | 2025-09-04 11:50:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 96.7 |
| a89e5493-b024-3422-a453-068c2680cfe6 | -15.0648 | -50.0431 | 2025-09-04 11:50:00 | GOES-19 | NOVA AMÉRICA | GOIÁS | Brasil | 5214705 | 52 | 33 | nan | nan | nan | Cerrado | 87.8 |
| f27c46df-bc96-3bff-a5b4-da3624d1ea38 | -7.6851 | -48.7386 | 2025-09-04 11:50:00 | GOES-19 | BANDEIRANTES DO TOCANTINS | TOCANTINS | Brasil | 1703057 | 17 | 33 | nan | nan | nan | Amazônia | 74.3 |
| 7306638e-83d5-37a8-be09-c3ec6c0c5874 | -5.6963 | -45.6076 | 2025-09-04 11:50:00 | GOES-19 | JENIPAPO DOS VIEIRAS | MARANHÃO | Brasil | 2105476 | 21 | 33 | nan | nan | nan | Cerrado | 85.7 |
| 7a2cb3f3-0f0b-3b72-8006-dfd58275d71c | -6.2318 | -42.4278 | 2025-09-04 11:50:00 | GOES-19 | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | 133.1 |
| 9d8c5954-7f31-3906-bcef-b7fb2f3c6aaa | -10.1454 | -46.265 | 2025-09-04 12:00:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 115.9 |
| 6b9ccdb5-f0f6-3dc2-adc1-316a713c0255 | -11.853 | -51.453 | 2025-09-04 12:00:00 | GOES-19 | ALTO BOA VISTA | MATO GROSSO | Brasil | 5100359 | 51 | 33 | nan | nan | nan | Cerrado | 104.1 |
| cf32bc07-c8b9-3e67-8967-109a530b8d04 | -7.6851 | -48.7386 | 2025-09-04 12:00:00 | GOES-19 | BANDEIRANTES DO TOCANTINS | TOCANTINS | Brasil | 1703057 | 17 | 33 | nan | nan | nan | Amazônia | 87.1 |
| 3e276df0-f493-31fa-b916-c0394402e6ae | -7.7039 | -48.7371 | 2025-09-04 12:00:00 | GOES-19 | BANDEIRANTES DO TOCANTINS | TOCANTINS | Brasil | 1703057 | 17 | 33 | nan | nan | nan | Amazônia | 73.0 |
| e19a4547-5950-3354-8e3f-ddf74c2976ce | -5.6777 | -45.6089 | 2025-09-04 12:00:00 | GOES-19 | JENIPAPO DOS VIEIRAS | MARANHÃO | Brasil | 2105476 | 21 | 33 | nan | nan | nan | Cerrado | 292.6 |
| ceac593d-ed91-3f8b-ac05-c84272b597e9 | -8.0799 | -45.339 | 2025-09-04 12:00:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 149.1 |
| 0961e823-3ad1-3b1b-afa9-f3a8e4b43043 | -6.3692 | -45.6258 | 2025-09-04 12:00:00 | GOES-19 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 115.5 |


[Clique aqui para ver as próximas entradas](README97.md)
