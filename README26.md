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

## Dados Diários - Página 26

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| acfe7ccd-b611-3bb2-84e4-5f633c6e00f4 | -2.9939 | -54.062199 | 2026-10-08 00:48:00 | METOP-C | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 42319d32-61b2-3e8f-901e-83ae1096ada0 | -15.4293 | -46.110298 | 2026-10-08 00:48:00 | METOP-C | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| 2586a243-8bb3-389b-8e0c-76e3e6a96db9 | -9.8825 | -50.505001 | 2026-10-08 00:48:00 | METOP-C | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 5a8ed5d7-4ada-3f38-8a7b-e3517e69c41c | -5.9637 | -55.379501 | 2026-10-08 00:48:00 | METOP-C | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 412cf49b-4856-3273-a066-776fa4ea524b | -2.6963 | -49.048599 | 2026-10-08 00:48:00 | METOP-C | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 02fdd152-528c-3d5e-b39a-239a2a1c7a95 | -2.7684 | -54.112202 | 2026-10-08 00:48:00 | METOP-C | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| ac558a8b-7714-39fc-9f73-bd421e92e258 | -6.904 | -45.904499 | 2026-10-08 00:48:00 | METOP-C | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 9ac28893-8fae-38d9-bf49-95c946b2132e | -7.2219 | -44.284901 | 2026-10-08 00:48:00 | METOP-C | ANTÔNIO ALMEIDA | PIAUÍ | Brasil | 2200806 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 7c61029b-d965-3ec5-bbea-dbd31917f938 | -2.4912 | -56.060398 | 2026-10-08 00:48:00 | METOP-C | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| b3cabfc1-cec6-308b-a033-02725bc9e4ce | -5.7426 | -53.470299 | 2026-10-08 00:48:00 | METOP-C | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| ee8ba13b-f848-3880-8782-cea158fdf3f8 | -2.5579 | -56.1735 | 2026-10-08 00:48:00 | METOP-C | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 286750e6-8338-3218-846b-0efd7bb44124 | -3.0072 | -54.0751 | 2026-10-08 00:48:00 | METOP-C | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 9fcaff8f-6f89-3ab9-97af-2d2f182d4caa | -7.3755 | -55.223999 | 2026-10-08 00:48:00 | METOP-C | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 24e7977d-afae-3de8-bb20-4804a90ed9d3 | -2.4962 | -56.1278 | 2026-10-08 00:48:00 | METOP-C | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 54ad2395-ecf2-396b-b014-5035c843baf8 | -3.2899 | -54.004601 | 2026-10-08 00:48:00 | METOP-C | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 16b25b71-55ad-373d-895a-cba573e593c9 | -2.7714 | -54.080002 | 2026-10-08 00:48:00 | METOP-C | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 569ab368-5bc4-3d61-93c0-b8aa326a9d0f | -3.0788 | -54.299301 | 2026-10-08 00:48:00 | METOP-C | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 10c220f1-5e7b-3852-8285-1ef9e3367358 | -2.5025 | -56.155899 | 2026-10-08 00:48:00 | METOP-C | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| b5519992-de80-3feb-b225-6f35635f9922 | -6.1795 | -53.445599 | 2026-10-08 00:48:00 | METOP-C | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 6e1aa45f-6a21-3326-af03-28d4aaa10c67 | -7.7547 | -54.942501 | 2026-10-08 00:48:00 | METOP-C | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 258ef16c-ffff-3b88-a64e-aad8a0972684 | -3.0302 | -54.0858 | 2026-10-08 00:48:00 | METOP-C | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 76262f54-add4-3f00-affc-09f17313999b | -6.8831 | -43.703499 | 2026-10-08 00:48:00 | METOP-C | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| c6945daf-e820-3b75-b8d0-a671e88abcb8 | -6.2221 | -52.8577 | 2026-10-08 00:48:00 | METOP-C | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 1972b73b-1faa-3b5e-8952-a8a427e87c6b | -11.8672 | -43.571499 | 2026-10-08 00:48:00 | METOP-C | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| df7c65ec-38a0-3f3e-9582-80df82a2b58c | -14.9343 | -48.101799 | 2026-10-08 00:48:00 | METOP-C | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 32f610ea-5493-322c-a020-cc11f33f7742 | -6.2204 | -52.8046 | 2026-10-08 00:48:00 | METOP-C | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| f66ecde6-a5ab-3cb2-9c0f-039812a77211 | -3.6525 | -54.2864 | 2026-10-08 00:48:00 | METOP-C | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 787feb07-dc7c-34e9-a7aa-67697a6e51da | -6.2172 | -52.881802 | 2026-10-08 00:48:00 | METOP-C | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 07b7f15c-f1d0-357b-a06a-df9d13de45bb | -4.3751 | -54.752499 | 2026-10-08 00:48:00 | METOP-C | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 8dfa94b6-a466-3741-b038-e60997ce1343 | -11.6173 | -43.688801 | 2026-10-08 00:48:00 | METOP-C | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 1170aef6-5533-3589-916e-9f833e2b95a2 | -2.7189 | -57.474499 | 2026-10-08 00:48:00 | METOP-C | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| ec70efc3-d593-32d4-94b8-8a2d4d3def59 | -3.5514 | -54.658401 | 2026-10-08 00:48:00 | METOP-C | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 6177ca20-304a-38d7-8af8-09435f7c2934 | -3.8377 | -55.972198 | 2026-10-08 00:48:00 | METOP-C | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| a99e573f-e587-348a-89bd-37788cd38bee | -2.8515 | -54.205101 | 2026-10-08 00:48:00 | METOP-C | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 319db495-b942-397c-aa8c-b0bcce506581 | -4.5224 | -54.995701 | 2026-10-08 00:48:00 | METOP-C | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| a44ac91c-d685-32cf-b3ad-8081692a5ec0 | -6.0144 | -52.759102 | 2026-10-08 00:48:00 | METOP-C | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| a2d03c44-6f82-3e36-8642-7ab2463c10ff | -3.6507 | -54.278599 | 2026-10-08 00:48:00 | METOP-C | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 3741e307-2e12-3e8b-98d9-b3bc4c2fdbdb | -2.9415 | -54.057999 | 2026-10-08 00:48:00 | METOP-C | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 32d33e66-6821-35f4-8eb6-249d36b00bc4 | -3.3464 | -50.473301 | 2026-10-08 00:48:00 | METOP-C | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 5ace297e-a53c-31ea-ada4-d703d1749830 | -10.9997 | -45.415901 | 2026-10-08 00:48:00 | METOP-C | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 760a9cfb-cb9d-387b-b860-37d997bc60a6 | -4.3593 | -43.814701 | 2026-10-08 00:48:00 | METOP-C | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| f3b4fe35-dbf9-319d-8936-eab336d1f08f | -14.23 | -48.540798 | 2026-10-08 00:48:00 | METOP-C | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 97f20144-8726-3b8f-a88d-d920b84dd9bd | -5.9595 | -55.3606 | 2026-10-08 00:48:00 | METOP-C | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| adcc6bf9-2ab1-3c91-98da-b2f824c35401 | -5.9673 | -55.349098 | 2026-10-08 00:48:00 | METOP-C | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 976efc6e-f0c8-367a-8ba8-9f5848db53ce | -14.9164 | -48.113701 | 2026-10-08 00:48:00 | METOP-C | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 435367b5-2881-3117-9206-0e5a31b53c08 | -3.1128 | -53.77 | 2026-10-08 00:48:00 | METOP-C | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 569d3e6c-92c6-3cdf-ac84-2dc2225ccf28 | -4.3653 | -54.754601 | 2026-10-08 00:48:00 | METOP-C | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| d4c3fdfd-2d52-3eaa-9814-06fb79f1c4e9 | -3.1781 | -50.548199 | 2026-10-08 00:48:00 | METOP-C | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 5eb3d0e0-a3ba-3533-a6f8-7f8bc4a247c2 | -2.221 | -53.699902 | 2026-10-08 00:48:00 | METOP-C | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 18b1e5c0-7d1a-3b40-8d82-afa1812f9977 | -2.8844 | -54.078602 | 2026-10-08 00:48:00 | METOP-C | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| a74219d2-326f-3b97-b1e2-70773b0fd5c8 | -6.5693 | -53.028 | 2026-10-08 00:48:00 | METOP-C | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 1c230245-be1f-3789-b4ef-960755a36188 | -3.0486 | -53.939899 | 2026-10-08 00:48:00 | METOP-C | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 2ff735b9-40ae-3ce0-b1aa-5ba7a624591e | -2.9271 | -54.084999 | 2026-10-08 00:48:00 | METOP-C | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 6d67a2c2-01d0-3099-98b0-428b4aec9bac | -3.0607 | -54.174702 | 2026-10-08 00:48:00 | METOP-C | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| d26c58aa-80f8-3ae4-b2fa-e566dbaac006 | -1.1104 | -54.160999 | 2026-10-08 00:48:00 | METOP-C | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 42776719-0cd4-308d-afa2-2ee99c00fbb3 | -3.0573 | -54.1595 | 2026-10-08 00:48:00 | METOP-C | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 2fc856e2-708c-3313-9dec-775133cea56e | -2.9264 | -54.172501 | 2026-10-08 00:48:00 | METOP-C | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 7d93f418-6d6d-3e47-accf-0df50b789239 | -3.5126 | -54.5322 | 2026-10-08 00:48:00 | METOP-C | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 4181c04e-0f21-3488-8f4b-583e14c4cad2 | -6.2058 | -52.876598 | 2026-10-08 00:48:00 | METOP-C | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 0bf1694f-2b1c-366b-b953-2b5adf9913c8 | -6.6367 | -43.748199 | 2026-10-08 00:48:00 | METOP-C | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 0aa1548b-d342-396a-97e8-087eb75c75b4 | -7.2293 | -55.1651 | 2026-10-08 00:48:00 | METOP-C | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 3f5a4674-aaa9-314d-b12a-99289a0e206e | -3.0886 | -54.297199 | 2026-10-08 00:48:00 | METOP-C | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 3739b836-071b-3af7-8f5c-53a455fb285b | -5.8142 | -53.834499 | 2026-10-08 00:48:00 | METOP-C | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| f30d257c-0816-3611-926c-1ba55f3ca346 | -3.0388 | -53.942101 | 2026-10-08 00:48:00 | METOP-C | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| f9e54bd4-716f-3b0d-927e-4773e9d28fd3 | -7.4631 | -47.597301 | 2026-10-08 00:48:00 | METOP-C | BARRA DO OURO | TOCANTINS | Brasil | 1703073 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 001796ba-d1f6-3a93-9edc-ce81d569ec61 | -3.4314 | -50.439301 | 2026-10-08 00:48:00 | METOP-C | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 837ad3b5-58cf-3545-8da2-2f16fa952a71 | -2.882 | -54.158401 | 2026-10-08 00:48:00 | METOP-C | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 87ca2b38-60f0-3d71-b7ca-b14afb1d2962 | -3.0222 | -53.914501 | 2026-10-08 00:48:00 | METOP-C | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 7b8b08bf-9d7b-3893-a7c3-28eca750b325 | -3.3784 | -59.592098 | 2026-10-08 00:48:00 | METOP-C | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 110b7a86-67c1-339e-8f9b-ab869ac4dbaf | -3.2801 | -54.006802 | 2026-10-08 00:48:00 | METOP-C | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 0f069b70-32a1-31b7-8ba8-f7ec43377ec4 | -2.9293 | -54.1399 | 2026-10-08 00:48:00 | METOP-C | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 40e2ade9-6cb7-3390-9ecd-4270a3cbf9e4 | -6.9555 | -45.263901 | 2026-10-08 00:48:00 | METOP-C | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 83e471b3-3388-3c77-a5cf-492026eab98a | -11.8575 | -43.574001 | 2026-10-08 00:48:00 | METOP-C | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 02c74646-7dde-3c3b-8ae7-00846721cfb4 | -2.9685 | -54.131199 | 2026-10-08 00:48:00 | METOP-C | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 89627a33-03cc-332d-b2a8-233630767437 | -6.0134 | -47.403301 | 2026-10-08 00:48:00 | METOP-C | RIBAMAR FIQUENE | MARANHÃO | Brasil | 2109551 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 82c24f17-3f53-32fb-bc73-2fb88ef6ef75 | -3.225 | -53.900799 | 2026-10-08 00:48:00 | METOP-C | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 328e6e2a-22a0-36c3-a7ac-91ef0ce22598 | -9.8334 | -44.7896 | 2026-10-08 00:48:00 | METOP-C | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 3d6974cd-e8ce-34c4-a17d-e67ee3520680 | -6.32 | -43.340401 | 2026-10-08 00:48:00 | METOP-C | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 1987b33d-0101-3b74-90ff-ba3733526ef0 | -1.4647 | -54.762901 | 2026-10-08 00:48:00 | METOP-C | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| b575c6a7-4d9e-325d-b909-50587e3065f9 | -11.2404 | -44.878399 | 2026-10-08 00:48:00 | METOP-C | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 4d9e74d6-ad8f-3936-94b7-684066ef2d12 | -11.6398 | -43.696201 | 2026-10-08 00:48:00 | METOP-C | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 55451039-881a-358d-950c-252814e9bbe2 | -10.5016 | -47.299801 | 2026-10-08 00:48:00 | METOP-C | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 4e20ec6d-1834-3a00-a35a-a08893a8198a | -2.9391 | -54.137798 | 2026-10-08 00:48:00 | METOP-C | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 0105caa7-fb44-3576-940b-435301b7c566 | -3.5533 | -54.666401 | 2026-10-08 00:48:00 | METOP-C | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| e1aeb113-8e54-329f-8638-1ea3ad583989 | -3.2655 | -54.033699 | 2026-10-08 00:48:00 | METOP-C | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 51c34e6f-7c51-33f7-9081-037a4086e9de | -7.8901 | -54.718601 | 2026-10-08 00:48:00 | METOP-C | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| ccb18a85-be21-3cc8-97cf-c55d0d4cb0cb | -8.7402 | -45.176399 | 2026-10-08 00:48:00 | METOP-C | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| ec700f2b-fa1a-364f-857d-d50a037d083d | 3.5388 | -51.2896 | 2026-10-08 00:48:00 | METOP-C | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | nan |
| ac5325cf-8b4a-3e90-94b6-49ab564ee12c | -6.441 | -55.0326 | 2026-10-08 00:48:00 | METOP-C | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 350efc81-dce0-3e4b-a8ae-d83be9f9c57b | -3.0238 | -54.1031 | 2026-10-08 00:48:00 | METOP-C | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 96ecf5ea-327c-3d2a-97ef-c10e3714bb03 | -10.4431 | -47.271198 | 2026-10-08 00:48:00 | METOP-C | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 44b3af0e-a25f-3940-923e-e6f839cbb20a | -5.6821 | -53.4757 | 2026-10-08 00:48:00 | METOP-C | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 4e0d6a8b-4715-353f-96c5-dc936ea9374b | -3.0735 | -54.276199 | 2026-10-08 00:48:00 | METOP-C | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 731eb230-18de-38f3-97d8-a52fb7d78e49 | -3.2916 | -54.0121 | 2026-10-08 00:48:00 | METOP-C | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 17d1d56f-45f7-34a1-ad47-3d4bdea88cbc | -6.0602 | -44.0425 | 2026-10-08 00:48:00 | METOP-C | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| b2d4897b-2370-3219-8c37-814c8ea20b7c | -3.2207 | -53.9725 | 2026-10-08 00:48:00 | METOP-C | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| fb6199ee-3fdb-3d08-a63f-53cd3d95ce9b | -3.2991 | -54.680199 | 2026-10-08 00:48:00 | METOP-C | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| aa77e40e-1fb6-35e5-81de-361f5dc5c516 | -9.2824 | -50.314701 | 2026-10-08 00:48:00 | METOP-C | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 8d52ae8c-ecc3-33ce-9c67-2cbbf5fc6c50 | -6.2204 | -52.850399 | 2026-10-08 00:48:00 | METOP-C | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 075ed254-5c80-35ac-b337-cf708583982c | -2.9824 | -54.056801 | 2026-10-08 00:48:00 | METOP-C | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |


[Clique aqui para ver as próximas entradas](README27.md)
