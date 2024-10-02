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

## Dados Diários - Página 126

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 5bac540c-9a08-33ba-bafe-c705aa63116d | -17.03053 | -58.04007 | 2024-10-02 04:51:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.7 |
| 121868f8-8712-3fa8-9532-a95ce6f68b18 | -17.00456 | -57.96282 | 2024-10-02 04:51:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 5.9 |
| ba20ac5d-18c9-3749-ab98-f467d6ee33c2 | -17.00367 | -57.96779 | 2024-10-02 04:51:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 4.3 |
| a37f5572-2c8f-3181-acd6-6c1963b00e1c | -16.99983 | -57.96705 | 2024-10-02 04:51:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 4.3 |
| aae9eb30-8290-36ae-82b0-5b821c72667a | -16.91315 | -57.7103 | 2024-10-02 04:51:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 5.4 |
| 9d1659e9-e6c9-359e-873f-929e54b5bcda | -16.91023 | -57.70477 | 2024-10-02 04:51:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 11.7 |
| 097d8851-f179-30f3-b6c6-e24c8640cb74 | -16.90936 | -57.70958 | 2024-10-02 04:51:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 8.9 |
| 99d9684f-13e8-3f74-86c5-c1657870c0a2 | -16.90558 | -57.70886 | 2024-10-02 04:51:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 8.9 |
| e696cd4b-e951-350f-9545-3a3b029fa3dd | -16.90471 | -57.71368 | 2024-10-02 04:51:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 8.9 |
| 82917bb6-2636-3300-9520-1f07ea549f97 | -16.90298 | -57.72333 | 2024-10-02 04:51:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 6.1 |
| b6324fba-2f8a-36e8-91d5-f6176f364a9e | -16.9018 | -57.70814 | 2024-10-02 04:51:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 15.7 |
| 37219846-a907-34a8-82de-dcb351aea3a9 | -16.90093 | -57.71296 | 2024-10-02 04:51:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 15.7 |
| d49df364-31c6-3aa4-8627-6982489e42d0 | -16.89919 | -57.72262 | 2024-10-02 04:51:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 4.7 |
| c1a983cf-d9b0-34bc-b26b-2eff2686cc29 | -16.89801 | -57.70742 | 2024-10-02 04:51:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 15.7 |
| 8d975637-f7b9-3981-9128-0009d28b35da | -16.89714 | -57.71225 | 2024-10-02 04:51:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 15.7 |
| c63b6999-86db-368b-b45d-53b43981f782 | -16.89627 | -57.71707 | 2024-10-02 04:51:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 4.7 |
| c053bc80-b080-3467-bb8f-0fea7f50db2f | -16.8954 | -57.72189 | 2024-10-02 04:51:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 4.7 |
| 4420b4ad-f17e-37c0-a0fa-04a10165cc78 | -16.89423 | -57.70671 | 2024-10-02 04:51:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 6.0 |
| f4d0023b-4016-33c2-b47a-fa20faba962d | -16.89336 | -57.71152 | 2024-10-02 04:51:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 6.0 |
| 16ca4ac4-9bfb-3e32-9481-df7429849a1f | -16.89248 | -57.71635 | 2024-10-02 04:51:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 4.4 |
| 8061b44f-1ec2-3427-964e-2f9b2f1cf298 | -16.89044 | -57.70599 | 2024-10-02 04:51:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 6.0 |
| 2c977166-15b7-3384-8837-d6c82133d6f7 | -16.88957 | -57.71081 | 2024-10-02 04:51:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 6.0 |
| 9c46cfd5-198f-3835-a1bc-dc53ab018d03 | -16.8887 | -57.71563 | 2024-10-02 04:51:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 4.4 |
| e17e5d9f-7f56-3f8a-aaeb-e6b051893b9e | -16.8867 | -57.70702 | 2024-10-02 04:51:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.6 |
| 566b5821-1f59-30b8-80cf-57ffa085056b | -16.88666 | -57.70527 | 2024-10-02 04:51:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.3 |
| 646a80d1-1c3b-39c6-b547-c881886095ab | -16.88491 | -57.71491 | 2024-10-02 04:51:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.9 |
| ea12b641-05d8-3429-9d55-1d85964d8375 | -16.86467 | -57.78806 | 2024-10-02 04:51:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.1 |
| 8f7e4d13-0f65-33c4-be67-3dbed27a96ab | -16.86413 | -57.78613 | 2024-10-02 04:51:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.6 |
| 59b61001-fa86-37b2-8a27-15f984df755c | -16.86049 | -57.76712 | 2024-10-02 04:51:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.3 |
| 7cb277df-14a3-3baf-a77c-a26a90997c89 | -16.85755 | -57.76152 | 2024-10-02 04:51:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.3 |
| 83769b16-edd1-3785-b270-f732077ce957 | -16.85289 | -57.76566 | 2024-10-02 04:51:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.0 |
| 66b26d5f-e083-3e46-bf89-d7d673b87719 | -16.84995 | -57.76007 | 2024-10-02 04:51:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.0 |
| 2ff67232-ffc1-3291-8cd0-5992bf6c3689 | -16.84909 | -57.76493 | 2024-10-02 04:51:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.0 |
| 133fa6fb-67db-30df-a815-9ae04895f8aa | -19.10711 | -57.48875 | 2024-10-02 04:51:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.7 |
| a133fb38-6a7a-350e-874a-18c01e73fd87 | -17.30735 | -57.46636 | 2024-10-02 04:51:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.1 |
| a7e34c09-662b-3eef-869f-0a7fd99609c2 | -17.21091 | -57.37302 | 2024-10-02 04:51:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.7 |
| 34c2308a-b5af-3f2e-8f1f-0a3e9e38cbd9 | -17.2101 | -57.37762 | 2024-10-02 04:51:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.7 |
| 56211e01-3b71-3e9d-a731-d2e2b31c1c98 | -17.20721 | -57.37233 | 2024-10-02 04:51:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.7 |
| c0144bdb-139c-3d28-8a95-45e199753d59 | -17.2064 | -57.37693 | 2024-10-02 04:51:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.7 |
| 57e5e9bf-3009-331e-aa15-ce1519761fd3 | -17.20433 | -57.36703 | 2024-10-02 04:51:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.8 |
| 34f6cd1b-3275-3d76-867c-1d76f27e6d8b | -17.20351 | -57.37163 | 2024-10-02 04:51:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 4.4 |
| cd8e151b-cd66-320c-8fc9-66d06608fc43 | -17.2027 | -57.37622 | 2024-10-02 04:51:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 4.4 |
| 18bae784-2031-3629-a329-78e32545bce6 | -17.19981 | -57.37092 | 2024-10-02 04:51:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 4.4 |
| c5091f45-dc6a-3696-9500-422e85ae70a7 | -17.199 | -57.37552 | 2024-10-02 04:51:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 4.4 |
| 1a5df120-47d0-3e3b-a96e-06bb6e2b3586 | -17.19736 | -57.38474 | 2024-10-02 04:51:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.8 |
| eb4e8abc-ebb3-3ba0-89fe-fae8eec9fb6a | -17.19448 | -57.37943 | 2024-10-02 04:51:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.7 |
| 9166cd0b-458a-3246-a5aa-34293622a6c7 | -17.19366 | -57.38404 | 2024-10-02 04:51:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.7 |
| 93e9dac5-7e39-3eca-b260-883cb2fe594f | -17.18914 | -57.38795 | 2024-10-02 04:51:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 7.5 |
| 4b121bff-dbd1-3488-90ea-fcf7bfc4db5b | -18.71915 | -57.33959 | 2024-10-02 04:51:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.4 |
| 9e856c80-c841-3257-965b-e4cc4c9fea13 | -18.71632 | -57.33448 | 2024-10-02 04:51:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.0 |
| 4727231a-34dc-320b-b159-65ad15e56286 | -18.71553 | -57.33889 | 2024-10-02 04:51:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.9 |
| 67015ec2-810b-3a5a-9078-a8399d0d40bf | -18.70294 | -57.30456 | 2024-10-02 04:51:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.4 |
| 4a1086c8-4fb2-39b4-89d1-8b802b226431 | -18.70216 | -57.30896 | 2024-10-02 04:51:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.9 |
| 5335334e-1b36-33c4-80af-e9c1c84b6b75 | -18.70184 | -57.33171 | 2024-10-02 04:51:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.1 |
| a2220327-aceb-3e3c-a2c2-0337df42a815 | -18.70137 | -57.31337 | 2024-10-02 04:51:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.9 |
| 36c2b025-17a5-38e4-87c7-b1cf6e6e1016 | -18.70098 | -57.31063 | 2024-10-02 04:51:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.8 |
| b4b89ec4-5c8a-308f-9589-602a1f8332fa | -18.70022 | -57.31504 | 2024-10-02 04:51:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.8 |
| ab43385f-fcbb-3fbd-8098-ffc2a0a671bb | -18.69776 | -57.31267 | 2024-10-02 04:51:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 10.8 |
| a6a50b4f-1646-36b5-88fb-676e79cb7b27 | -18.69737 | -57.30993 | 2024-10-02 04:51:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.8 |
| 3080c8bb-76eb-3f06-9dbb-35116736dbe5 | -18.69697 | -57.31708 | 2024-10-02 04:51:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.3 |
| 09af2844-19ab-3eb7-afe9-8cad45233705 | -18.69661 | -57.31434 | 2024-10-02 04:51:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.8 |
| 3ad50e69-734e-3014-8b19-966e1dbe20e4 | -18.69618 | -57.3215 | 2024-10-02 04:51:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.3 |
| 235f7db8-240f-3518-baf6-6f453c58f2f6 | -18.69508 | -57.32318 | 2024-10-02 04:51:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.8 |
| e658abe6-05db-35c9-8e7d-e2cbf9b1c94b | -18.6946 | -57.33033 | 2024-10-02 04:51:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.6 |
| a4c2ff8a-fb63-3d8a-b2be-2842fb4009f5 | -18.69382 | -57.33474 | 2024-10-02 04:51:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.9 |
| 29697b53-ec1c-3c95-9c37-479505ed6268 | -18.69355 | -57.33203 | 2024-10-02 04:51:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 5.4 |
| aa8d375a-8d16-397d-8463-5c27294bd282 | -18.69278 | -57.33644 | 2024-10-02 04:51:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.7 |
| 876258e8-f4ff-3863-a6a9-271fd8ad79c7 | -19.11727 | -57.47378 | 2024-10-02 04:51:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 5.0 |
| a37309f0-d41c-3b96-9ced-47be4823bee5 | -19.11467 | -57.50937 | 2024-10-02 04:51:00 | NOAA-21 | LADÁRIO | MATO GROSSO DO SUL | Brasil | 5005202 | 50 | 33 | nan | nan | nan | Pantanal | 3.7 |
| 2eb007b5-0316-36d4-9d0a-94a26f55c8b8 | -19.10631 | -57.49049 | 2024-10-02 04:51:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 5.0 |
| 5cca01bf-ec12-3b76-bcc6-beb72e81de03 | -17.0402 | -58.39381 | 2024-10-02 04:51:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 12.0 |
| 539fb38f-6eba-3d3e-9ea2-798429ceeccd | -25.82977 | -50.25494 | 2024-10-02 04:53:00 | NOAA-21 | SÃO JOÃO DO TRIUNFO | PARANÁ | Brasil | 4125100 | 41 | 33 | nan | nan | nan | Mata Atlântica | 0.4 |
| 8535267f-d6f7-3840-a0dd-53cad0c6d77b | -25.82529 | -50.25825 | 2024-10-02 04:53:00 | NOAA-21 | SÃO JOÃO DO TRIUNFO | PARANÁ | Brasil | 4125100 | 41 | 33 | nan | nan | nan | Mata Atlântica | 3.6 |
| 72178b33-0297-3d7d-879f-6913cd623e8e | -26.74751 | -51.72261 | 2024-10-02 04:53:00 | NOAA-21 | ÁGUA DOCE | SANTA CATARINA | Brasil | 4200408 | 42 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 39ee35cf-14b1-3c61-b3f1-57c096091f5c | -26.49378 | -51.65154 | 2024-10-02 04:53:00 | NOAA-21 | PALMAS | PARANÁ | Brasil | 4117602 | 41 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 006695a7-ce06-3879-9e30-bd76e6cf0d3a | -26.49315 | -51.65648 | 2024-10-02 04:53:00 | NOAA-21 | PALMAS | PARANÁ | Brasil | 4117602 | 41 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 7b5bd785-f774-334a-a9d2-90a15c6e602c | -25.61162 | -51.3507 | 2024-10-02 04:53:00 | NOAA-21 | GUARAPUAVA | PARANÁ | Brasil | 4109401 | 41 | 33 | nan | nan | nan | Mata Atlântica | 2.8 |
| 15864389-f3b3-307e-8dea-5acd0a1a54cb | -25.60969 | -52.42731 | 2024-10-02 04:53:00 | NOAA-21 | PORTO BARREIRO | PARANÁ | Brasil | 4120150 | 41 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| ae2e80b5-0239-3686-abad-3ccf3aa3a784 | -26.75438 | -51.72866 | 2024-10-02 04:53:00 | NOAA-21 | ÁGUA DOCE | SANTA CATARINA | Brasil | 4200408 | 42 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 6a4287aa-aa86-3c70-96b7-be8db596297f | -16.59 | -58.26 | 2024-10-02 05:03:52 | MSG-03 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 7aea0c9d-6a4f-3460-b86c-adf8372d7276 | -3.47137 | -43.35424 | 2024-10-02 05:08:00 | NPP-375D | URBANO SANTOS | MARANHÃO | Brasil | 2112605 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 4b76172e-8f08-3b0e-a51c-2823d1fae706 | -3.47041 | -43.3608 | 2024-10-02 05:08:00 | NPP-375D | URBANO SANTOS | MARANHÃO | Brasil | 2112605 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 4e9361bf-672b-33bb-93dd-55388ca7ddba | -1.01391 | -46.78207 | 2024-10-02 05:08:00 | NPP-375D | BRAGANÇA | PARÁ | Brasil | 1501709 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 799da7fa-2fb2-30d8-ad4c-2977ab2230fb | -1.01337 | -46.78553 | 2024-10-02 05:08:00 | NPP-375D | BRAGANÇA | PARÁ | Brasil | 1501709 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| ec42648a-b816-3f4a-8d34-9255b09a7823 | -1.00847 | -46.78123 | 2024-10-02 05:08:00 | NPP-375D | BRAGANÇA | PARÁ | Brasil | 1501709 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 3ea525f2-0cbb-3a1b-b0cf-93913b5c81b3 | -3.21654 | -46.78236 | 2024-10-02 05:08:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 3ae57975-6990-3cfa-a5f3-455918aaa42c | -3.21597 | -46.78609 | 2024-10-02 05:08:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 8.7 |
| dc43aa5f-38cf-38c6-8925-c0366dd8944b | -3.21468 | -46.78069 | 2024-10-02 05:08:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 8aff26b1-6de0-399a-a018-3b9972406867 | -3.21414 | -46.78444 | 2024-10-02 05:08:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| b47232cb-90b5-36de-a504-fae6fa32c45f | -3.2136 | -46.78818 | 2024-10-02 05:08:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 1879bc5d-5899-3281-8ee3-3dfdbdb87557 | -2.90804 | -47.11121 | 2024-10-02 05:08:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 841dcb02-afe0-3d56-8e7f-59e08d2e430d | -2.62433 | -46.90901 | 2024-10-02 05:08:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 84a45281-bebb-3666-92b6-d6f4628b1321 | -2.61883 | -46.90803 | 2024-10-02 05:08:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| a61a7143-b6a7-3937-b871-0b323ca51742 | -2.61827 | -46.91172 | 2024-10-02 05:08:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| a8583d60-8faa-37ac-b1e0-083fd4df7767 | -3.70018 | -47.59976 | 2024-10-02 05:08:00 | NPP-375D | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| dbebf15a-ab86-34f8-bf9d-76bf04b95a9a | -3.69969 | -47.6031 | 2024-10-02 05:08:00 | NPP-375D | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| b54e3ad6-d885-3698-996d-52d09a0738dc | -3.46631 | -47.66332 | 2024-10-02 05:08:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 02b70603-5dc1-3418-894a-31b533614c94 | -3.46581 | -47.66666 | 2024-10-02 05:08:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 4ed8f5b6-035f-3920-9930-724e2a9e6c06 | -2.60198 | -48.03468 | 2024-10-02 05:08:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 112cdbe3-dc9b-3822-83f3-71fec4f94f3e | -2.60152 | -48.03765 | 2024-10-02 05:08:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |


[Clique aqui para ver as próximas entradas](README127.md)
