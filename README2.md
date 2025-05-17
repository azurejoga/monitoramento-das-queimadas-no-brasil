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

## Dados Diários - Página 2

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| f42e5655-b57f-3a1b-b5e5-17691a6122d9 | -11.1574 | -48.67156 | 2025-05-17 01:13:00 | TERRA_M-M | BREJINHO DE NAZARÉ | TOCANTINS | Brasil | 1703701 | 17 | 33 | nan | nan | nan | Cerrado | 85.1 |
| f55339ff-484a-3a20-b549-56af7d70117e | -13.38504 | -56.91069 | 2025-05-17 01:13:00 | TERRA_M-M | SÃO JOSÉ DO RIO CLARO | MATO GROSSO | Brasil | 5107305 | 51 | 33 | nan | nan | nan | Amazônia | 6.3 |
| 92451aad-694b-3bfd-badf-262a01862e75 | -14.01842 | -55.13725 | 2025-05-17 01:13:00 | TERRA_M-M | SANTA RITA DO TRIVELATO | MATO GROSSO | Brasil | 5107768 | 51 | 33 | nan | nan | nan | Cerrado | 7.0 |
| 6fd17eba-0551-355c-a44e-dd3efc29fa06 | -13.04199 | -53.7229 | 2025-05-17 01:13:00 | TERRA_M-M | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 7.4 |
| f04d129b-6524-3102-963f-4187458fcb40 | -13.14963 | -56.80193 | 2025-05-17 01:13:00 | TERRA_M-M | SÃO JOSÉ DO RIO CLARO | MATO GROSSO | Brasil | 5107305 | 51 | 33 | nan | nan | nan | Amazônia | 47.6 |
| f16777fb-9c7c-308b-bf06-6f79e49be34d | -14.01715 | -55.12819 | 2025-05-17 01:13:00 | TERRA_M-M | SANTA RITA DO TRIVELATO | MATO GROSSO | Brasil | 5107768 | 51 | 33 | nan | nan | nan | Cerrado | 9.2 |
| 542f022d-bb8f-363d-a076-7578b9151c3d | -11.4233 | -54.32948 | 2025-05-17 01:13:00 | TERRA_M-M | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 7.0 |
| a6249c08-b381-3895-b2b9-3979c1094c35 | -13.14186 | -56.81259 | 2025-05-17 01:13:00 | TERRA_M-M | SÃO JOSÉ DO RIO CLARO | MATO GROSSO | Brasil | 5107305 | 51 | 33 | nan | nan | nan | Amazônia | 63.2 |
| 8ba8e440-7b96-3d69-b477-e84cb9001221 | -13.39538 | -56.91891 | 2025-05-17 01:13:00 | TERRA_M-M | SÃO JOSÉ DO RIO CLARO | MATO GROSSO | Brasil | 5107305 | 51 | 33 | nan | nan | nan | Cerrado | 26.5 |
| f8897ed9-de3a-3b67-9f3c-fbe5267571b9 | -11.36224 | -52.95135 | 2025-05-17 01:13:00 | TERRA_M-M | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 7.9 |
| 40e784dc-46b8-378f-9098-a5d55958be95 | -11.42191 | -54.31994 | 2025-05-17 01:13:00 | TERRA_M-M | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 10.9 |
| 4c0c9326-ed87-3ffd-b961-634702b71475 | -10.39721 | -57.55187 | 2025-05-17 01:13:00 | TERRA_M-M | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 8fb87d97-49c9-3799-a27d-1f3d7362903d | -14.02851 | -55.14497 | 2025-05-17 01:13:00 | TERRA_M-M | SANTA RITA DO TRIVELATO | MATO GROSSO | Brasil | 5107768 | 51 | 33 | nan | nan | nan | Cerrado | 9.5 |
| 6fd25e8e-0ea4-333b-8b48-1426895b216c | -13.85553 | -59.72451 | 2025-05-17 01:13:00 | TERRA_M-M | COMODORO | MATO GROSSO | Brasil | 5103304 | 51 | 33 | nan | nan | nan | Cerrado | 8.9 |
| 5809851f-ae3c-38ac-bdba-618a6372a945 | -13.30355 | -45.36051 | 2025-05-17 01:13:00 | TERRA_M-M | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 48.7 |
| 244b1f6f-614d-3be5-bbbe-e44065d29dc9 | -12.44829 | -57.20129 | 2025-05-17 01:13:00 | TERRA_M-M | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 6.1 |
| 7c1a8682-b776-36b9-b3ff-96be1fe927e5 | -11.15027 | -48.67934 | 2025-05-17 01:13:00 | TERRA_M-M | BREJINHO DE NAZARÉ | TOCANTINS | Brasil | 1703701 | 17 | 33 | nan | nan | nan | Cerrado | 19.0 |
| b607d19e-defb-34e7-8715-1f23bb7b4f1d | -14.01589 | -55.11913 | 2025-05-17 01:13:00 | TERRA_M-M | SANTA RITA DO TRIVELATO | MATO GROSSO | Brasil | 5107768 | 51 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 294ff626-d781-36aa-8c89-73fdc14e8564 | -11.16386 | -48.67709 | 2025-05-17 01:13:00 | TERRA_M-M | BREJINHO DE NAZARÉ | TOCANTINS | Brasil | 1703701 | 17 | 33 | nan | nan | nan | Cerrado | 97.9 |
| ca2360ac-4ebc-3f48-bfe1-5cc3b080f69b | -11.42825 | -54.29945 | 2025-05-17 01:13:00 | TERRA_M-M | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 10.9 |
| 511ca029-8446-31c0-95f1-9264896bdd24 | -14.02725 | -55.13592 | 2025-05-17 01:13:00 | TERRA_M-M | SANTA RITA DO TRIVELATO | MATO GROSSO | Brasil | 5107768 | 51 | 33 | nan | nan | nan | Cerrado | 26.5 |
| 4265c386-7c4c-3e28-890a-8254e3d73e15 | -11.35412 | -52.96405 | 2025-05-17 01:13:00 | TERRA_M-M | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 6.5 |
| 351d9ec9-40b1-3ecf-a396-c1dc13ef28f8 | -13.16115 | -56.81943 | 2025-05-17 01:13:00 | TERRA_M-M | SÃO JOSÉ DO RIO CLARO | MATO GROSSO | Brasil | 5107305 | 51 | 33 | nan | nan | nan | Amazônia | 11.9 |
| 360c83be-9dc3-3f58-b7b7-4bac0fa9ff89 | -11.78778 | -47.35087 | 2025-05-17 01:13:00 | TERRA_M-M | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 61.3 |
| ffdfd9bb-99b0-3a5f-aaf4-933895f886c5 | -11.36388 | -52.96251 | 2025-05-17 01:13:00 | TERRA_M-M | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 6.0 |
| 78f62adb-a551-303b-8fa6-bee95b13f634 | -11.39455 | -52.95182 | 2025-05-17 01:13:00 | TERRA_M-M | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 9.3 |
| 936b7ee4-328d-398c-b685-14854e500e6b | -10.47611 | -49.14369 | 2025-05-17 01:13:00 | TERRA_M-M | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 26.4 |
| d036bad7-f021-32b6-b0e2-79b1edd7e921 | -11.16126 | -48.69431 | 2025-05-17 01:13:00 | TERRA_M-M | BREJINHO DE NAZARÉ | TOCANTINS | Brasil | 1703701 | 17 | 33 | nan | nan | nan | Cerrado | 33.3 |
| 3af642c7-e04a-30b4-a4be-37af22e82d31 | -13.38632 | -56.9202 | 2025-05-17 01:13:00 | TERRA_M-M | SÃO JOSÉ DO RIO CLARO | MATO GROSSO | Brasil | 5107305 | 51 | 33 | nan | nan | nan | Amazônia | 6.5 |
| 4d3cdd8c-f389-36d4-afd2-161dceddd5fb | -11.4142 | -54.33083 | 2025-05-17 01:13:00 | TERRA_M-M | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 4.8 |
| c71b8462-b83b-3734-a5d7-f219ebd02c5a | -13.31045 | -45.39837 | 2025-05-17 01:13:00 | TERRA_M-M | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 46.7 |
| fb0bd026-f641-3001-8236-ed4ec90041a3 | -12.64019 | -57.19146 | 2025-05-17 01:13:00 | TERRA_M-M | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 5.6 |
| 35452541-4e8f-3430-a36d-00fb88d14c34 | -11.64326 | -48.02881 | 2025-05-17 01:13:00 | TERRA_M-M | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | 24.5 |
| cc038389-5311-3fd5-8e9d-8fed9f16fcbd | -11.78876 | -47.3561 | 2025-05-17 01:13:00 | TERRA_M-M | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 49.9 |
| a29a3468-cb19-3fa0-9564-c46d47244c0f | -13.15088 | -56.81133 | 2025-05-17 01:13:00 | TERRA_M-M | SÃO JOSÉ DO RIO CLARO | MATO GROSSO | Brasil | 5107305 | 51 | 33 | nan | nan | nan | Amazônia | 58.0 |
| f718b36c-92f5-3325-b19a-3735b86830f2 | -6.5714 | -51.12044 | 2025-05-17 01:15:00 | TERRA_M-M | OURILÂNDIA DO NORTE | PARÁ | Brasil | 1505437 | 15 | 33 | nan | nan | nan | Amazônia | 14.8 |
| 194d0855-1455-38ce-a6c3-61627d7965f1 | -9.25638 | -60.32378 | 2025-05-17 01:15:00 | TERRA_M-M | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 7.3 |
| 6ca8290c-7aac-3824-ade6-cd00c55f2339 | -13.317 | -45.3803 | 2025-05-17 01:20:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 122.4 |
| b69cf145-8439-3082-bfec-4e5644677e3c | -13.2981 | -45.3603 | 2025-05-17 01:20:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 78.5 |
| 00341834-3570-3445-9ce2-b7d58a3ccd10 | -11.1531 | -48.6736 | 2025-05-17 01:20:00 | GOES-19 | BREJINHO DE NAZARÉ | TOCANTINS | Brasil | 1703701 | 17 | 33 | nan | nan | nan | Cerrado | 54.0 |
| 280b74c5-ec5f-3eb8-b158-59d602b0c7ca | -13.3175 | -45.3571 | 2025-05-17 01:20:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 96.1 |
| e4c0ebb7-4e97-33a9-b3fe-545a6373dd80 | -13.2977 | -45.3835 | 2025-05-17 01:20:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 82.6 |
| d5dbb310-0ea8-37ab-9858-f3f243e73f75 | -13.1498 | -56.8054 | 2025-05-17 01:20:00 | GOES-19 | SÃO JOSÉ DO RIO CLARO | MATO GROSSO | Brasil | 5107305 | 51 | 33 | nan | nan | nan | Amazônia | 113.6 |
| bf77e4aa-aa95-3047-9db4-be1fa77ca44f | -13.2981 | -45.3603 | 2025-05-17 01:30:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 66.8 |
| d8e00e47-b3f5-3cfb-807e-1abc2e2ef0e7 | -13.2977 | -45.3835 | 2025-05-17 01:30:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 78.8 |
| 9d36c193-77fb-3578-ae89-5e61ae1cbc1b | -13.3175 | -45.3571 | 2025-05-17 01:30:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 80.8 |
| 2e5d13b8-2f31-3099-a633-0a5c9c3422a1 | -13.1498 | -56.8054 | 2025-05-17 01:30:00 | GOES-19 | SÃO JOSÉ DO RIO CLARO | MATO GROSSO | Brasil | 5107305 | 51 | 33 | nan | nan | nan | Amazônia | 99.1 |
| c1fd3632-274f-30d9-b60d-e41b243e3412 | -11.1531 | -48.6736 | 2025-05-17 01:30:00 | GOES-19 | BREJINHO DE NAZARÉ | TOCANTINS | Brasil | 1703701 | 17 | 33 | nan | nan | nan | Cerrado | 55.5 |
| 5a2034de-1ab5-3631-884a-5d6ee7ab65ae | -13.317 | -45.3803 | 2025-05-17 01:30:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 112.9 |
| 9b27dee5-103e-3c8f-958b-11c0a2fa502e | -13.2977 | -45.3835 | 2025-05-17 01:40:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 71.7 |
| 6ee8d3b2-67e4-3129-907b-54fe1522e953 | -13.3175 | -45.3571 | 2025-05-17 01:40:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 65.1 |
| 02b20a1f-580d-3ac5-991f-1ad254aaa20f | -13.2981 | -45.3603 | 2025-05-17 01:40:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 57.7 |
| 25524e6b-8091-3240-b167-2bcd3c582ed6 | -13.317 | -45.3803 | 2025-05-17 01:40:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 101.0 |
| 63db0179-0fd9-3560-93e7-c429b61abb4b | -13.1498 | -56.8054 | 2025-05-17 01:40:00 | GOES-19 | SÃO JOSÉ DO RIO CLARO | MATO GROSSO | Brasil | 5107305 | 51 | 33 | nan | nan | nan | Amazônia | 83.4 |
| a92e3452-a442-376e-a76f-bd442be7514b | -11.1531 | -48.6736 | 2025-05-17 01:40:00 | GOES-19 | BREJINHO DE NAZARÉ | TOCANTINS | Brasil | 1703701 | 17 | 33 | nan | nan | nan | Cerrado | 51.3 |
| b10d4c88-f846-3906-9518-dc580a13aab5 | -13.1498 | -56.8054 | 2025-05-17 01:50:00 | GOES-19 | SÃO JOSÉ DO RIO CLARO | MATO GROSSO | Brasil | 5107305 | 51 | 33 | nan | nan | nan | Amazônia | 84.2 |
| 9d8becfa-91e2-334f-a55f-17b64b973009 | -13.2981 | -45.3603 | 2025-05-17 01:50:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 55.1 |
| a8964939-21aa-380e-a377-7254ff1e5c2c | -13.3175 | -45.3571 | 2025-05-17 01:50:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 71.6 |
| 14fcee9c-0141-344e-87c5-679d691da5fb | -13.317 | -45.3803 | 2025-05-17 01:50:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 85.9 |
| ee27421a-4783-32b1-8707-b1575ffb5125 | -13.3175 | -45.3571 | 2025-05-17 02:00:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 65.3 |
| 0febc824-b679-3017-907b-e39abc55c27f | -13.1498 | -56.8054 | 2025-05-17 02:00:00 | GOES-19 | SÃO JOSÉ DO RIO CLARO | MATO GROSSO | Brasil | 5107305 | 51 | 33 | nan | nan | nan | Amazônia | 74.2 |
| 3c385514-c485-3890-98bf-44cea1180fb9 | -13.317 | -45.3803 | 2025-05-17 02:00:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 83.0 |
| 0f8b3297-9846-33d7-a066-86f41c9a23ca | -11.1531 | -48.6736 | 2025-05-17 02:10:00 | GOES-19 | BREJINHO DE NAZARÉ | TOCANTINS | Brasil | 1703701 | 17 | 33 | nan | nan | nan | Cerrado | 49.2 |
| ab4f5bce-f4bf-30b8-99ae-d71da32a0222 | -13.1498 | -56.8054 | 2025-05-17 02:10:00 | GOES-19 | SÃO JOSÉ DO RIO CLARO | MATO GROSSO | Brasil | 5107305 | 51 | 33 | nan | nan | nan | Amazônia | 73.6 |
| a61a7790-4fa9-3eeb-942c-9a8d46af5692 | -13.3175 | -45.3571 | 2025-05-17 02:10:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 55.5 |
| fd1f12d9-6798-3cc0-9ecb-6cf286b12d67 | -13.317 | -45.3803 | 2025-05-17 02:10:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 76.9 |
| 28c19309-60cc-3f44-8cc1-ceb588f11937 | -13.317 | -45.3803 | 2025-05-17 02:20:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 71.6 |
| eecca14e-8f36-398e-b01b-3baddbf27726 | -13.1498 | -56.8054 | 2025-05-17 02:20:00 | GOES-19 | SÃO JOSÉ DO RIO CLARO | MATO GROSSO | Brasil | 5107305 | 51 | 33 | nan | nan | nan | Amazônia | 59.7 |
| 57dbec83-58fc-3048-9f32-a0b626e74017 | -21.1376 | -50.7192 | 2025-05-17 02:30:00 | GOES-19 | GUARARAPES | SÃO PAULO | Brasil | 3518206 | 35 | 33 | nan | nan | nan | Mata Atlântica | 55.9 |
| 1e992f34-392d-3fc8-b50a-a84332ddb143 | -13.1498 | -56.8054 | 2025-05-17 02:30:00 | GOES-19 | SÃO JOSÉ DO RIO CLARO | MATO GROSSO | Brasil | 5107305 | 51 | 33 | nan | nan | nan | Amazônia | 61.0 |
| d3ae7acd-7580-3797-87d5-7e7471050b5b | -13.317 | -45.3803 | 2025-05-17 02:30:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 62.6 |
| bf3f919e-1e52-394a-99d9-d0f04a9a336b | -13.1498 | -56.8054 | 2025-05-17 02:40:00 | GOES-19 | SÃO JOSÉ DO RIO CLARO | MATO GROSSO | Brasil | 5107305 | 51 | 33 | nan | nan | nan | Amazônia | 53.0 |
| ea57bff3-ae53-36f6-8674-bd49d11077e1 | -13.317 | -45.3803 | 2025-05-17 02:40:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 61.4 |
| 8db00b50-c55d-339a-aa36-94bf05b9107a | -13.1498 | -56.8054 | 2025-05-17 02:50:00 | GOES-19 | SÃO JOSÉ DO RIO CLARO | MATO GROSSO | Brasil | 5107305 | 51 | 33 | nan | nan | nan | Amazônia | 53.0 |
| bb3bc046-7754-316d-bb1a-826e23a6341b | -13.1498 | -56.8054 | 2025-05-17 03:00:00 | GOES-19 | SÃO JOSÉ DO RIO CLARO | MATO GROSSO | Brasil | 5107305 | 51 | 33 | nan | nan | nan | Amazônia | 48.3 |
| 237a512f-e930-3ecd-82f0-d557e1535fff | -13.1498 | -56.8054 | 2025-05-17 03:10:00 | GOES-19 | SÃO JOSÉ DO RIO CLARO | MATO GROSSO | Brasil | 5107305 | 51 | 33 | nan | nan | nan | Amazônia | 50.6 |
| cea1d5cb-43f1-3624-858f-6dfbf707c29e | -13.1498 | -56.8054 | 2025-05-17 03:20:00 | GOES-19 | SÃO JOSÉ DO RIO CLARO | MATO GROSSO | Brasil | 5107305 | 51 | 33 | nan | nan | nan | Amazônia | 49.5 |
| 165758ba-271a-3aae-adbe-01cc0def5a78 | -13.1498 | -56.8054 | 2025-05-17 03:30:00 | GOES-19 | SÃO JOSÉ DO RIO CLARO | MATO GROSSO | Brasil | 5107305 | 51 | 33 | nan | nan | nan | Amazônia | 52.0 |
| 39871a9c-9632-378b-a7f3-af15eae9c94e | -6.62545 | -48.01443 | 2025-05-17 03:47:00 | NOAA-21 | DARCINÓPOLIS | TOCANTINS | Brasil | 1706506 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 0e048001-2f8d-3816-8703-cacd348f149c | -7.904 | -44.48385 | 2025-05-17 03:47:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 7.4 |
| f95b099c-3674-364e-ab36-f34760af5758 | -7.90647 | -44.48586 | 2025-05-17 03:47:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.4 |
| fa9b891d-6baf-37a0-ab05-85def7857c64 | -6.78926 | -47.59552 | 2025-05-17 03:47:00 | NOAA-21 | DARCINÓPOLIS | TOCANTINS | Brasil | 1706506 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 8ccf0748-3544-321f-a7b5-389d16e7d9c4 | -5.10644 | -44.80007 | 2025-05-17 03:47:00 | NOAA-21 | JOSELÂNDIA | MARANHÃO | Brasil | 2105609 | 21 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 81f8066a-a72f-3c33-ae0f-70d9596b7365 | -8.13748 | -41.13584 | 2025-05-17 03:47:00 | NOAA-21 | PAULISTANA | PIAUÍ | Brasil | 2207801 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 9ad1bdf5-a39a-345d-8812-4e3cd2dccab9 | -6.84519 | -42.7977 | 2025-05-17 03:47:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 2.8 |
| 818cfdaa-5da2-3020-a606-274e17bffa8b | -9.03034 | -36.6737 | 2025-05-17 03:47:00 | NOAA-21 | TEREZINHA | PERNAMBUCO | Brasil | 2615102 | 26 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| d0e31934-06f7-34c6-affb-190d8467bd88 | -6.84878 | -42.80243 | 2025-05-17 03:47:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 2.8 |
| 5b28138b-822f-302b-ac20-e4a2ccd112fe | -6.17476 | -48.0612 | 2025-05-17 03:47:00 | NOAA-21 | ANANÁS | TOCANTINS | Brasil | 1701002 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| d72de04e-082f-3d24-9b1c-6cd600b6eb8e | -8.13824 | -41.13119 | 2025-05-17 03:47:00 | NOAA-21 | PAULISTANA | PIAUÍ | Brasil | 2207801 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 96ad454b-5bd9-391b-9c55-f2d1f1070dd9 | -6.62666 | -48.01483 | 2025-05-17 03:47:00 | NOAA-21 | DARCINÓPOLIS | TOCANTINS | Brasil | 1706506 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 080ed063-b8e6-3c6d-b530-a840fdbf7ae3 | -6.71858 | -42.13359 | 2025-05-17 03:47:00 | NOAA-21 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 5e622365-a57d-3651-827e-9865ed8e4e81 | -6.72328 | -42.1306 | 2025-05-17 03:47:00 | NOAA-21 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| d5b03088-9e4f-3308-a932-4ba58a7d1d21 | -6.62455 | -48.01945 | 2025-05-17 03:47:00 | NOAA-21 | DARCINÓPOLIS | TOCANTINS | Brasil | 1706506 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 60cbfea7-0539-3ea3-951e-a2143ebac806 | -6.62016 | -48.00905 | 2025-05-17 03:47:00 | NOAA-21 | DARCINÓPOLIS | TOCANTINS | Brasil | 1706506 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 310111a8-e2bd-3da9-885a-da72ab668b67 | -6.62573 | -48.01984 | 2025-05-17 03:47:00 | NOAA-21 | DARCINÓPOLIS | TOCANTINS | Brasil | 1706506 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 7fec2d3d-e310-36dd-a1b1-dd0d5b069bdd | -6.70979 | -42.13589 | 2025-05-17 03:47:00 | NOAA-21 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| be193e11-0977-339a-8010-de6b5761da7b | -6.70916 | -42.13961 | 2025-05-17 03:47:00 | NOAA-21 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| f48cfe39-23c1-3099-97d5-fa854279d663 | -6.62142 | -48.00937 | 2025-05-17 03:47:00 | NOAA-21 | DARCINÓPOLIS | TOCANTINS | Brasil | 1706506 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| be600d8d-d601-3d7b-8bef-c5adbecac965 | -9.03088 | -36.6702 | 2025-05-17 03:47:00 | NOAA-21 | TEREZINHA | PERNAMBUCO | Brasil | 2615102 | 26 | 33 | nan | nan | nan | Mata Atlântica | 1.9 |
| 5f77441c-5430-3353-8866-ac702c27378a | -5.10193 | -44.79614 | 2025-05-17 03:47:00 | NOAA-21 | JOSELÂNDIA | MARANHÃO | Brasil | 2105609 | 21 | 33 | nan | nan | nan | Cerrado | 7.6 |


[Clique aqui para ver as próximas entradas](README3.md)
