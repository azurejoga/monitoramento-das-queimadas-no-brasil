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

## Dados Diários - Página 19

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| e4725cf5-a7f3-36ed-907e-da73eb8b44bd | -3.76119 | -46.95414 | 2025-11-28 05:01:00 | NPP-375D | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 17.7 |
| b898e30f-6902-393d-934c-3943104c9788 | -2.96714 | -51.02067 | 2025-11-28 05:01:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 718e1572-0158-372f-8c55-2cf7c5042a08 | -3.17561 | -50.24469 | 2025-11-28 05:01:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 74184521-fe01-3f6b-86d3-8d2e336a069e | -3.10792 | -53.13478 | 2025-11-28 05:01:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 8dcd3913-49f8-389f-8ac2-9ea21716bf70 | -3.39369 | -52.43304 | 2025-11-28 05:01:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 69cb34a3-56e4-33fc-a9ee-197450f89fc2 | -3.36561 | -50.75266 | 2025-11-28 05:01:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 5e1c4fcf-5655-32bb-9100-03f200f4ca2a | -5.30129 | -44.72369 | 2025-11-28 05:01:00 | NPP-375D | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 6b9e245a-dc72-38db-a15e-bc7c7beb1de8 | -3.27693 | -53.75859 | 2025-11-28 05:01:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| c20f61b8-0658-379c-972d-09a272951fc1 | -3.22819 | -50.31574 | 2025-11-28 05:01:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| fb834c96-9dae-3af9-a414-e3863926403f | -3.68326 | -51.69653 | 2025-11-28 05:01:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 1b74fa82-37c9-32da-afdc-50ec260136d9 | -2.84018 | -53.01176 | 2025-11-28 05:01:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 205d0dc8-dee7-3b51-85a5-1dc16ce1f404 | -3.96515 | -50.1951 | 2025-11-28 05:01:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| a96786da-111c-396e-bb6d-c68adafed261 | -4.25922 | -46.24118 | 2025-11-28 05:01:00 | NPP-375D | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 9e59d3a8-d21e-3386-9c38-12a4fd1e7cc7 | -3.43668 | -50.17107 | 2025-11-28 05:01:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 680e324d-ec08-35a8-ac4e-51001804d599 | -3.74334 | -50.9657 | 2025-11-28 05:01:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| d9c23046-373b-325a-a6c7-af0c0891c7f7 | -3.4203 | -50.15537 | 2025-11-28 05:01:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 2f76eece-d258-3409-9726-06b3a7049c73 | -2.71866 | -53.18004 | 2025-11-28 05:01:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| a99ead45-16e7-37a9-90b7-c566a5922aa4 | -2.71148 | -53.18245 | 2025-11-28 05:01:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 26098d3b-f82a-31a5-9589-56e47baa2b3d | -3.36036 | -50.49155 | 2025-11-28 05:01:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 9f7b012a-926b-39b6-904c-4bc7bf91d606 | -3.93297 | -50.16999 | 2025-11-28 05:01:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 32775b9e-1787-33a6-a9ae-4639288d2477 | -5.45049 | -44.69307 | 2025-11-28 05:01:00 | NPP-375D | SANTA FILOMENA DO MARANHÃO | MARANHÃO | Brasil | 2109759 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| cd3c1624-06a1-3be0-a848-e6b390704511 | -3.24785 | -50.01829 | 2025-11-28 05:01:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 4ea3ed42-1a84-3450-a44b-cb1c6c46b94e | -3.60876 | -52.61768 | 2025-11-28 05:01:00 | NPP-375D | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 8dd9703b-3de5-303c-b396-b0692aa98f50 | -2.72224 | -53.17719 | 2025-11-28 05:01:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| fa4ac0c9-09c2-3315-8511-72b983e3062f | -3.82693 | -50.10675 | 2025-11-28 05:01:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 39272a3d-48c7-3416-b1f2-a3479eeea6db | -3.8395 | -52.03583 | 2025-11-28 05:01:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 5c7e0e06-3969-3681-9da2-86fc56ddb215 | -3.39837 | -54.54765 | 2025-11-28 05:01:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 34f0b4ba-53aa-3788-bd64-93f6e97f246b | -5.06249 | -40.82487 | 2025-11-28 05:01:00 | NPP-375D | CRATEÚS | CEARÁ | Brasil | 2304103 | 23 | 33 | nan | nan | nan | Caatinga | 3.8 |
| 7886089d-f72f-394a-a29f-35f0fd5ea341 | -3.6861 | -51.70079 | 2025-11-28 05:01:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| f5b82d4e-d614-3cfc-b0ae-6040ac9892fc | -5.53537 | -46.97889 | 2025-11-28 05:01:00 | NPP-375D | BURITIRANA | MARANHÃO | Brasil | 2102358 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| e17c3637-c73e-313d-a2ea-4a83b2cbfff9 | -4.05646 | -46.56176 | 2025-11-28 05:01:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 5f6823a5-b817-3ed5-8331-d82f9009f498 | -4.30004 | -55.6148 | 2025-11-28 05:01:00 | NPP-375D | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| d670554b-d272-33d9-aa2e-01f5a60eb360 | -5.13199 | -43.01867 | 2025-11-28 05:01:00 | NPP-375D | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| a2022390-a8e3-3595-b7ae-d94e6b5b2f05 | -4.30036 | -48.60016 | 2025-11-28 05:01:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| fb461d05-3349-365a-a9da-91b569d0bcae | -3.45211 | -50.55044 | 2025-11-28 05:01:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 44cefce0-0a20-3306-ab7d-b41120ebe16d | -3.91604 | -50.44461 | 2025-11-28 05:01:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| cbfdab78-352b-328b-9d2a-9d65715e109d | -3.07697 | -50.35355 | 2025-11-28 05:01:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 0e17c846-383c-390e-b5da-e2c87e9f105a | -3.3493 | -54.08879 | 2025-11-28 05:01:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 98605c45-a399-3787-bab2-cee6eb8a943e | -4.29944 | -55.61852 | 2025-11-28 05:01:00 | NPP-375D | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 92335e99-0b29-355b-af25-27f8f7e4be09 | -2.8262 | -54.0384 | 2025-11-28 05:01:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| c322333e-02c1-321c-b78f-cd1a08350f98 | -3.26157 | -51.16998 | 2025-11-28 05:01:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| bd3a021f-8214-3914-858c-dcf2ce3e6b02 | -2.9891 | -52.51461 | 2025-11-28 05:01:00 | NPP-375D | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 2c0935c1-462e-3043-95bb-29865281e079 | -4.06595 | -49.44255 | 2025-11-28 05:01:00 | NPP-375D | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 31d1b2f0-2178-3c9a-ab71-b2a24df29a9e | -4.03965 | -43.36015 | 2025-11-28 05:01:00 | NPP-375D | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| cf784d5a-b3da-387f-8772-2e14a1b8fd3e | -3.558 | -52.07423 | 2025-11-28 05:01:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 5e939276-cec4-34b4-b267-287066370228 | -3.85151 | -47.03443 | 2025-11-28 05:01:00 | NPP-375D | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 540862e2-22fa-31da-b670-ea726d1605a3 | -2.98915 | -49.11961 | 2025-11-28 05:01:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| d264590e-4694-3da4-af04-f5a9b1cb0dd6 | -5.04795 | -47.44001 | 2025-11-28 05:01:00 | NPP-375D | SÃO FRANCISCO DO BREJÃO | MARANHÃO | Brasil | 2110856 | 21 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 850ac18a-8662-3886-a80c-0e796573945b | -2.74073 | -54.59618 | 2025-11-28 05:01:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 43f307d6-fa2a-39a0-909f-45ba4d01258c | -3.01433 | -51.154 | 2025-11-28 05:01:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 9d1d3af3-280d-3044-bb34-38da17293c30 | -3.46776 | -56.31577 | 2025-11-28 05:01:00 | NPP-375D | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| b4398e34-489b-30d5-a4fc-6df6596fe33f | -4.43831 | -55.60192 | 2025-11-28 05:01:00 | NPP-375D | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 08649ef9-6bf3-3704-84c8-fb2b4aa9fe05 | -2.71203 | -53.179 | 2025-11-28 05:01:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 59ab6fd9-3253-3323-bc88-c160f5d2eb13 | -3.45749 | -53.04447 | 2025-11-28 05:01:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 369a8bcc-fbb3-395a-9d40-295712d06a79 | -3.16499 | -50.6049 | 2025-11-28 05:01:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 1a2eefa0-dfe0-348b-9b65-ce2e42fee756 | -4.18447 | -48.63056 | 2025-11-28 05:01:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 5385f5a1-0412-37e0-9d79-043fc9d82281 | -3.85015 | -47.04337 | 2025-11-28 05:01:00 | NPP-375D | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 2.5 |
| b14a5a5b-80b0-3ecb-9362-bacd498584d3 | -3.48932 | -53.26899 | 2025-11-28 05:01:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 580e8a5d-5d00-3470-8725-978bcdeeceb0 | -3.36268 | -50.74809 | 2025-11-28 05:01:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 98cde2d5-8b4b-3f8d-aa91-f5fc8ccb4a2c | -3.83938 | -50.31382 | 2025-11-28 05:01:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 6e978f3f-b0db-3407-8dac-f6e54c61dba7 | -3.50523 | -53.44819 | 2025-11-28 05:01:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 7c96bba0-42c8-3e08-960b-f288c20d640e | -3.27638 | -53.76204 | 2025-11-28 05:01:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 9793507b-c145-349d-bde8-d97661d8baf3 | -3.43982 | -52.18136 | 2025-11-28 05:01:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| a94a93bb-aee7-3465-9443-63f5f47e0d44 | -3.56139 | -52.07477 | 2025-11-28 05:01:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| d8ae6576-6a8d-3f5d-87bf-3d0b24965a1c | -2.81249 | -50.46801 | 2025-11-28 05:01:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 5a3eceb3-4c57-3130-ae71-39e999a32ee4 | -3.35676 | -50.49099 | 2025-11-28 05:01:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 4f5a0580-0e1a-3dc3-9e09-589c0b0aadfb | -3.92645 | -50.9922 | 2025-11-28 05:01:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 55f7dcb1-3a90-34c8-9716-276e433c0696 | -3.3482 | -54.09571 | 2025-11-28 05:01:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 0813baf4-f2da-3faf-af56-5d2925b1f74f | -3.24861 | -50.69069 | 2025-11-28 05:01:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 4b8cc015-bd26-30d2-8455-0a4170ee7000 | -3.38178 | -51.50225 | 2025-11-28 05:01:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 50924154-bb19-30af-8bbf-6ce33745cab6 | -2.72933 | -51.83658 | 2025-11-28 05:01:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 03c34345-708f-3cf8-a515-cc53d11feaee | -3.30879 | -51.54069 | 2025-11-28 05:01:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 988afa4a-b257-39da-9bfd-29e6e40aafc3 | -3.85533 | -47.03964 | 2025-11-28 05:01:00 | NPP-375D | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 73a64a29-7d5b-3b50-8ea4-21c926ef39b8 | -4.06361 | -49.43928 | 2025-11-28 05:01:00 | NPP-375D | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| c658a37d-d486-38ff-9cd7-91398500cf23 | -2.56395 | -54.75886 | 2025-11-28 05:01:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| aab8922b-aed3-3a77-93d7-68c3e70bbca1 | -2.83899 | -52.39788 | 2025-11-28 05:01:00 | NPP-375D | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| fe81782a-00b0-3186-bf9e-b866c4a144c3 | -2.93995 | -51.42503 | 2025-11-28 05:01:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| fcd412de-d6a3-3886-ade2-d080e9f132ea | -3.46053 | -50.5503 | 2025-11-28 05:01:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 992f3021-4f2c-3435-99ce-072d66140c51 | -3.40993 | -53.30272 | 2025-11-28 05:01:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 06f9fbef-8a11-3c11-b9d4-34381e7a5802 | -3.06187 | -50.35547 | 2025-11-28 05:01:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 84652673-341a-3d71-8dee-1483900de699 | -3.78972 | -43.57492 | 2025-11-28 05:01:00 | NPP-375D | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| e4e665c8-3d91-3993-99bc-7dec47442051 | -3.06612 | -50.35188 | 2025-11-28 05:01:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| e2b74b80-6495-3a4f-aafd-db1f48afb65d | -4.46172 | -48.12022 | 2025-11-28 05:01:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| bd37b3e2-0e33-3553-aa65-08b5b578b921 | -2.85401 | -53.01036 | 2025-11-28 05:01:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 561e93d3-40b5-3c97-8f0b-7691127a5a38 | -3.03106 | -50.9789 | 2025-11-28 05:01:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 618a3759-c0b0-344e-8fd7-2a009c4de6f4 | -3.75734 | -46.94901 | 2025-11-28 05:01:00 | NPP-375D | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 75db604a-ee60-3a40-b209-263f418ee8e8 | -3.20535 | -50.80672 | 2025-11-28 05:01:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 6d85a5f5-101d-321e-8df9-a0ef03fedbd8 | -3.85082 | -47.03894 | 2025-11-28 05:01:00 | NPP-375D | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 88509ab9-9004-36b3-92b2-ecadf51facf5 | -3.38581 | -51.49905 | 2025-11-28 05:01:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 4a2460a0-ce84-37e9-92fe-a2f271b99216 | -3.33986 | -50.26671 | 2025-11-28 05:01:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 39e68050-b130-3edb-b9a3-45901393b52b | -3.74127 | -50.03773 | 2025-11-28 05:01:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| dd21cb28-fcb3-370f-9287-47ebccec580e | -5.29925 | -44.72364 | 2025-11-28 05:01:00 | NPP-375D | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 8b92cde5-185f-3359-b3b2-76b8fff5ad7a | -3.25279 | -50.68724 | 2025-11-28 05:01:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 5d3de012-7790-3261-a90b-d64bcb1c2635 | -6.73011 | -40.82346 | 2025-11-28 05:01:00 | NPP-375D | PIO IX | PIAUÍ | Brasil | 2208205 | 22 | 33 | nan | nan | nan | Caatinga | 3.1 |
| 91ca2413-2c0e-358f-b968-1b2386601380 | -3.1046 | -53.13426 | 2025-11-28 05:01:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 485e9f14-3258-3c7d-9738-27e500453479 | -3.23313 | -50.6965 | 2025-11-28 05:01:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| cafa7b82-bac4-347a-966d-34ff9e57544c | -3.52423 | -53.06894 | 2025-11-28 05:01:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 1070e0a3-d7b5-369b-9c26-7159b32963ed | -5.57923 | -44.57942 | 2025-11-28 05:01:00 | NPP-375D | SANTA FILOMENA DO MARANHÃO | MARANHÃO | Brasil | 2109759 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 62928178-6909-3fd6-8d84-9226c63d1c3d | -16.14165 | -59.96345 | 2025-11-28 05:03:00 | NPP-375D | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 89f4a87e-3ce0-3cd2-9793-14ce9ec842d8 | -12.28187 | -64.40996 | 2025-11-28 05:03:00 | NPP-375D | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 0.9 |


[Clique aqui para ver as próximas entradas](README20.md)
