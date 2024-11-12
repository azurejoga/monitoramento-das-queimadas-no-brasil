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

## Dados Diários - Página 6

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 7a64a5d3-3a58-3833-8403-3612773fa443 | -17.639 | -57.409599 | 2024-11-12 01:13:00 | METOP-B | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| d5aa3ed0-8232-3398-8626-170fd8e99b3e | -17.635099 | -57.531601 | 2024-11-12 01:13:00 | METOP-B | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 2e8e0a31-87e5-30bf-a63c-e1a30c146c09 | -23.949499 | -54.035702 | 2024-11-12 01:13:00 | METOP-B | ALTÔNIA | PARANÁ | Brasil | 4100509 | 41 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 923cdf95-bc9b-3d92-91a7-520faddbba85 | 1.0518 | -60.589802 | 2024-11-12 01:13:00 | METOP-B | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | nan |
| b2acb094-a38d-3952-81dd-6886004fd426 | -12.2879 | -57.7323 | 2024-11-12 01:13:00 | METOP-B | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| f6adec50-e7d3-342e-aeb5-edb6b22c5f3f | -17.615801 | -57.490799 | 2024-11-12 01:13:00 | METOP-B | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 6c3abf52-9553-30f8-b2e7-f2deea42127c | -17.606501 | -57.402199 | 2024-11-12 01:13:00 | METOP-B | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 84d32685-d516-3679-93b6-bfa958f759a0 | -19.626699 | -54.139999 | 2024-11-12 01:13:00 | METOP-B | CAMAPUÃ | MATO GROSSO DO SUL | Brasil | 5002605 | 50 | 33 | nan | nan | nan | Cerrado | nan |
| d3b1ef28-aad1-328a-b760-9244313fac9b | -17.607599 | -57.500301 | 2024-11-12 01:13:00 | METOP-B | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 3dd72091-25bc-3090-8299-a42072828b17 | -17.605801 | -57.538601 | 2024-11-12 01:13:00 | METOP-B | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| d8328a15-5964-3a3e-a5d8-7c4ec3b148bc | -17.5996 | -57.464401 | 2024-11-12 01:13:00 | METOP-B | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| a09774a5-9570-3a33-852c-81fb0e29a183 | -17.650299 | -57.414299 | 2024-11-12 01:13:00 | METOP-B | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 52bb45a1-d009-3cc3-9c42-0048d061cdb3 | 1.0502 | -60.596901 | 2024-11-12 01:13:00 | METOP-B | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | nan |
| 3106dd55-ed9d-3dc8-b30b-b2e2ec995332 | -17.2526 | -57.479401 | 2024-11-12 01:13:00 | METOP-B | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 879ac163-1b5a-3b7c-ab36-c2ee51a158d3 | -17.6422 | -57.423901 | 2024-11-12 01:13:00 | METOP-B | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 562af450-a6b3-39b5-b596-5935c312f81b | -20.3137 | -48.8125 | 2024-11-12 01:13:00 | METOP-B | COLÔMBIA | SÃO PAULO | Brasil | 3512100 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| 433390d2-c166-3f78-ba1a-6a6fbd761155 | -17.6563 | -57.534 | 2024-11-12 01:13:00 | METOP-B | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| f9743e5a-6cf0-30c0-9683-60699f769420 | -17.6535 | -57.428699 | 2024-11-12 01:13:00 | METOP-B | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| c82d2292-d867-3d61-b873-cde4ea9a5574 | -17.7201 | -57.496101 | 2024-11-12 01:13:00 | METOP-B | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| cb599872-1521-3bcc-b871-e22d03b2e3b8 | -17.2722 | -57.4748 | 2024-11-12 01:13:00 | METOP-B | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| b69e54c0-1091-3f8e-9c80-24732d9a4de4 | -17.633499 | -57.524399 | 2024-11-12 01:13:00 | METOP-B | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 1b3aa882-1b9f-32df-a7e0-5dfe431e84c1 | -17.643801 | -57.431099 | 2024-11-12 01:13:00 | METOP-B | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 3ad537fd-2368-3aa1-9253-8435552053ce | -17.7103 | -57.498501 | 2024-11-12 01:13:00 | METOP-B | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 60037e36-ec94-3d4e-b5f3-088193d3a743 | -17.5998 | -57.4189 | 2024-11-12 01:13:00 | METOP-B | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 3b7236f2-5e8a-3670-81be-24569af3b615 | -17.608 | -57.409401 | 2024-11-12 01:13:00 | METOP-B | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 82520b0f-10d8-35ec-8976-a4a918b31886 | -3.1097 | -54.2865 | 2024-11-12 01:20:00 | GOES-16 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 87.3 |
| 9e1c682b-794a-300f-a9f3-9829d79ab6af | -2.7773 | -49.3279 | 2024-11-12 01:20:00 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 54.2 |
| 3661a439-a659-3541-b2eb-5b9e50c4ec2b | 1.048 | -60.5986 | 2024-11-12 01:20:00 | GOES-16 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 70.6 |
| fa63e735-93f2-34cf-88a9-9861adad9225 | -17.274 | -57.4675 | 2024-11-12 01:20:00 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 53.1 |
| 2baa8797-f7f8-39d0-83d4-338792791da9 | -2.9913 | -51.3356 | 2024-11-12 01:20:00 | GOES-16 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 84.5 |
| 86d83e41-2219-32c3-9c15-f76653e06eae | -2.7588 | -49.3285 | 2024-11-12 01:20:00 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 92.2 |
| ff1bc8b5-c825-3557-9a1a-6d1ce231718c | 1.0663 | -60.5985 | 2024-11-12 01:20:00 | GOES-16 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 63.1 |
| 56e28463-22e6-3b4e-b29a-e5e3d9e21e87 | -17.2936 | -57.4652 | 2024-11-12 01:20:00 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 55.3 |
| b42d34b6-e06d-3533-a5b5-899ccebdd6fb | -2.9912 | -51.3563 | 2024-11-12 01:20:00 | GOES-16 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 57.2 |
| 91ae264c-f185-35c0-a1bc-6da868b4376e | -17.254 | -57.4903 | 2024-11-12 01:20:00 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 52.4 |
| 3f330301-a34b-3ca4-82a7-14a636b7c16f | -2.7587 | -49.3497 | 2024-11-12 01:20:00 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 83.6 |
| 333d7637-7291-3a48-bb9b-86de14305bc2 | -2.7737 | -50.3201 | 2024-11-12 01:20:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 72.1 |
| 856bf71f-43d7-366b-a138-f11141ec4157 | -17.2737 | -57.488 | 2024-11-12 01:20:00 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 73.0 |
| 48e1332c-138d-3bd0-a1eb-9c65fa9ed216 | -2.7737 | -50.2992 | 2024-11-12 01:20:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 147.8 |
| 80c1deab-21a7-33b3-af35-52f08b46b1e2 | -2.7922 | -50.2986 | 2024-11-12 01:20:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 91.2 |
| 00c89e72-083e-3bf7-b4d9-112918e4e5a8 | -3.1096 | -54.3066 | 2024-11-12 01:20:00 | GOES-16 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 86.0 |
| af985429-df7a-3dbd-aba7-a532937419b3 | -17.2933 | -57.4857 | 2024-11-12 01:20:00 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 71.5 |
| 156f12ad-be07-3fe5-bfc7-91a9a392039e | -2.7772 | -49.3492 | 2024-11-12 01:30:00 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 53.4 |
| fdcbdd5e-bfdb-3aed-b5ab-2a88fe7e528f | -17.6283 | -57.4252 | 2024-11-12 01:30:00 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 56.5 |
| 3b1c0357-c1cb-31bd-8285-9c8f25b34f12 | -17.2933 | -57.4857 | 2024-11-12 01:30:00 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 78.1 |
| 30805c4f-13bd-3fe5-b4d3-b38716d6acae | -17.648 | -57.4229 | 2024-11-12 01:30:00 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 68.2 |
| 64807e5a-66ec-33be-9739-af528b2f23c6 | -17.2737 | -57.488 | 2024-11-12 01:30:00 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 82.3 |
| 8742f89e-e844-3427-bd41-4b1b127d3b41 | -2.9913 | -51.3356 | 2024-11-12 01:30:00 | GOES-16 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 67.6 |
| 35429aee-b245-30d6-9b56-e8d9f2a6ecb3 | 1.0663 | -60.5985 | 2024-11-12 01:30:00 | GOES-16 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 63.7 |
| dd08a83a-1742-330f-9a7c-8b8926f20a62 | -2.9912 | -51.3563 | 2024-11-12 01:30:00 | GOES-16 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 54.1 |
| effc92c7-5e7f-3359-99aa-e76e212870ae | -2.7773 | -49.3279 | 2024-11-12 01:30:00 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 55.0 |
| c810c71e-7119-3752-82bb-84ac4b2617b5 | -17.2936 | -57.4652 | 2024-11-12 01:30:00 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 62.9 |
| 88f7bba4-5c25-31db-874e-a4c17bdbe83c | -3.1097 | -54.2865 | 2024-11-12 01:30:00 | GOES-16 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 50.5 |
| 81cd0a02-1abe-358b-a306-e641be246617 | -17.6477 | -57.4434 | 2024-11-12 01:30:00 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 58.1 |
| 764d2306-92ab-3d86-ab3b-b7b1ea1b7423 | 1.048 | -60.5986 | 2024-11-12 01:30:00 | GOES-16 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 63.3 |
| 2f1ad555-336c-3015-98dc-84bc47f41269 | -17.254 | -57.4903 | 2024-11-12 01:30:00 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 52.5 |
| 58e2a514-d6ac-3046-91cc-05b30e1adc17 | -2.7922 | -50.2986 | 2024-11-12 01:30:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 56.5 |
| 681b74ac-824b-3efc-9d04-fae75591ea2e | -2.7587 | -49.3497 | 2024-11-12 01:30:00 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 128.2 |
| c966fe69-dcc0-3082-a84a-cbcbba2266db | -17.274 | -57.4675 | 2024-11-12 01:30:00 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 57.8 |
| 14c53832-a83f-333a-b9e7-5380c98d301e | -2.7588 | -49.3285 | 2024-11-12 01:30:00 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 123.3 |
| 16710bb5-4e83-3905-96ce-191a3c40d795 | -2.7773 | -49.3279 | 2024-11-12 01:40:00 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 61.7 |
| 478e5c8c-b4c5-3866-951f-d5104d93f184 | -2.7402 | -49.3502 | 2024-11-12 01:40:00 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 59.6 |
| 33e0f39c-39ce-30fe-b377-2cd69670c526 | -17.274 | -57.4675 | 2024-11-12 01:40:00 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 58.8 |
| 739f07f7-e4bb-308f-8d80-a8d48c274c6c | -17.2936 | -57.4652 | 2024-11-12 01:40:00 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 72.3 |
| bfba69d5-e0a9-3160-ad09-93e1da1be41b | 1.048 | -60.5986 | 2024-11-12 01:40:00 | GOES-16 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 58.3 |
| 48600ee4-3374-338c-8dec-3c3d61060574 | -17.2933 | -57.4857 | 2024-11-12 01:40:00 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 88.2 |
| fff9bd5d-f283-32ad-8b8b-a5ce4e18e575 | -2.7871 | -51.7544 | 2024-11-12 01:40:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 68.3 |
| 9ebf6ebf-1c60-3305-bf6f-1c35d71ae44c | -17.254 | -57.4903 | 2024-11-12 01:40:00 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 53.2 |
| bf9f5ae8-e65c-304a-b9ea-c1dc72bfa844 | 1.0663 | -60.5985 | 2024-11-12 01:40:00 | GOES-16 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 52.9 |
| 380685fa-89da-33f0-892a-00a705eebd65 | -2.7737 | -50.2992 | 2024-11-12 01:40:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 70.5 |
| 9c73e590-300d-3bd4-8f59-105efb65cec5 | -4.8032 | -45.282 | 2024-11-12 01:40:00 | GOES-16 | LAGO DA PEDRA | MARANHÃO | Brasil | 2105708 | 21 | 33 | nan | nan | nan | Cerrado | 72.4 |
| fe18aeda-95c3-3456-8455-d783564aff40 | -2.7772 | -49.3492 | 2024-11-12 01:40:00 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 63.6 |
| 584b9ff4-65de-39db-b8c8-6938d5d111e3 | -2.7587 | -49.3497 | 2024-11-12 01:40:00 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 132.7 |
| a3c1f09b-c5ee-3c42-bb25-9abac258c90b | -2.7588 | -49.3285 | 2024-11-12 01:40:00 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 109.4 |
| a248d698-127b-32c2-abb1-63e9fc0700e3 | -17.2737 | -57.488 | 2024-11-12 01:40:00 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 83.6 |
| ce75143d-c720-3656-9d6a-8faf203511d1 | -17.648 | -57.4229 | 2024-11-12 01:40:00 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 50.7 |
| 36caef07-b968-3865-a1a4-18f6256a5c6a | -2.9913 | -51.3356 | 2024-11-12 01:50:00 | GOES-16 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 60.3 |
| 6167e156-e245-3f88-abc6-fab5ab404e80 | -17.2737 | -57.488 | 2024-11-12 01:50:00 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 66.4 |
| 1cbc7f90-4941-3d15-8130-9fa25149fa97 | -17.6066 | -57.551 | 2024-11-12 01:50:00 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 48.7 |
| e8ddaa60-dc97-36b9-a20a-b159e71243d3 | -17.6073 | -57.5099 | 2024-11-12 01:50:00 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 51.5 |
| 7be58dd1-fece-3e22-8086-362d0619ca32 | -17.2933 | -57.4857 | 2024-11-12 01:50:00 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 72.2 |
| 4284daac-70f1-36aa-9699-57db4f6c845b | -2.7587 | -49.3497 | 2024-11-12 01:50:00 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 90.9 |
| cddcaa1b-66c6-3eeb-b83f-ce2baba91dcc | -3.1096 | -54.3066 | 2024-11-12 01:50:00 | GOES-16 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 50.0 |
| 620c3e9b-df83-3f1b-b8df-86130eba70af | -17.2936 | -57.4652 | 2024-11-12 01:50:00 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 58.4 |
| b38dcac5-5679-38b1-9b47-ee778df4aeb8 | -17.5875 | -57.5122 | 2024-11-12 01:50:00 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 49.0 |
| e39a87e2-4f7b-3773-8fbc-9e14aad7c297 | 1.0663 | -60.5985 | 2024-11-12 01:50:00 | GOES-16 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 64.3 |
| 937cbbdd-5336-335d-ba46-7b40d2458022 | -17.6069 | -57.5304 | 2024-11-12 01:50:00 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 61.5 |
| d801726a-1a63-3b80-a1c1-3b0f9a47407d | -2.7922 | -50.2986 | 2024-11-12 01:50:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 92.8 |
| e08948fd-f414-32e8-b106-954997e5b114 | -3.1097 | -54.2865 | 2024-11-12 01:50:00 | GOES-16 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 48.2 |
| 9972c27d-2d7b-3e6f-961a-811a532f5cd1 | -17.274 | -57.4675 | 2024-11-12 01:50:00 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 52.5 |
| a64ddb4d-daab-3a29-b79c-d423c4163b5d | -2.7588 | -49.3285 | 2024-11-12 01:50:00 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 90.4 |
| 85e55a7c-cb4c-3793-bbaa-ed5ee7c78940 | -2.7871 | -51.7544 | 2024-11-12 01:50:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 74.3 |
| 76e5a04a-d557-3b78-9987-3129d8ee173c | 1.048 | -60.5986 | 2024-11-12 01:50:00 | GOES-16 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 55.3 |
| e083854b-7a73-3f89-921d-6f0a5ee7f48c | -2.7737 | -50.2992 | 2024-11-12 01:50:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 79.4 |
| c51ed370-e15c-3a60-b438-82182883d2f6 | -3.0913 | -54.287 | 2024-11-12 02:00:00 | GOES-16 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 57.4 |
| 50c03b4a-0e2a-35f8-8378-c6162f5cd184 | -3.1097 | -54.2865 | 2024-11-12 02:00:00 | GOES-16 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 91.7 |
| 019d4247-8b1d-36c3-bc31-7919d086a27b | -2.7588 | -49.3285 | 2024-11-12 02:00:00 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 106.1 |
| f8daca97-6d4c-327d-ac04-bf9c1aa87ea4 | -3.0689 | -50.3326 | 2024-11-12 02:00:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 55.5 |
| 635e2589-c0f0-3a1f-9a77-24f106759af5 | 1.0663 | -60.5985 | 2024-11-12 02:00:00 | GOES-16 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 61.4 |
| 87a40b21-a750-341c-8eb1-3e5637739206 | -17.2936 | -57.4652 | 2024-11-12 02:00:00 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 62.0 |


[Clique aqui para ver as próximas entradas](README7.md)
