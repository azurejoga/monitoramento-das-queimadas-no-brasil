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

## Dados Diários - Página 33

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 418e85c7-25a1-3cf6-87b1-db2a51f1599d | -15.70297 | -48.32125 | 2026-08-14 05:21:00 | NOAA-21 | COCALZINHO DE GOIÁS | GOIÁS | Brasil | 5205513 | 52 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 7b5539e0-cf0b-3a23-aeca-9a4f7f92367a | -14.03937 | -53.58593 | 2026-08-14 05:21:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 6.6 |
| 8f311828-7211-3f84-a29a-567b110eafa4 | -14.05 | -53.5848 | 2026-08-14 05:21:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 21.2 |
| 7df872c4-f64d-3e4a-b1cf-453076b03d53 | -15.1227 | -48.65327 | 2026-08-14 05:21:00 | NOAA-21 | VILA PROPÍCIO | GOIÁS | Brasil | 5222302 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| ec75df37-8b70-3f8a-8b9a-fb3bdab645db | -14.04924 | -53.58216 | 2026-08-14 05:21:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 16.5 |
| 8253cadd-53fe-3146-b320-74452b67f9ff | -16.90405 | -54.14725 | 2026-08-14 05:21:00 | NOAA-21 | PEDRA PRETA | MATO GROSSO | Brasil | 5106372 | 51 | 33 | nan | nan | nan | Cerrado | 3.2 |
| fb6c681e-e6ee-34c4-9358-190ce7419154 | -13.25504 | -50.37864 | 2026-08-14 05:21:00 | NOAA-21 | SÃO MIGUEL DO ARAGUAIA | GOIÁS | Brasil | 5220207 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 4a448fd4-adf6-39f7-9739-266ecc1da387 | -14.2915 | -51.9688 | 2026-08-14 05:21:00 | NOAA-21 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 13.0 |
| f81b7041-d8b4-3384-968c-817dd5b3ab2e | -15.35779 | -49.66903 | 2026-08-14 05:21:00 | NOAA-21 | CARMO DO RIO VERDE | GOIÁS | Brasil | 5205000 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| ca173826-0a13-379a-864d-b8d6d354d6bc | -16.91805 | -54.14832 | 2026-08-14 05:21:00 | NOAA-21 | PEDRA PRETA | MATO GROSSO | Brasil | 5106372 | 51 | 33 | nan | nan | nan | Cerrado | 4.4 |
| b51076e8-e3bc-3dc7-bfe1-48c8a757fd12 | -14.05465 | -53.5853 | 2026-08-14 05:21:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 8d999a80-8d74-3f91-a913-f27fe8ed5406 | -14.35893 | -53.68689 | 2026-08-14 05:21:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 8c4fa3b4-5445-3c8b-b64c-17089b88d1e3 | -14.35751 | -53.69387 | 2026-08-14 05:21:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 6941ef24-1fc6-3948-988c-8fb8759c1fcf | -14.03103 | -53.6226 | 2026-08-14 05:21:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 2.2 |
| bb2f9541-5317-3eb4-95f4-bd1c0f080485 | -17.47981 | -53.33691 | 2026-08-14 05:21:00 | NOAA-21 | ALTO ARAGUAIA | MATO GROSSO | Brasil | 5100300 | 51 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 7e25af12-1f08-36c3-8266-064068d1a367 | -13.74804 | -53.4271 | 2026-08-14 05:21:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| f55fe436-2960-38c0-9dbd-2b7239bed5ac | -13.22992 | -54.27085 | 2026-08-14 05:21:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 5.2 |
| f2bd1611-f134-3caf-9dd0-67804e70398d | -16.92272 | -54.14863 | 2026-08-14 05:21:00 | NOAA-21 | PEDRA PRETA | MATO GROSSO | Brasil | 5106372 | 51 | 33 | nan | nan | nan | Cerrado | 13.0 |
| e2109b59-300c-38ff-9c2f-5824c7d31db2 | -13.82743 | -53.79272 | 2026-08-14 05:21:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 3.3 |
| ab99e931-e496-3e50-8ac7-5cda8411bfd3 | -14.04073 | -53.58366 | 2026-08-14 05:21:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 4.2 |
| f9e98376-ad7d-3fb8-9f13-66b42a44f051 | -13.27977 | -54.22987 | 2026-08-14 05:21:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 93f65d68-20db-3060-989f-b5fd3a981568 | -15.44782 | -52.99808 | 2026-08-14 05:21:00 | NOAA-21 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 970e7b98-e2ce-3a0d-a1e9-4c9c30c27433 | -13.7546 | -53.41304 | 2026-08-14 05:21:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 298909f8-6849-359d-977b-43603a4f3282 | -14.07805 | -53.6157 | 2026-08-14 05:21:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 32e8610e-4826-32b4-839d-0ff5e10104d7 | -14.05583 | -53.64367 | 2026-08-14 05:21:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 4a936113-4544-35ea-ae2b-06db92cb35e9 | -14.28707 | -51.9617 | 2026-08-14 05:21:00 | NOAA-21 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 9.6 |
| 5a13a813-50cc-300b-9bf8-95abc08252fd | -13.90904 | -53.77702 | 2026-08-14 05:21:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 7d45bf4e-31d6-3d63-8921-6c3946a0dd89 | -13.92273 | -53.96431 | 2026-08-14 05:21:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 3f1f4273-0a70-39bc-88a3-bce7ba349aaa | -13.28587 | -54.21745 | 2026-08-14 05:21:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 0242f87d-1c8c-3a0d-b2a4-24280a3d3309 | -16.89947 | -54.14607 | 2026-08-14 05:21:00 | NOAA-21 | PEDRA PRETA | MATO GROSSO | Brasil | 5106372 | 51 | 33 | nan | nan | nan | Cerrado | 2.7 |
| fa53b0eb-aae4-320a-9961-78c5b76dac68 | -13.93291 | -53.9563 | 2026-08-14 05:21:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 7e1696aa-3d63-374f-82b4-85425cb38b15 | -13.24634 | -54.24702 | 2026-08-14 05:21:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 3e3f381d-cc6a-3dfa-9cdd-e8710e2d0f82 | -16.89892 | -54.1508 | 2026-08-14 05:21:00 | NOAA-21 | PEDRA PRETA | MATO GROSSO | Brasil | 5106372 | 51 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 92ea37a1-c73b-3151-8d6c-53ea8bc2a8c2 | -16.91926 | -54.13809 | 2026-08-14 05:21:00 | NOAA-21 | PEDRA PRETA | MATO GROSSO | Brasil | 5106372 | 51 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 7dbdf36c-52d7-339e-9f05-0c113bdb221b | -16.25388 | -53.70817 | 2026-08-14 05:21:00 | NOAA-21 | GUIRATINGA | MATO GROSSO | Brasil | 5104203 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 361e62b5-5264-34df-b95b-d05d17db5a6a | -12.35836 | -50.89695 | 2026-08-14 05:21:00 | NOAA-21 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 2a315846-37db-3f74-9caf-285c67bf9320 | -14.0728 | -53.62012 | 2026-08-14 05:21:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| aeac0c29-9a25-3046-b3b3-d8070a565218 | -15.50974 | -52.99965 | 2026-08-14 05:21:00 | NOAA-21 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 3.0 |
| e44d4d10-b774-34a1-a517-bf1fa2d3a446 | -18.47833 | -51.74795 | 2026-08-14 05:21:00 | NOAA-21 | SERRANÓPOLIS | GOIÁS | Brasil | 5220504 | 52 | 33 | nan | nan | nan | Cerrado | 2.8 |
| a001dcb4-2a43-31af-b215-8c37fb1cf1d9 | -14.044 | -53.58653 | 2026-08-14 05:21:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 6.6 |
| ab147325-4a3c-3864-aef8-cbd010030d1f | -14.08543 | -53.63188 | 2026-08-14 05:21:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 8.3 |
| 106b2d05-fb39-3b03-b824-dd7dfba72c16 | -14.05329 | -53.58753 | 2026-08-14 05:21:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 6.6 |
| ceb0dc9d-d0c9-3112-80b4-5eefaa9409eb | -13.92779 | -53.96052 | 2026-08-14 05:21:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 914c6ddc-a170-3121-95e0-a8433dbd7b53 | -13.8326 | -53.78832 | 2026-08-14 05:21:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 4cdfe95c-2052-3ece-afe1-963060f81942 | -14.45372 | -51.85857 | 2026-08-14 05:21:00 | NOAA-21 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 4da514c9-77d2-30b8-bc68-1e82a848798e | -14.03997 | -53.58091 | 2026-08-14 05:21:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 7.9 |
| 91d5737b-2a9a-399f-b128-bc1dd291e1d3 | -14.06938 | -53.60975 | 2026-08-14 05:21:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 6fe77ee4-5bcf-3c5f-b779-42e6f6c186e9 | -15.51467 | -53.00014 | 2026-08-14 05:21:00 | NOAA-21 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 983301b3-fa6b-3e05-864f-9a884460e837 | -13.75268 | -53.4278 | 2026-08-14 05:21:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 0eca136c-96a0-3b5b-b80f-a530a21812f8 | -14.35698 | -53.08798 | 2026-08-14 05:21:00 | NOAA-21 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 616f75e8-2118-383e-b9bc-ddfad1d05d69 | -21.89928 | -55.36786 | 2026-08-14 05:23:00 | NOAA-21 | DOURADOS | MATO GROSSO DO SUL | Brasil | 5003702 | 50 | 33 | nan | nan | nan | Cerrado | 7.1 |
| c1dc0536-c836-3240-8242-25c22d715087 | -21.90385 | -55.36858 | 2026-08-14 05:23:00 | NOAA-21 | DOURADOS | MATO GROSSO DO SUL | Brasil | 5003702 | 50 | 33 | nan | nan | nan | Cerrado | 5.5 |
| c5218e42-589c-359b-8386-4f075b9be3a1 | -21.89983 | -55.36283 | 2026-08-14 05:23:00 | NOAA-21 | DOURADOS | MATO GROSSO DO SUL | Brasil | 5003702 | 50 | 33 | nan | nan | nan | Cerrado | 7.1 |
| 3311313d-ea8e-30e4-840a-3dfb54fc21bd | -21.9044 | -55.36353 | 2026-08-14 05:23:00 | NOAA-21 | DOURADOS | MATO GROSSO DO SUL | Brasil | 5003702 | 50 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 37dc30da-242b-39d9-bafa-141dfdd9fdc0 | -21.89874 | -55.37293 | 2026-08-14 05:23:00 | NOAA-21 | DOURADOS | MATO GROSSO DO SUL | Brasil | 5003702 | 50 | 33 | nan | nan | nan | Cerrado | 7.5 |
| 6ab59520-2019-36cb-a64c-4ae5aed1b771 | -20.89554 | -50.51018 | 2026-08-14 05:23:00 | NOAA-21 | SANTO ANTÔNIO DO ARACANGUÁ | SÃO PAULO | Brasil | 3548054 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.6 |
| a1aeecd0-dfef-3bbf-b7ec-b04006f3b56d | -21.90329 | -55.3737 | 2026-08-14 05:23:00 | NOAA-21 | DOURADOS | MATO GROSSO DO SUL | Brasil | 5003702 | 50 | 33 | nan | nan | nan | Cerrado | 1.8 |
| b38d7db3-86f6-34c8-baf3-5c3718a1181b | -21.89417 | -55.3722 | 2026-08-14 05:23:00 | NOAA-21 | DOURADOS | MATO GROSSO DO SUL | Brasil | 5003702 | 50 | 33 | nan | nan | nan | Cerrado | 7.5 |
| 5c6ba530-e9c0-3b48-a276-74d2665a56f2 | -11.4885 | -54.6273 | 2026-08-14 05:40:00 | GOES-19 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 48.9 |
| 073204e0-b425-3e38-8110-ca2eb4865831 | -4.49626 | -42.53226 | 2026-08-14 05:53:00 | AQUA_M-M | LAGOA ALEGRE | PIAUÍ | Brasil | 2205557 | 22 | 33 | nan | nan | nan | Caatinga | 56.8 |
| e3dc2341-e57d-340b-9bff-23e9dbb92107 | -4.49377 | -42.52401 | 2026-08-14 05:53:00 | AQUA_M-M | LAGOA ALEGRE | PIAUÍ | Brasil | 2205557 | 22 | 33 | nan | nan | nan | Caatinga | 30.3 |
| 738d8462-c2aa-334f-990a-af926491c8c0 | -4.48975 | -42.54908 | 2026-08-14 05:53:00 | AQUA_M-M | LAGOA ALEGRE | PIAUÍ | Brasil | 2205557 | 22 | 33 | nan | nan | nan | Caatinga | 36.5 |
| 36598b73-2996-3d5e-8849-bd28182d1803 | -8.55365 | -54.59415 | 2026-08-14 05:53:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| eee41e27-484f-3e53-a4e6-81140f7b3198 | -7.58627 | -61.22028 | 2026-08-14 05:53:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 00f6b18c-d984-3901-8c01-62ff705c9e8b | 0.49895 | -60.59386 | 2026-08-14 05:53:00 | NPP-375D | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 1.3 |
| bfbdc4f1-d593-362c-98de-27d154863243 | -8.98301 | -60.53265 | 2026-08-14 05:53:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 15e2f405-d6cb-3b1b-9417-dbdfab27a596 | -7.40647 | -59.98956 | 2026-08-14 05:53:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| e8a09dc4-a59e-3d9d-aea4-cbd164978e69 | -1.78333 | -55.53112 | 2026-08-14 05:53:00 | NPP-375D | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 244f0168-c5c3-3c80-9814-54ba1aa2566b | -11.50652 | -54.6141 | 2026-08-14 05:53:00 | NPP-375D | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| f3df6f13-6f0e-3d4e-9bf3-62c726ccc403 | -9.76734 | -60.76461 | 2026-08-14 05:53:00 | NPP-375D | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 1da0e2d4-826e-34fb-b2f2-a32d1d52226b | -9.1918 | -66.10014 | 2026-08-14 05:53:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 06f7f84d-7a68-3554-b6dc-fe1b5cd9f52f | -9.98357 | -53.94847 | 2026-08-14 05:53:00 | NPP-375D | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 9.0 |
| 5b078d9c-b6de-3866-b8a6-88fb2288b5ee | -11.49463 | -54.61887 | 2026-08-14 05:53:00 | NPP-375D | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 5.4 |
| eab7fa50-3b96-321c-8e69-7820496ef79c | 2.61157 | -61.42912 | 2026-08-14 05:53:00 | NPP-375D | MUCAJAÍ | RORAIMA | Brasil | 1400308 | 14 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 8ce85e58-b0d2-3ab9-9b67-0e0f504fa376 | -2.7503 | -60.23594 | 2026-08-14 05:53:00 | NPP-375D | MANAUS | AMAZONAS | Brasil | 1302603 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 5376fc7b-f6aa-3c13-ba7c-d910db590c59 | -11.49691 | -54.63963 | 2026-08-14 05:53:00 | NPP-375D | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 412ee170-a849-3fbc-b4ab-d3146cf98e13 | -9.76681 | -60.76838 | 2026-08-14 05:53:00 | NPP-375D | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 37141b9d-84b3-3a24-89f3-9ad190079327 | -8.50761 | -64.03876 | 2026-08-14 05:53:00 | NPP-375D | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| aaca32f9-492d-3d7e-957d-e146057c5225 | -1.83037 | -54.50479 | 2026-08-14 05:53:00 | NPP-375D | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 13.0 |
| 3d475cae-04df-3d8d-a66e-c8f782fed65d | -11.49114 | -54.63371 | 2026-08-14 05:53:00 | NPP-375D | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 9a0f4c55-3262-319e-81fa-7fbf34888f9e | -3.14812 | -54.606 | 2026-08-14 05:53:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 836f406b-7fd5-3f54-bd36-3ff38d7c5111 | -8.55301 | -54.59895 | 2026-08-14 05:53:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 7983b4dc-807c-35bb-b87c-b4b22d0ae8fa | -9.97491 | -53.96463 | 2026-08-14 05:53:00 | NPP-375D | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 5.7 |
| 18274096-ed68-34ec-95f6-3ebc2057ca53 | -7.58553 | -61.22523 | 2026-08-14 05:53:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| be71357d-c420-3ab0-b868-e488c6865d07 | -9.97703 | -53.94757 | 2026-08-14 05:53:00 | NPP-375D | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 9.0 |
| ec135361-88e1-3d7b-8b7f-7994dad590db | -7.40534 | -59.99744 | 2026-08-14 05:53:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 0a4960d9-c2e6-315d-a081-e79631c4e6f2 | 0.49826 | -60.58961 | 2026-08-14 05:53:00 | NPP-375D | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 1249d762-23a6-30dd-8e95-c1672408b382 | -9.97633 | -53.95319 | 2026-08-14 05:53:00 | NPP-375D | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 9.0 |
| 3b8b6820-f4cf-3207-8cb8-8b600eb0bc0d | -11.49342 | -54.6294 | 2026-08-14 05:53:00 | NPP-375D | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 51757030-7fbf-35b2-b736-5027712250bb | -8.95693 | -60.53649 | 2026-08-14 05:53:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 820e0b47-7f4e-3ce1-ad88-bb71dc737a8d | -6.98158 | -63.00847 | 2026-08-14 05:53:00 | NPP-375D | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 72b6f20c-3339-3ead-9a0b-c9a8051b7626 | -8.95639 | -60.54026 | 2026-08-14 05:53:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 8465fac4-bc67-34f5-b975-aae01e1bc2da | -9.98098 | -53.95652 | 2026-08-14 05:53:00 | NPP-375D | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 21.9 |
| f8045170-d8a9-3591-93b9-36f01b821241 | -2.36205 | -60.0831 | 2026-08-14 05:53:00 | NPP-375D | MANAUS | AMAZONAS | Brasil | 1302603 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 94920913-a8e5-3cdd-a7b0-a41690c261dc | -11.49239 | -54.62337 | 2026-08-14 05:53:00 | NPP-375D | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 5.1 |
| cfedd0db-22ec-334b-824b-491629093176 | -3.24755 | -60.12353 | 2026-08-14 05:53:00 | NPP-375D | IRANDUBA | AMAZONAS | Brasil | 1301852 | 13 | 33 | nan | nan | nan | Amazônia | 2.4 |
| f23f2f0f-f029-3c96-885f-d8dffff465cf | -9.76787 | -60.76085 | 2026-08-14 05:53:00 | NPP-375D | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 3ac14fb0-397a-3f5b-afe4-1817b04ce10b | -9.18461 | -66.10255 | 2026-08-14 05:53:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| f42cd3b5-21c8-3a31-8963-4fc116fe6219 | -8.89372 | -60.55523 | 2026-08-14 05:53:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 7.1 |
| 76b2bc4a-e238-351c-9695-84f334135e73 | -9.75851 | -60.76717 | 2026-08-14 05:53:00 | NPP-375D | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |


[Clique aqui para ver as próximas entradas](README34.md)
