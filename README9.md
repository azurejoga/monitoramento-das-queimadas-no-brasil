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

## Dados Diários - Página 9

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| bba67f23-d829-3d33-8dc3-74cf9f2d152a | 2.7164 | -60.22675 | 2026-02-25 05:54:00 | NOAA-20 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 0.7 |
| d9770737-b464-3284-8650-594bab676c32 | 1.82832 | -60.84921 | 2026-02-25 05:54:00 | NOAA-20 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.5 |
| ada3162b-1fb6-3c7b-8bda-5abec4c775da | 1.93992 | -60.36061 | 2026-02-25 05:54:00 | NOAA-20 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 1b993dfa-a8ed-323b-82e9-0f303419e82d | 1.49374 | -59.92562 | 2026-02-25 05:54:00 | NOAA-20 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 3.6 |
| ba34154c-e6d0-3711-9ece-df22a017fdc8 | 3.93415 | -60.05825 | 2026-02-25 05:54:00 | NOAA-20 | NORMANDIA | RORAIMA | Brasil | 1400407 | 14 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 564b5512-78bf-31ad-b6f0-fe805d215b7b | 4.1549 | -60.29394 | 2026-02-25 05:54:00 | NOAA-20 | NORMANDIA | RORAIMA | Brasil | 1400407 | 14 | 33 | nan | nan | nan | Amazônia | 1.6 |
| bee51b63-bc20-38ca-86a7-b76f9e959288 | 4.29428 | -60.76971 | 2026-02-25 05:54:00 | NOAA-20 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 92aec642-3262-37df-ba38-76eca6cf7283 | 4.25212 | -60.2785 | 2026-02-25 05:54:00 | NOAA-20 | UIRAMUTÃ | RORAIMA | Brasil | 1400704 | 14 | 33 | nan | nan | nan | Amazônia | 1.2 |
| e3b1465c-d8b7-33ed-91ae-a2e784d0c642 | 4.23731 | -60.28811 | 2026-02-25 05:54:00 | NOAA-20 | UIRAMUTÃ | RORAIMA | Brasil | 1400704 | 14 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 91c9326d-9d57-3ff3-98df-11bea8b859d0 | 3.92979 | -60.05897 | 2026-02-25 05:54:00 | NOAA-20 | NORMANDIA | RORAIMA | Brasil | 1400407 | 14 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 4c11b57e-4d93-3bf4-85d2-3d0673eeaa45 | 3.88109 | -59.73867 | 2026-02-25 05:54:00 | NOAA-20 | NORMANDIA | RORAIMA | Brasil | 1400407 | 14 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 0a1ea32d-5502-3631-8216-50e2b44bf0cb | 4.29017 | -60.77055 | 2026-02-25 05:54:00 | NOAA-20 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 44936dc2-18ba-3fd0-9269-17ce552d33a2 | 4.0686 | -60.18806 | 2026-02-25 05:54:00 | NOAA-20 | NORMANDIA | RORAIMA | Brasil | 1400407 | 14 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 394b31f9-7530-3b31-b442-5acf95bbb25b | 4.06993 | -60.19604 | 2026-02-25 05:54:00 | NOAA-20 | NORMANDIA | RORAIMA | Brasil | 1400407 | 14 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 13d06818-dc2a-3a82-bbf9-fd71e5ea8eb6 | 3.92543 | -60.05968 | 2026-02-25 05:54:00 | NOAA-20 | NORMANDIA | RORAIMA | Brasil | 1400407 | 14 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 47af37fd-6c58-30a1-885e-502ed38d116e | 3.88182 | -59.7431 | 2026-02-25 05:54:00 | NOAA-20 | NORMANDIA | RORAIMA | Brasil | 1400407 | 14 | 33 | nan | nan | nan | Amazônia | 3.8 |
| e6048498-324f-3f88-b50a-2f7d64c62217 | 4.2495 | -60.28217 | 2026-02-25 05:54:00 | NOAA-20 | UIRAMUTÃ | RORAIMA | Brasil | 1400704 | 14 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 7d674ab5-e457-37d0-b768-9541ac3dfa64 | 4.25279 | -60.28249 | 2026-02-25 05:54:00 | NOAA-20 | UIRAMUTÃ | RORAIMA | Brasil | 1400704 | 14 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 47230e42-a930-36fd-a0f8-65eab1390588 | 3.91977 | -60.4941 | 2026-02-25 05:54:00 | NOAA-20 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 3b5be819-4815-3caf-bc47-be075b66e8a5 | 4.23434 | -60.18839 | 2026-02-25 05:54:00 | NOAA-20 | UIRAMUTÃ | RORAIMA | Brasil | 1400704 | 14 | 33 | nan | nan | nan | Amazônia | 1.1 |
| fd4f0c67-9658-39b3-bf1c-4c3004e3f46b | 4.06927 | -60.19205 | 2026-02-25 05:54:00 | NOAA-20 | NORMANDIA | RORAIMA | Brasil | 1400407 | 14 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 5d76be61-1478-373e-adee-ad2436a2b54c | 3.88555 | -59.73794 | 2026-02-25 05:54:00 | NOAA-20 | NORMANDIA | RORAIMA | Brasil | 1400407 | 14 | 33 | nan | nan | nan | Amazônia | 0.7 |
| d38579d7-e298-3721-ad19-e09e292510b9 | 1.4864 | -59.9498 | 2026-02-25 06:00:00 | GOES-19 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 196.7 |
| 55deb8d5-7b69-38fa-b867-c1d0d63bd067 | 1.4864 | -59.9308 | 2026-02-25 06:00:00 | GOES-19 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 183.8 |
| 816bc3dc-9185-3694-943c-afe8cfc63fb4 | 1.5046 | -59.9306 | 2026-02-25 06:00:00 | GOES-19 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 165.5 |
| 124d7601-2d00-34f9-9e05-73b84f84a01b | 1.5046 | -59.9497 | 2026-02-25 06:00:00 | GOES-19 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 156.3 |
| b7bdda79-7cec-33d6-a6c0-1a00b6c6ae38 | 1.4864 | -59.9498 | 2026-02-25 06:10:00 | GOES-19 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 198.4 |
| c5dd8c39-39d4-3446-bfae-c480f1cab043 | 1.5046 | -59.9497 | 2026-02-25 06:10:00 | GOES-19 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 254.7 |
| c49823bd-8bdb-3f1a-912f-7848908ff796 | 1.4864 | -59.9308 | 2026-02-25 06:10:00 | GOES-19 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 136.6 |
| 28413906-1cfe-3313-8abe-89f8b8ddfbcf | 1.5046 | -59.9306 | 2026-02-25 06:10:00 | GOES-19 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 203.9 |
| 39cb79d2-932f-3141-95f2-d3bb88f987e5 | 1.4864 | -59.9498 | 2026-02-25 06:20:00 | GOES-19 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 179.1 |
| 50f26aab-56e9-3bcc-bb90-5f6f6c565fb4 | 1.4864 | -59.9308 | 2026-02-25 06:20:00 | GOES-19 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 161.0 |
| 8df05b68-ec0e-3fb0-8f19-b88e47fc2e66 | 1.5046 | -59.9306 | 2026-02-25 06:20:00 | GOES-19 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 203.9 |
| c9ef99b2-5543-36e0-8dec-4b55bdafd4a4 | 1.5046 | -59.9497 | 2026-02-25 06:20:00 | GOES-19 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 184.4 |
| 4bc9d468-3922-3e40-a188-2cba52b7da45 | 1.5229 | -59.9305 | 2026-02-25 06:30:00 | GOES-19 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 45.4 |
| 04f008ef-2635-3313-a321-b73519ea3c2f | 1.4864 | -59.9308 | 2026-02-25 06:30:00 | GOES-19 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 226.9 |
| 3b27598b-ffc9-3bfa-ae11-cdb70e974bbd | 1.5046 | -59.9497 | 2026-02-25 06:30:00 | GOES-19 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 198.7 |
| 21eac0fc-09c8-3422-8d2a-f1c5d8f7f06a | 1.4864 | -59.9498 | 2026-02-25 06:30:00 | GOES-19 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 231.8 |
| 6b114044-0522-3e7c-8eb4-42338195bda4 | 1.5046 | -59.9306 | 2026-02-25 06:30:00 | GOES-19 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 214.6 |
| 0c150511-5f91-3580-a9c9-2278078693e2 | 1.5229 | -59.9495 | 2026-02-25 06:30:00 | GOES-19 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 43.3 |
| 8758505b-f516-3e3b-a933-9c013b00df4e | 1.4864 | -59.9498 | 2026-02-25 06:40:00 | GOES-19 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 102.8 |
| 25134bf3-45d0-3cb6-be7c-71634a78f193 | 1.4864 | -59.9308 | 2026-02-25 06:40:00 | GOES-19 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 79.5 |
| c3a9ffe8-ac8c-31ab-b669-3042f2718512 | 1.5046 | -59.9306 | 2026-02-25 06:40:00 | GOES-19 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 73.7 |
| 16187e70-576b-3980-afaa-0df84190b0c8 | 1.5046 | -59.9497 | 2026-02-25 06:40:00 | GOES-19 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 72.9 |
| 2f3e1a68-3f1e-3940-a5b8-f8a254f328cb | 1.5046 | -59.9497 | 2026-02-25 06:50:00 | GOES-19 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 116.9 |
| 1da692fc-a0e8-3f9c-a2cd-1b3aca139d75 | 1.5046 | -59.9306 | 2026-02-25 06:50:00 | GOES-19 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 125.0 |
| 3760ddb4-e6c8-3d3a-ac8c-e8c052d792ec | 1.4864 | -59.9308 | 2026-02-25 06:50:00 | GOES-19 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 157.7 |
| 985cd5c4-930f-30a3-853f-1bc8e10dde79 | 1.4864 | -59.9498 | 2026-02-25 06:50:00 | GOES-19 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 146.5 |
| 569e8987-1976-3252-857b-ab3fa7f867a8 | 1.4864 | -59.9498 | 2026-02-25 07:00:00 | GOES-19 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 51.8 |
| 151e6bc3-00b8-3fe9-ad88-97cf1009dfb3 | 1.5046 | -59.9497 | 2026-02-25 07:00:00 | GOES-19 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 53.6 |
| f12f00a4-b756-360b-9cd6-62aa4cf2983a | 1.5046 | -59.9306 | 2026-02-25 07:00:00 | GOES-19 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 61.0 |
| 3b1e5b74-1266-3edc-9351-81d5650bc74c | 1.4864 | -59.9308 | 2026-02-25 07:00:00 | GOES-19 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 54.1 |
| 07fae0cb-c96c-30fb-a4f0-f2b6b2066fa3 | 1.5046 | -59.9497 | 2026-02-25 07:10:00 | GOES-19 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 52.8 |
| 2422d8c2-2ecf-37ce-be7c-3037fe26a9c6 | 1.4864 | -59.9498 | 2026-02-25 07:10:00 | GOES-19 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 61.9 |
| af0862ac-dd24-3666-836d-5a6598cc67d6 | 1.4864 | -59.9308 | 2026-02-25 07:10:00 | GOES-19 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 50.9 |
| 4fb147d4-08a6-3b43-994e-39f38b66d92a | 1.5046 | -59.9306 | 2026-02-25 07:10:00 | GOES-19 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 59.7 |
| d93b7dda-5db9-3400-82bc-51a8e6448a3d | 1.4864 | -59.9308 | 2026-02-25 07:20:00 | GOES-19 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 52.8 |
| 7643636c-694c-337c-936a-8dc1c5fb9ad4 | 1.4864 | -59.9498 | 2026-02-25 07:20:00 | GOES-19 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 106.1 |
| abb7d0c8-6993-3d76-9fc6-703175f05cdd | 1.4681 | -59.95 | 2026-02-25 07:20:00 | GOES-19 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 36.9 |
| 9840ccc7-b6fb-30bb-bc10-bbe1eac1afb9 | 1.5046 | -59.9306 | 2026-02-25 07:20:00 | GOES-19 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 48.3 |
| fc542b01-a8ec-3201-ba11-3c44180ae0bf | 1.4863 | -59.9688 | 2026-02-25 07:20:00 | GOES-19 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 38.0 |
| 3cdb15ec-1961-3a13-af46-39046b235ab9 | 1.5046 | -59.9497 | 2026-02-25 07:20:00 | GOES-19 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 70.7 |
| d0534615-7bbb-3529-b4f9-333eabeec474 | 1.4681 | -59.95 | 2026-02-25 07:30:00 | GOES-19 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 33.4 |
| 1b10a5bf-2ad6-3db5-93ee-de835ac6529a | 1.5046 | -59.9306 | 2026-02-25 07:30:00 | GOES-19 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 48.8 |
| 42d1d281-4816-3af6-9224-8390f6193715 | 1.4864 | -59.9498 | 2026-02-25 07:30:00 | GOES-19 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 96.1 |
| f12fbca7-39cd-377f-8a1a-0620abc8f8e2 | 1.5046 | -59.9497 | 2026-02-25 07:30:00 | GOES-19 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 63.2 |
| 8d6781f6-7e34-3bec-876c-94961fbb38bc | 1.4864 | -59.9308 | 2026-02-25 07:30:00 | GOES-19 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 60.4 |
| 5e248f20-fe28-3169-99c9-4dd40896391d | 3.45743 | -59.89409 | 2026-02-25 07:39:00 | AQUA_M-M | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 23.8 |
| d0126675-1ce0-3310-9a1b-4e0b695df6be | 1.48812 | -59.92303 | 2026-02-25 07:39:00 | AQUA_M-M | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 34.4 |
| 48afff3b-0d47-385d-8118-875d6b4e9ecf | 1.5046 | -59.9497 | 2026-02-25 07:40:00 | GOES-19 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 44.5 |
| 5235afc8-13e3-39bf-b020-22c19d61b909 | 1.5046 | -59.9306 | 2026-02-25 07:40:00 | GOES-19 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 36.9 |
| 5595f0e6-57c9-3a95-8850-d13ff15567a3 | 1.4864 | -59.9498 | 2026-02-25 07:40:00 | GOES-19 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 58.4 |
| 3f9fd4b4-9059-36e1-928e-3733b4b0d600 | 1.4864 | -59.9308 | 2026-02-25 07:40:00 | GOES-19 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 41.3 |
| 6b93b199-5675-341e-b6ee-3023fa6f32c4 | 1.4864 | -59.9308 | 2026-02-25 07:50:00 | GOES-19 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 47.4 |
| ff635202-07cb-39fc-87bc-1e95144efb51 | 1.4864 | -59.9498 | 2026-02-25 07:50:00 | GOES-19 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 47.3 |
| 6c6be9f0-5b1c-388d-82ac-5f48a9e74018 | 1.5046 | -59.9497 | 2026-02-25 07:50:00 | GOES-19 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 38.7 |
| 733de8d6-eeac-3927-b9bd-2af60e051504 | 1.5046 | -59.9306 | 2026-02-25 07:50:00 | GOES-19 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 40.7 |
| 57247f24-6843-3c1f-950e-2ab1948af563 | 1.5046 | -59.9497 | 2026-02-25 08:00:00 | GOES-19 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 67.6 |
| 1816aeb9-8e04-322f-945f-89110b1ad72b | 1.5046 | -59.9306 | 2026-02-25 08:00:00 | GOES-19 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 70.3 |
| 36121375-0934-3260-a4ef-e58f8caa2411 | 1.4864 | -59.9308 | 2026-02-25 08:00:00 | GOES-19 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 98.3 |
| 635371e2-25a7-3bf7-8252-020beb77bd7d | 1.4864 | -59.9498 | 2026-02-25 08:00:00 | GOES-19 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 89.9 |
| f503cb19-63a0-37f6-b069-5d9e436ef0cb | 1.4864 | -59.9308 | 2026-02-25 08:10:00 | GOES-19 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 77.4 |
| e14a3116-7277-3be3-a58b-ce8f501ee762 | 1.4864 | -59.9498 | 2026-02-25 08:10:00 | GOES-19 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 62.4 |
| 1314d8f5-5775-3014-81f7-40806381be40 | 1.5046 | -59.9497 | 2026-02-25 08:10:00 | GOES-19 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 52.4 |
| 67c6fa8a-d933-371e-8bd6-fb229f8a4b4f | 1.5046 | -59.9306 | 2026-02-25 08:10:00 | GOES-19 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 61.8 |
| 5085002c-a6c9-345e-987c-88a5f0908af6 | 1.5046 | -59.9497 | 2026-02-25 08:20:00 | GOES-19 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 47.8 |
| bec4783a-fba1-33c6-9afb-f650ad8904d3 | 1.4864 | -59.9308 | 2026-02-25 08:20:00 | GOES-19 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 61.0 |
| 6c87fdca-34c6-394e-90e4-b410581985a8 | 1.4864 | -59.9498 | 2026-02-25 08:20:00 | GOES-19 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 51.1 |
| efcee50f-6937-3228-aede-6b8751d661fd | 1.5046 | -59.9306 | 2026-02-25 08:20:00 | GOES-19 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 58.7 |
| bfcf07a3-1404-399f-99e0-54f5ebbed9c3 | 1.5046 | -59.9306 | 2026-02-25 10:20:00 | GOES-19 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 98.6 |
| 01d5ec36-03d5-3cc8-854b-594e812a7f74 | 1.5046 | -59.9497 | 2026-02-25 10:20:00 | GOES-19 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 109.2 |
| 898294e3-2bac-3ee8-967f-4dbbb506258c | 1.4864 | -59.9308 | 2026-02-25 10:20:00 | GOES-19 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 186.3 |
| 91fdc379-0995-32f5-896d-0c2c0a664c68 | 1.4864 | -59.9498 | 2026-02-25 10:20:00 | GOES-19 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 242.3 |
| 21ac1aee-92e0-36c7-ba9c-a2f2829c12d5 | 1.4681 | -59.95 | 2026-02-25 10:20:00 | GOES-19 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 85.9 |
| e595a529-6446-3cad-8b63-c79a5c9f26a7 | -6.37749 | -37.21095 | 2026-02-25 11:29:00 | TERRA_M-M | SÃO FERNANDO | RIO GRANDE DO NORTE | Brasil | 2411809 | 24 | 33 | nan | nan | nan | Caatinga | 8.8 |
| e1d468ef-3601-33f5-a028-5f2256806f3d | -6.37619 | -37.22028 | 2026-02-25 11:29:00 | TERRA_M-M | SÃO FERNANDO | RIO GRANDE DO NORTE | Brasil | 2411809 | 24 | 33 | nan | nan | nan | Caatinga | 4.5 |
| f0a844a6-5eec-3806-8298-d6d26099f50b | 1.4681 | -59.9309 | 2026-02-25 11:30:00 | GOES-19 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 222.8 |
| 754ba664-b6ff-3769-9fad-27f824ef3278 | 1.4864 | -59.9498 | 2026-02-25 11:30:00 | GOES-19 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1185.7 |
| e9c1db30-f9f7-3b29-b6a9-faf463f4c275 | 1.4863 | -59.9688 | 2026-02-25 11:30:00 | GOES-19 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 143.7 |
| 8f4f5526-3efc-3fc8-b971-118021d288b5 | 1.5046 | -59.9497 | 2026-02-25 11:30:00 | GOES-19 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 205.6 |


[Clique aqui para ver as próximas entradas](README10.md)
