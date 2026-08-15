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

## Dados Diários - Página 34

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 0cf47503-3596-37bc-a3cc-90445522070a | -13.84945 | -53.71017 | 2026-08-15 04:59:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 35f48b03-f684-30aa-a4d8-1171e7a6474a | -13.24737 | -54.17667 | 2026-08-15 04:59:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 5b1a2a5c-a41a-34ff-87e1-8ac3239bb173 | -14.09825 | -53.62574 | 2026-08-15 04:59:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 72eb7ddf-3558-36f5-afea-60887764fd6b | -11.48599 | -54.61307 | 2026-08-15 04:59:00 | NOAA-21 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 53925d2d-a54b-36ef-89b3-bff838e3cecc | -13.75703 | -53.43061 | 2026-08-15 04:59:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 27c8d795-2bfa-3654-883e-53a758f0b94c | -11.58936 | -54.66981 | 2026-08-15 04:59:00 | NOAA-21 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 4bcc66b2-3da3-3ee5-9a09-ba3e12e1ac22 | -14.44116 | -51.91137 | 2026-08-15 04:59:00 | NOAA-21 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 19.5 |
| af49e808-b600-3761-a22f-0adc38b215f6 | -6.6194 | -59.0609 | 2026-08-15 05:00:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 52.2 |
| f9807253-3e1e-3caf-a5cf-ebd2e934a05c | -14.4499 | -51.9004 | 2026-08-15 05:00:00 | GOES-19 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 176.6 |
| 42543f74-0543-3343-9061-0994ac439736 | -11.4187 | -46.328 | 2026-08-15 05:00:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 94.0 |
| 0613701d-81b8-3bd6-9b9c-0be68673e2ec | -14.4306 | -51.9029 | 2026-08-15 05:00:00 | GOES-19 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 202.3 |
| cf1283e2-a405-3848-9c4d-8c620021ad3e | -14.4495 | -51.9217 | 2026-08-15 05:00:00 | GOES-19 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 93.1 |
| cdf16e7b-2619-394f-99c8-65bdd209c3c9 | -6.9334 | -43.6333 | 2026-08-15 05:00:00 | GOES-19 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 52.8 |
| fd451ce6-84c1-3596-977a-57d29df0219d | -11.4184 | -46.3506 | 2026-08-15 05:00:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 365.3 |
| 8167fc12-65de-38c0-91d3-409633cc2c1f | -14.4112 | -51.9055 | 2026-08-15 05:00:00 | GOES-19 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 48.5 |
| 15b29d0f-061c-326f-9528-6f393186840e | -11.418 | -46.3733 | 2026-08-15 05:00:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 65.0 |
| 4fd9c347-6851-39f3-a024-d532dbc594b2 | -14.4302 | -51.9243 | 2026-08-15 05:00:00 | GOES-19 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 116.0 |
| cf21ee9d-9adb-345b-bfa6-8adb1b682560 | -11.4375 | -46.348 | 2026-08-15 05:00:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 142.4 |
| 4c371168-cc68-39a8-8220-0f349a9f377f | -14.74151 | -56.35077 | 2026-08-15 05:01:00 | NOAA-21 | NOBRES | MATO GROSSO | Brasil | 5105903 | 51 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 78111760-c145-30ba-9a0f-34b7aad8be0b | -17.90639 | -44.44583 | 2026-08-15 05:01:00 | NOAA-21 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 1.9 |
| dcdfbdd0-b6c5-3194-bf94-363bb6df3adf | -16.89487 | -54.14911 | 2026-08-15 05:01:00 | NOAA-21 | PEDRA PRETA | MATO GROSSO | Brasil | 5106372 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 5ab975c1-ca98-307e-9cc5-0fbf1e52b62e | -22.3469 | -48.49334 | 2026-08-15 05:01:00 | NOAA-21 | JAÚ | SÃO PAULO | Brasil | 3525300 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| b853af0e-16d2-370b-821f-2a5ec6b28b7e | -15.16162 | -52.83301 | 2026-08-15 05:01:00 | NOAA-21 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 6f1423f4-fa69-301e-82a6-70508f1c47ca | -21.46862 | -48.61567 | 2026-08-15 05:01:00 | NOAA-21 | TAQUARITINGA | SÃO PAULO | Brasil | 3553708 | 35 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 0b6720ae-c487-3a1b-94ab-59e68a1758b7 | -21.46895 | -48.61244 | 2026-08-15 05:01:00 | NOAA-21 | TAQUARITINGA | SÃO PAULO | Brasil | 3553708 | 35 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 2708c616-4dd4-3011-a2fb-812a57606913 | -22.34714 | -48.49535 | 2026-08-15 05:01:00 | NOAA-21 | JAÚ | SÃO PAULO | Brasil | 3525300 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 9aac936c-8fd9-360c-b561-80f26aa6a1d9 | -16.10968 | -49.85984 | 2026-08-15 05:01:00 | NOAA-21 | ITABERAÍ | GOIÁS | Brasil | 5210406 | 52 | 33 | nan | nan | nan | Cerrado | 9.0 |
| f2c05b19-fdcb-3e32-804c-856137914a3c | -16.8885 | -54.16858 | 2026-08-15 05:01:00 | NOAA-21 | PEDRA PRETA | MATO GROSSO | Brasil | 5106372 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| fb9c0468-249d-3d88-b152-60389fd8f806 | -15.52745 | -52.99275 | 2026-08-15 05:01:00 | NOAA-21 | GENERAL CARNEIRO | MATO GROSSO | Brasil | 5103908 | 51 | 33 | nan | nan | nan | Cerrado | 2.3 |
| c6d901fb-451f-34e0-b921-96dee71a0ff1 | -16.87793 | -54.14243 | 2026-08-15 05:01:00 | NOAA-21 | PEDRA PRETA | MATO GROSSO | Brasil | 5106372 | 51 | 33 | nan | nan | nan | Cerrado | 2.9 |
| c7db159e-9654-3a9b-9ac2-0cc2c095789d | -16.87501 | -54.13785 | 2026-08-15 05:01:00 | NOAA-21 | PEDRA PRETA | MATO GROSSO | Brasil | 5106372 | 51 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 942ae3f4-d68c-3c5f-ab60-f88e7225b534 | -20.33368 | -46.73978 | 2026-08-15 05:01:00 | NOAA-21 | DELFINÓPOLIS | MINAS GERAIS | Brasil | 3121209 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 30217442-8a36-38d6-930f-9b8dc548667c | -22.68161 | -47.55292 | 2026-08-15 05:01:00 | NOAA-21 | PIRACICABA | SÃO PAULO | Brasil | 3538709 | 35 | 33 | nan | nan | nan | Mata Atlântica | 9.3 |
| 523c42fa-eda8-33f2-ada7-29a615972a6c | -16.95703 | -51.74476 | 2026-08-15 05:01:00 | NOAA-21 | CAIAPÔNIA | GOIÁS | Brasil | 5204409 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| e1647d7e-dea8-3057-b596-245622e5df6c | -15.41198 | -56.73645 | 2026-08-15 05:01:00 | NOAA-21 | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 9aa08880-9288-3bff-b29c-126f13361455 | -20.02208 | -43.89661 | 2026-08-15 05:01:00 | NOAA-21 | NOVA LIMA | MINAS GERAIS | Brasil | 3144805 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| 6c769af5-9f6c-36a0-bb6b-04fb15b02457 | -15.50983 | -52.98577 | 2026-08-15 05:01:00 | NOAA-21 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 0.6 |
| e64b4c7b-25b6-3b4c-8d5e-dd6d89a35529 | -16.25413 | -53.70236 | 2026-08-15 05:01:00 | NOAA-21 | GUIRATINGA | MATO GROSSO | Brasil | 5104203 | 51 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 0f77a89a-694c-39ed-8263-110a72c619df | -15.60028 | -56.16323 | 2026-08-15 05:01:00 | NOAA-21 | VÁRZEA GRANDE | MATO GROSSO | Brasil | 5108402 | 51 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 0070b22b-0eff-34b7-844b-650e6fe97ccc | -15.22163 | -52.72325 | 2026-08-15 05:01:00 | NOAA-21 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 0.8 |
| abaf4098-600d-3f71-8346-64aadde03c69 | -16.11353 | -49.86506 | 2026-08-15 05:01:00 | NOAA-21 | ITABERAÍ | GOIÁS | Brasil | 5210406 | 52 | 33 | nan | nan | nan | Cerrado | 9.0 |
| 7c668768-ef10-3b61-ab3f-e6ff8ba2a231 | -16.19499 | -45.26894 | 2026-08-15 05:01:00 | NOAA-21 | PINTÓPOLIS | MINAS GERAIS | Brasil | 3150570 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| e6ea137e-6a94-3143-8e99-a7ca58db09db | -16.89835 | -54.14975 | 2026-08-15 05:01:00 | NOAA-21 | PEDRA PRETA | MATO GROSSO | Brasil | 5106372 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 703bc268-7989-3f26-a6a2-5cd13fd3c11f | -16.89544 | -54.14513 | 2026-08-15 05:01:00 | NOAA-21 | PEDRA PRETA | MATO GROSSO | Brasil | 5106372 | 51 | 33 | nan | nan | nan | Cerrado | 6.1 |
| 91158d0e-9b36-322c-a9a9-2ba932bc6e84 | -14.75531 | -56.3494 | 2026-08-15 05:01:00 | NOAA-21 | NOBRES | MATO GROSSO | Brasil | 5105903 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 987c2021-b67d-3951-9146-736cab614154 | -20.33862 | -46.74926 | 2026-08-15 05:01:00 | NOAA-21 | DELFINÓPOLIS | MINAS GERAIS | Brasil | 3121209 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 2f9257ee-d055-398e-ab3e-deb0c3a4a7f0 | -21.46264 | -48.67427 | 2026-08-15 05:01:00 | NOAA-21 | TAQUARITINGA | SÃO PAULO | Brasil | 3553708 | 35 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 16d612b9-d9b3-3be8-916d-142e69a41b39 | -22.34156 | -48.49781 | 2026-08-15 05:01:00 | NOAA-21 | JAÚ | SÃO PAULO | Brasil | 3525300 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.9 |
| 86932bf4-fb8c-3760-aa1c-8b498e7b1e19 | -16.25491 | -53.69984 | 2026-08-15 05:01:00 | NOAA-21 | GUIRATINGA | MATO GROSSO | Brasil | 5104203 | 51 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 1efac787-9ec7-30e2-b45b-1f78fb335e19 | -15.52381 | -52.99219 | 2026-08-15 05:01:00 | NOAA-21 | GENERAL CARNEIRO | MATO GROSSO | Brasil | 5103908 | 51 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 0e1c001d-5b17-3ab1-87fc-e62bfc5467d5 | -18.1656 | -47.99219 | 2026-08-15 05:01:00 | NOAA-21 | CATALÃO | GOIÁS | Brasil | 5205109 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 605ff09a-4471-3408-91a7-8691141f8ea3 | -14.75475 | -56.35295 | 2026-08-15 05:01:00 | NOAA-21 | NOBRES | MATO GROSSO | Brasil | 5105903 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| f250f556-7f64-36d9-afbd-815a597204ec | -14.752 | -56.34885 | 2026-08-15 05:01:00 | NOAA-21 | NOBRES | MATO GROSSO | Brasil | 5105903 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| b586b6aa-4b39-3ffc-b9b1-a761e6d02ae2 | -18.54889 | -48.2003 | 2026-08-15 05:01:00 | NOAA-21 | ARAGUARI | MINAS GERAIS | Brasil | 3103504 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 5f5f6af8-3bb0-3b21-8e88-bb5892a606d9 | -16.90364 | -54.16279 | 2026-08-15 05:01:00 | NOAA-21 | PEDRA PRETA | MATO GROSSO | Brasil | 5106372 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| cc35fe64-06e3-3c0e-bf0f-8eaba99f7194 | -22.67596 | -47.55261 | 2026-08-15 05:01:00 | NOAA-21 | PIRACICABA | SÃO PAULO | Brasil | 3538709 | 35 | 33 | nan | nan | nan | Mata Atlântica | 9.3 |
| 77389cee-e179-3241-ba4e-b5cf1909df10 | -16.9042 | -54.15889 | 2026-08-15 05:01:00 | NOAA-21 | PEDRA PRETA | MATO GROSSO | Brasil | 5106372 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 06be5e1a-774e-3f52-a4fd-8bee4c612bcc | -14.74813 | -56.35186 | 2026-08-15 05:01:00 | NOAA-21 | NOBRES | MATO GROSSO | Brasil | 5105903 | 51 | 33 | nan | nan | nan | Cerrado | 0.8 |
| cf65e103-ec9e-3255-a398-050286ba2522 | -22.3419 | -48.49437 | 2026-08-15 05:01:00 | NOAA-21 | JAÚ | SÃO PAULO | Brasil | 3525300 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.9 |
| b5456ee9-f46a-3b6b-af12-6c415826b0c6 | -16.89842 | -54.17422 | 2026-08-15 05:01:00 | NOAA-21 | PEDRA PRETA | MATO GROSSO | Brasil | 5106372 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 89f4ccad-af1e-352c-9dfe-77c7fb86aa47 | -16.88086 | -54.14698 | 2026-08-15 05:01:00 | NOAA-21 | PEDRA PRETA | MATO GROSSO | Brasil | 5106372 | 51 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 6b23c85f-1083-3a52-bf14-44e646df4247 | -16.19698 | -45.26981 | 2026-08-15 05:01:00 | NOAA-21 | PINTÓPOLIS | MINAS GERAIS | Brasil | 3150570 | 31 | 33 | nan | nan | nan | Cerrado | 2.6 |
| ed8716a7-6fb8-3f0c-bf92-a09166957b2d | -18.54613 | -48.20095 | 2026-08-15 05:01:00 | NOAA-21 | ARAGUARI | MINAS GERAIS | Brasil | 3103504 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 29847a1b-cd17-3994-8b33-406506b09814 | -14.73433 | -56.35323 | 2026-08-15 05:01:00 | NOAA-21 | NOBRES | MATO GROSSO | Brasil | 5105903 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 1e8d7761-22ae-31ff-8528-bccfbb624a69 | -15.21795 | -52.72271 | 2026-08-15 05:01:00 | NOAA-21 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 0.8 |
| cca90de9-fe9d-32a7-934c-cc21b9e18cfe | -16.95913 | -51.74706 | 2026-08-15 05:01:00 | NOAA-21 | CAIAPÔNIA | GOIÁS | Brasil | 5204409 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| b81ec782-177f-39b1-932f-269a3d1b02be | -20.0199 | -43.89859 | 2026-08-15 05:01:00 | NOAA-21 | NOVA LIMA | MINAS GERAIS | Brasil | 3144805 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| 21a98d8c-6c63-3087-9f7e-55d1cac07710 | -18.90642 | -54.82998 | 2026-08-15 05:01:00 | NOAA-21 | RIO VERDE DE MATO GROSSO | MATO GROSSO DO SUL | Brasil | 5007406 | 50 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 756cc000-6aef-39f9-b2a7-1502d20e4cf7 | -16.87737 | -54.14638 | 2026-08-15 05:01:00 | NOAA-21 | PEDRA PRETA | MATO GROSSO | Brasil | 5106372 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| b3514011-572e-3bed-9ffe-15a38b5588a6 | -22.34657 | -48.49686 | 2026-08-15 05:01:00 | NOAA-21 | JAÚ | SÃO PAULO | Brasil | 3525300 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 5b4b2771-feec-340c-9472-933cd494488d | -14.7382 | -56.35022 | 2026-08-15 05:01:00 | NOAA-21 | NOBRES | MATO GROSSO | Brasil | 5105903 | 51 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 6baa24c7-42b8-3c1f-afc7-75825eac5bdd | -16.10524 | -49.85917 | 2026-08-15 05:01:00 | NOAA-21 | ITABERAÍ | GOIÁS | Brasil | 5210406 | 52 | 33 | nan | nan | nan | Cerrado | 3.1 |
| d0cd8812-7da9-3420-8733-9facc76d44bb | -14.5444 | -59.7611 | 2026-08-15 05:01:00 | NOAA-21 | NOVA LACERDA | MATO GROSSO | Brasil | 5106182 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| bc70ebfb-af1c-3ed8-9335-38f51b168211 | -16.10081 | -49.85851 | 2026-08-15 05:01:00 | NOAA-21 | ITABERAÍ | GOIÁS | Brasil | 5210406 | 52 | 33 | nan | nan | nan | Cerrado | 3.1 |
| f5e47ed1-dc93-30a4-9366-63d538f2b8d0 | -22.3475 | -48.49172 | 2026-08-15 05:01:00 | NOAA-21 | JAÚ | SÃO PAULO | Brasil | 3525300 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 5620a05f-0a0c-3a10-883b-5e9ee07716d7 | -22.34627 | -48.50017 | 2026-08-15 05:01:00 | NOAA-21 | JAÚ | SÃO PAULO | Brasil | 3525300 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 07da7b68-dc91-3c72-a4ef-82cef4c97d32 | -22.67631 | -47.54858 | 2026-08-15 05:01:00 | NOAA-21 | PIRACICABA | SÃO PAULO | Brasil | 3538709 | 35 | 33 | nan | nan | nan | Mata Atlântica | 8.5 |
| 3d5ba8f5-88e8-3a84-ab37-fd8187723a94 | -15.16832 | -52.83842 | 2026-08-15 05:01:00 | NOAA-21 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 80434902-07f2-366c-a7c7-a683ed91594d | -15.29437 | -53.18964 | 2026-08-15 05:01:00 | NOAA-21 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 060a8342-f394-377c-aea7-a1eb4a660e79 | -15.51713 | -52.98679 | 2026-08-15 05:01:00 | NOAA-21 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 5018bfef-43b1-3fbf-849d-c65f3cdac310 | -17.90038 | -44.44029 | 2026-08-15 05:01:00 | NOAA-21 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 3.0 |
| e84e720f-cac3-35ec-bb6a-c897aefd6007 | -18.00448 | -49.40224 | 2026-08-15 05:01:00 | NOAA-21 | GOIATUBA | GOIÁS | Brasil | 5209101 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 23f44702-16cf-3f4e-abf2-3a6ed079f2c2 | -16.88436 | -54.14755 | 2026-08-15 05:01:00 | NOAA-21 | PEDRA PRETA | MATO GROSSO | Brasil | 5106372 | 51 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 72be1831-cbeb-3158-9789-700e3206e2f8 | -16.18572 | -55.95769 | 2026-08-15 05:01:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 3.0 |
| 4c31b704-512e-361d-bcc4-d81c941089b1 | -16.19181 | -55.96237 | 2026-08-15 05:01:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.2 |
| 6c7d9ea1-3f9b-3969-99f5-ae50a8562686 | -23.01571 | -50.42599 | 2026-08-15 05:01:00 | NOAA-21 | ITAMBARACÁ | PARANÁ | Brasil | 4111001 | 41 | 33 | nan | nan | nan | Mata Atlântica | 2.5 |
| a53ac61e-f9b9-3729-a043-a9653441ae6b | -22.3468 | -48.49873 | 2026-08-15 05:01:00 | NOAA-21 | JAÚ | SÃO PAULO | Brasil | 3525300 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 9db7f836-934c-3654-a870-3416661c7cd3 | -16.89137 | -54.1486 | 2026-08-15 05:01:00 | NOAA-21 | PEDRA PRETA | MATO GROSSO | Brasil | 5106372 | 51 | 33 | nan | nan | nan | Cerrado | 6.4 |
| 52838b09-c057-3621-8a76-3b3fc5db11d2 | -15.475 | -52.88769 | 2026-08-15 05:01:00 | NOAA-21 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 0.6 |
| df1462da-2ba4-359f-a2f9-65a91aaa675c | -16.3371 | -55.38174 | 2026-08-15 05:01:00 | NOAA-21 | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 52763bd2-28a0-3096-aa94-29583a6b203e | -16.88501 | -54.16802 | 2026-08-15 05:01:00 | NOAA-21 | PEDRA PRETA | MATO GROSSO | Brasil | 5106372 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 31be382d-fa42-3842-b12b-737cbba66857 | -15.2347 | -56.47971 | 2026-08-15 05:01:00 | NOAA-21 | JANGADA | MATO GROSSO | Brasil | 5104906 | 51 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 04ea95ac-d8ea-34d1-8a2c-3c6c45c61447 | -22.68196 | -47.54886 | 2026-08-15 05:01:00 | NOAA-21 | PIRACICABA | SÃO PAULO | Brasil | 3538709 | 35 | 33 | nan | nan | nan | Mata Atlântica | 8.5 |
| d00a6966-9e22-3b08-91c5-766ae9b1597f | -16.11665 | -49.86733 | 2026-08-15 05:01:00 | NOAA-21 | ITABERAÍ | GOIÁS | Brasil | 5210406 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 4c7e5c84-28ba-3015-9ba0-24c032c7b813 | -15.52501 | -53.01019 | 2026-08-15 05:01:00 | NOAA-21 | GENERAL CARNEIRO | MATO GROSSO | Brasil | 5103908 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 33a2f159-b438-3502-83c3-ff1873493928 | -22.34225 | -48.49081 | 2026-08-15 05:01:00 | NOAA-21 | JAÚ | SÃO PAULO | Brasil | 3525300 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.8 |
| e534a438-9ff1-3976-8733-23a8773a683d | -15.21427 | -52.72218 | 2026-08-15 05:01:00 | NOAA-21 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 2.2 |
| a46b4438-9967-3402-9516-86cbc85f7a65 | -16.87444 | -54.1418 | 2026-08-15 05:01:00 | NOAA-21 | PEDRA PRETA | MATO GROSSO | Brasil | 5106372 | 51 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 9a91e81b-468e-3d8e-9a80-25bbcd436e59 | -16.20102 | -45.26953 | 2026-08-15 05:01:00 | NOAA-21 | PINTÓPOLIS | MINAS GERAIS | Brasil | 3150570 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 310d0b28-da4a-38d9-8f46-c7c7a66ee74d | -16.25768 | -53.70288 | 2026-08-15 05:01:00 | NOAA-21 | GUIRATINGA | MATO GROSSO | Brasil | 5104203 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |


[Clique aqui para ver as próximas entradas](README35.md)
