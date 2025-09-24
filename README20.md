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

## Dados Diários - Página 20

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 8cf48124-688a-3605-8d49-6512d9558c1c | -17.94726 | -55.85516 | 2025-09-24 05:44:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.9 |
| ffa92e33-58d7-36e9-b235-f03d8d07d603 | -15.96211 | -59.49281 | 2025-09-24 05:44:00 | NOAA-20 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 04e397c4-14c1-3543-b7d1-b9f648dfd837 | -21.00348 | -47.37946 | 2025-09-24 05:44:00 | AQUA_M-M | ALTINÓPOLIS | SÃO PAULO | Brasil | 3501004 | 35 | 33 | nan | nan | nan | Cerrado | 9.4 |
| 7dda5dc8-1da6-3c86-9efe-bee0af447526 | -15.77849 | -59.48812 | 2025-09-24 05:44:00 | NOAA-20 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 1101e24c-9df4-3cbd-937a-0b6903523601 | -15.9011 | -59.35847 | 2025-09-24 05:44:00 | NOAA-20 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 506070c1-295f-384e-b9d6-9f323ce246e6 | -15.96695 | -59.49358 | 2025-09-24 05:44:00 | NOAA-20 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| b014ed6f-a83f-3981-8e1e-34ec9bb4ea4a | -17.95698 | -55.85889 | 2025-09-24 05:44:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 0.9 |
| aa8ebe00-5e97-3740-873d-4eb02e280967 | -17.9444 | -55.85757 | 2025-09-24 05:44:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.7 |
| 94366e2b-f402-345e-a246-89e3e9b962c8 | -15.89622 | -59.3577 | 2025-09-24 05:44:00 | NOAA-20 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| e7b3bae6-6c74-3789-8369-005b2f2f9dd6 | -15.77973 | -59.47785 | 2025-09-24 05:44:00 | NOAA-20 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 3.1 |
| d7ecf4c9-c7e6-3cf6-9788-8c98ea8cf3e2 | -15.83888 | -59.59071 | 2025-09-24 05:44:00 | NOAA-20 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| c3dc36bc-65d1-33cc-b2f7-2a90a92dbaab | -15.97297 | -59.48447 | 2025-09-24 05:44:00 | NOAA-20 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 3.8 |
| a7a3a9b7-d75e-38c1-8c86-33d22ed08240 | -15.83343 | -59.59543 | 2025-09-24 05:44:00 | NOAA-20 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 462b5008-d364-3b6e-92d1-7c2435d8003d | -22.6084 | -49.0117 | 2025-09-24 06:40:00 | GOES-19 | AGUDOS | SÃO PAULO | Brasil | 3500709 | 35 | 33 | nan | nan | nan | Cerrado | 60.5 |
| 3ca682f4-3b57-3489-bf64-8460ab71e9c8 | -9.44538 | -67.13961 | 2025-09-24 07:18:00 | AQUA_M-M | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 3.6 |
| bffde6fa-2ef8-3c46-a88e-4f6cc45f65c2 | -15.7835 | -59.4853 | 2025-09-24 08:40:00 | GOES-19 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 63.7 |
| 2c817fe1-dc03-3de3-87b2-7b4a627518d2 | -15.7835 | -59.4853 | 2025-09-24 08:50:00 | GOES-19 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 58.4 |
| ed512037-7382-3a2e-b913-5da4bcd2ae51 | -9.7225 | -46.696 | 2025-09-24 09:00:00 | GOES-19 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 576.0 |
| 3472a349-7ffa-3ee0-8abc-8ec8d40c4fe1 | -9.7222 | -46.7184 | 2025-09-24 09:00:00 | GOES-19 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 234.3 |
| 2ac26b59-6ff2-3601-a987-b1bbc0477366 | -9.7036 | -46.6981 | 2025-09-24 09:00:00 | GOES-19 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 169.2 |
| 04edaa88-02f7-3ba1-a82a-ce2f936d0dc0 | -15.7835 | -59.4853 | 2025-09-24 09:00:00 | GOES-19 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 54.8 |
| 1fcb356b-0f17-31b6-9d11-a00b2f622cfe | -9.7225 | -46.696 | 2025-09-24 09:10:00 | GOES-19 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 399.9 |
| 7e9dce83-c73f-38f6-ba44-319e8371819f | -9.7222 | -46.7184 | 2025-09-24 09:10:00 | GOES-19 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 425.2 |
| a18d5a57-d5b8-39dd-afe2-72f389a49282 | -9.7225 | -46.696 | 2025-09-24 09:20:00 | GOES-19 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 191.5 |
| db665c9a-5376-3eec-8bb8-0ddd0518e460 | -9.7032 | -46.7205 | 2025-09-24 09:20:00 | GOES-19 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 183.2 |
| 4bf5c97f-7d7e-397c-834b-bffeacf905d5 | -9.7222 | -46.7184 | 2025-09-24 09:20:00 | GOES-19 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 317.5 |
| 6284858e-fc47-3453-b6a8-9f02268490fc | -9.7219 | -46.7407 | 2025-09-24 09:30:00 | GOES-19 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 191.5 |
| 1fcb6c41-bf18-3153-8b6f-9bc6bf3f5066 | -9.7222 | -46.7184 | 2025-09-24 09:30:00 | GOES-19 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 264.0 |
| 25d9c485-ea2d-32eb-bf2c-b618ebc25303 | -9.7032 | -46.7205 | 2025-09-24 09:30:00 | GOES-19 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 243.6 |
| ab852331-b7f4-3a9e-82ec-8d8c4a556e09 | -9.7029 | -46.7429 | 2025-09-24 09:30:00 | GOES-19 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 177.0 |
| 71c0cba5-9584-3ec9-8153-4b18ac8d4bed | -9.7225 | -46.696 | 2025-09-24 10:20:00 | GOES-19 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 122.6 |
| d6d0763b-03fa-3e89-9b26-d0952e5576a0 | -9.7222 | -46.7184 | 2025-09-24 10:20:00 | GOES-19 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 140.9 |
| 109f6fbc-d796-3a6a-b85b-81607804d856 | -9.7219 | -46.7407 | 2025-09-24 10:30:00 | GOES-19 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 167.3 |
| a53d5db1-1874-3659-8547-57db9dde1730 | -9.7414 | -46.6938 | 2025-09-24 10:30:00 | GOES-19 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 120.6 |
| 7ded5e50-8ea3-3963-ab3f-8976f3362316 | -9.7222 | -46.7184 | 2025-09-24 10:30:00 | GOES-19 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 609.4 |
| 62b86936-c4ad-3b5b-b3dd-ba4d0fc3a99c | -9.7411 | -46.7162 | 2025-09-24 10:30:00 | GOES-19 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 238.1 |
| cc97b4c6-7421-3089-a101-e4f50a894511 | -9.7219 | -46.7407 | 2025-09-24 10:40:00 | GOES-19 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 97.2 |
| d0adc605-9802-3181-a935-5722d0563d20 | -9.7222 | -46.7184 | 2025-09-24 10:40:00 | GOES-19 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 157.1 |
| a4011cf0-b859-34d4-9cfb-8676e2702582 | -9.9555 | -46.2876 | 2025-09-24 11:00:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 100.8 |
| 4f67fc70-a290-31e0-95eb-d8f239df9eb9 | -8.5176 | -44.9977 | 2025-09-24 11:00:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 99.9 |
| 7abe405a-b627-32cf-b875-b77dc643f367 | -9.9555 | -46.2876 | 2025-09-24 11:10:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 87.3 |
| 08537e34-e218-3118-97be-60fe8c964065 | -8.2611 | -44.4052 | 2025-09-24 11:20:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 99.6 |
| 6a3f33fd-8a61-315e-a33e-ad6d5b5d9a6f | -8.2614 | -44.3821 | 2025-09-24 11:20:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 93.3 |
| 3bfd3dce-4362-3162-8c98-54a53e447567 | -8.5176 | -44.9977 | 2025-09-24 11:30:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 92.6 |
| 92263345-b8bb-386b-aa4b-0797642b47b5 | -7.6486 | -45.2218 | 2025-09-24 11:30:00 | GOES-19 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 127.5 |
| c1d0ffce-bde3-33fd-8be1-1e665889eabd | -10.3191 | -46.0632 | 2025-09-24 11:30:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 125.9 |
| e1f7958c-1ac3-3edc-a670-ae8389d656dd | -8.3139 | -46.2183 | 2025-09-24 11:40:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 103.6 |
| bcd50cb2-82df-3b94-a1c5-c8d386f4d17a | -8.2614 | -44.3821 | 2025-09-24 11:40:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 78.4 |
| 5cdfc9f8-24ba-3f33-bd33-9329436cf098 | -8.2611 | -44.4052 | 2025-09-24 11:40:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 102.9 |
| 7279d5db-58d8-30f9-9f14-36d15e805ba3 | -8.3139 | -46.2183 | 2025-09-24 11:50:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 107.9 |
| 84942c00-354d-38c1-bfcb-0dd6398ec63f | -8.2611 | -44.4052 | 2025-09-24 11:50:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 103.1 |
| 243108f5-93be-3201-8ad2-849254e995df | -8.2614 | -44.3821 | 2025-09-24 11:50:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 82.3 |
| f49b8d29-3391-38a5-a931-35006b23dc21 | -8.2614 | -44.3821 | 2025-09-24 12:00:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 100.9 |
| 107710a6-dedb-3506-97e0-7ef423415f26 | -8.3139 | -46.2183 | 2025-09-24 12:00:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 94.9 |
| 034b6d79-9bab-345b-9f7b-81230091cc73 | -9.5595 | -47.5581 | 2025-09-24 12:00:00 | GOES-19 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 89.3 |
| 930d54a8-db18-3515-8540-d3e4eede6ee5 | -8.2611 | -44.4052 | 2025-09-24 12:00:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 171.8 |
| dbd3d97e-8f18-3d54-b3fc-d827143165d3 | -9.5781 | -47.5782 | 2025-09-24 12:10:00 | GOES-19 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 112.5 |
| dec325a2-c642-3200-b08f-25b2cfd5edb4 | -8.3139 | -46.2183 | 2025-09-24 12:10:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 138.7 |
| 082c7769-fe33-3bfb-9e5d-2003ba00e446 | -8.2611 | -44.4052 | 2025-09-24 12:10:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 274.0 |
| caaa435f-1670-3cc7-a2bc-87987c4f5ad7 | -8.2614 | -44.3821 | 2025-09-24 12:10:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 119.5 |
| 42fffcd6-1205-3d69-8fb6-72efea1d61d7 | -9.5595 | -47.5581 | 2025-09-24 12:10:00 | GOES-19 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 93.0 |
| 2c59c6d5-6270-3a5f-b4d1-9c3599b8a63b | -0.66197 | -47.29436 | 2025-09-24 12:14:00 | TERRA_M-T | SALINÓPOLIS | PARÁ | Brasil | 1506203 | 15 | 33 | nan | nan | nan | Amazônia | 11.3 |
| a7071352-bc36-39f1-971d-edbe509679f5 | -2.16023 | -46.11379 | 2025-09-24 12:14:00 | TERRA_M-T | MARACAÇUMÉ | MARANHÃO | Brasil | 2106326 | 21 | 33 | nan | nan | nan | Amazônia | 6.8 |
| bd22aa02-6664-3f43-b332-e5a3393e2b06 | -2.97294 | -43.50212 | 2025-09-24 12:14:00 | TERRA_M-T | HUMBERTO DE CAMPOS | MARANHÃO | Brasil | 2105005 | 21 | 33 | nan | nan | nan | Cerrado | 7.2 |
| 98f8e3e1-b34c-367e-947f-845d1b5dc92c | 0.93481 | -51.19002 | 2025-09-24 12:14:00 | TERRA_M-T | FERREIRA GOMES | AMAPÁ | Brasil | 1600238 | 16 | 33 | nan | nan | nan | Amazônia | 22.1 |
| aa5979d1-6902-396f-880e-e1772b3d211e | -1.13683 | -46.36282 | 2025-09-24 12:14:00 | TERRA_M-T | AUGUSTO CORRÊA | PARÁ | Brasil | 1500909 | 15 | 33 | nan | nan | nan | Amazônia | 5.5 |
| cf130b05-6f76-3117-8623-353327848e76 | -3.86488 | -40.35586 | 2025-09-24 12:17:00 | TERRA_M-T | FORQUILHA | CEARÁ | Brasil | 2304350 | 23 | 33 | nan | nan | nan | Caatinga | 42.9 |
| 54c51b62-f480-325b-9f9c-ebc7275bf47f | -4.23454 | -43.69741 | 2025-09-24 12:17:00 | TERRA_M-T | TIMBIRAS | MARANHÃO | Brasil | 2112100 | 21 | 33 | nan | nan | nan | Cerrado | 9.1 |
| 804aefca-f872-3899-a97d-7b0df2a920a7 | -8.00808 | -45.7056 | 2025-09-24 12:17:00 | TERRA_M-T | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 13.0 |
| 5c9cddbd-089f-333f-8f93-f0f308351e30 | -8.31349 | -46.22201 | 2025-09-24 12:17:00 | TERRA_M-T | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 29.0 |
| ca3031a3-6a95-3bf6-9cc3-85dbe2e037be | -7.55832 | -44.35619 | 2025-09-24 12:17:00 | TERRA_M-T | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 13.2 |
| 111cfb9e-b586-3e3b-8789-762b2d7a0787 | -7.55974 | -44.34568 | 2025-09-24 12:17:00 | TERRA_M-T | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 34.1 |
| b819dd96-ae1c-3166-8cd6-3687ce0f51e8 | -8.26384 | -44.4083 | 2025-09-24 12:17:00 | TERRA_M-T | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 457.7 |
| f1683e45-a38d-3683-9ab9-513af86f9302 | -8.33606 | -44.93644 | 2025-09-24 12:17:00 | TERRA_M-T | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 10.9 |
| f2cec8dd-3f80-3599-96db-990b9ea989e5 | -10.58876 | -44.06524 | 2025-09-24 12:17:00 | TERRA_M-T | BURITIRAMA | BAHIA | Brasil | 2904753 | 29 | 33 | nan | nan | nan | Cerrado | 12.7 |
| e0746068-fbce-3357-aa60-e23f58811eaf | -8.52687 | -45.0261 | 2025-09-24 12:17:00 | TERRA_M-T | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 32.2 |
| ecc1e035-a2e6-3016-b92f-7928d359979b | -5.5184 | -43.87236 | 2025-09-24 12:17:00 | TERRA_M-T | GOVERNADOR EUGÊNIO BARROS | MARANHÃO | Brasil | 2104602 | 21 | 33 | nan | nan | nan | Cerrado | 14.5 |
| 2958f6fa-7be1-3722-be8b-6c7297b33480 | -3.83816 | -41.6928 | 2025-09-24 12:17:00 | TERRA_M-T | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 15.0 |
| 5658b932-ed66-39dd-bdda-544ef9bf92c3 | -8.50562 | -46.88013 | 2025-09-24 12:17:00 | TERRA_M-T | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 26.5 |
| 4b249db4-7ab8-3836-869d-5c074255ab59 | -8.52029 | -45.00472 | 2025-09-24 12:17:00 | TERRA_M-T | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 26.7 |
| feb72a37-43fc-3bba-a35a-575b18c4e007 | -8.84288 | -46.1878 | 2025-09-24 12:17:00 | TERRA_M-T | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 24.6 |
| 9f64aeae-2510-3464-9533-874936916874 | -5.22055 | -43.72053 | 2025-09-24 12:17:00 | TERRA_M-T | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 94.3 |
| a2b9b5d6-929f-39d4-9bac-b0753a260dd1 | -8.5189 | -45.01479 | 2025-09-24 12:17:00 | TERRA_M-T | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 19.7 |
| c6d30bc7-993a-3873-a07e-d1f9ff811b86 | -9.73527 | -46.65913 | 2025-09-24 12:17:00 | TERRA_M-T | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 5.1 |
| e4935d15-ac81-3580-adab-f579e1f40668 | -9.58737 | -47.56833 | 2025-09-24 12:17:00 | TERRA_M-T | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 88.9 |
| ea766c89-95ef-3683-81ad-2a05c25a708f | -6.53157 | -44.21845 | 2025-09-24 12:17:00 | TERRA_M-T | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 13.8 |
| 3833416f-de3e-3510-92e9-ae0b4b87e797 | -9.5673 | -47.56844 | 2025-09-24 12:17:00 | TERRA_M-T | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 20.4 |
| ebfe225d-06cd-3953-90df-33017fa41f73 | -9.05093 | -46.66932 | 2025-09-24 12:17:00 | TERRA_M-T | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 49.6 |
| a86d8e2d-3c23-3ce9-a2fa-4663a3fd0f63 | -3.31431 | -48.72221 | 2025-09-24 12:17:00 | TERRA_M-T | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 9.7 |
| ec8d44a3-b327-3bed-82bb-8f6044e7e967 | -8.25565 | -46.36449 | 2025-09-24 12:17:00 | TERRA_M-T | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 8.1 |
| e37a662f-3450-39c8-a341-5261fa27a85f | -7.38448 | -47.04495 | 2025-09-24 12:17:00 | TERRA_M-T | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 14.6 |
| 6ef7650d-2b00-3e6e-ba06-6ebd6d6cdd47 | -4.78333 | -40.82978 | 2025-09-24 12:17:00 | TERRA_M-T | ARARENDÁ | CEARÁ | Brasil | 2301257 | 23 | 33 | nan | nan | nan | Caatinga | 19.6 |
| 674124a1-678a-3a6b-8e20-652c58816cc8 | -8.6776 | -44.00357 | 2025-09-24 12:17:00 | TERRA_M-T | CRISTINO CASTRO | PIAUÍ | Brasil | 2203107 | 22 | 33 | nan | nan | nan | Cerrado | 10.2 |
| e852c56e-0c38-3d9e-8c32-9a1289ddd6ac | -8.49677 | -46.87888 | 2025-09-24 12:17:00 | TERRA_M-T | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 9.3 |
| f13c4c25-2a5f-3ba8-9cad-345a9bee4818 | -3.56435 | -43.77688 | 2025-09-24 12:17:00 | TERRA_M-T | VARGEM GRANDE | MARANHÃO | Brasil | 2112704 | 21 | 33 | nan | nan | nan | Cerrado | 9.7 |
| 19036f76-07d4-3483-baf5-cf0f798e60ec | -8.84419 | -46.17861 | 2025-09-24 12:17:00 | TERRA_M-T | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 10.1 |
| fd750c24-4b13-38f0-8325-2c147b8a5687 | -7.6535 | -45.21146 | 2025-09-24 12:17:00 | TERRA_M-T | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 12.5 |
| bff64b00-816b-3745-b1fb-d9b5d8e73aa1 | -4.7536 | -43.62643 | 2025-09-24 12:17:00 | TERRA_M-T | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 22.0 |
| 87e83ede-c4f9-334d-8c93-099a8d90e400 | -4.79157 | -42.76826 | 2025-09-24 12:17:00 | TERRA_M-T | JOSÉ DE FREITAS | PIAUÍ | Brasil | 2205508 | 22 | 33 | nan | nan | nan | Cerrado | 61.8 |
| 637479a7-5860-39c6-a771-b68890b2356a | -8.1827 | -46.35721 | 2025-09-24 12:17:00 | TERRA_M-T | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 7.0 |


[Clique aqui para ver as próximas entradas](README21.md)
