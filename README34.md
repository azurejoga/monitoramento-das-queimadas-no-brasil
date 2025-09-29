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
| 4579b1dd-efc6-3151-8759-86538d9e3160 | -8.16007 | -46.40218 | 2025-09-29 04:06:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 0fc2954b-3fbf-3330-a27f-a56c10c059d7 | -2.58302 | -48.40637 | 2025-09-29 04:06:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 36.3 |
| 6d2fbe8b-c581-3100-be3a-2f1212e8522e | -5.55486 | -44.84345 | 2025-09-29 04:06:00 | NOAA-20 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 6.9 |
| 82f634a5-4952-3b1a-8986-05e7413b30ca | -6.11705 | -43.46971 | 2025-09-29 04:06:00 | NOAA-20 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 2fe8cb5d-e8bc-397e-b819-aecc0b122590 | -5.33487 | -43.72994 | 2025-09-29 04:06:00 | NOAA-20 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| cb0152f2-b31f-3286-9c84-f3942f279407 | -7.22004 | -44.7638 | 2025-09-29 04:06:00 | NOAA-20 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 25e4c8e1-21a0-38e0-abcc-c573d7290786 | -5.46853 | -42.88184 | 2025-09-29 04:06:00 | NOAA-20 | NAZÁRIA | PIAUÍ | Brasil | 2206720 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| a37e54ae-ad6d-347b-b55c-1db4f09b36c8 | -6.62501 | -44.95942 | 2025-09-29 04:06:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| dbd804c2-03bc-3b70-98b6-6205f92f9c74 | -5.71309 | -42.86458 | 2025-09-29 04:06:00 | NOAA-20 | SÃO PEDRO DO PIAUÍ | PIAUÍ | Brasil | 2210508 | 22 | 33 | nan | nan | nan | Caatinga | 4.6 |
| 72909135-fb55-359d-87fa-8b4b82ff731c | -4.57377 | -38.92237 | 2025-09-29 04:06:00 | NOAA-20 | ITAPIÚNA | CEARÁ | Brasil | 2306504 | 23 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 448a275c-fe32-3447-8bab-5f815ec5de36 | -7.24901 | -43.01575 | 2025-09-29 04:06:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 9328707a-2701-3e66-98ac-471fba8a22f4 | -6.22224 | -44.19932 | 2025-09-29 04:06:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 77972769-8eb2-3bc0-ae53-2b636230dca0 | -5.69062 | -42.62812 | 2025-09-29 04:06:00 | NOAA-20 | MONSENHOR GIL | PIAUÍ | Brasil | 2206407 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 7841f61f-48c7-3505-a710-af0cf35c6b41 | -6.39401 | -42.90212 | 2025-09-29 04:06:00 | NOAA-20 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Caatinga | 3.1 |
| a64e920e-7c7f-3356-a074-3f0c6844dcc4 | -5.71998 | -42.84325 | 2025-09-29 04:06:00 | NOAA-20 | SÃO PEDRO DO PIAUÍ | PIAUÍ | Brasil | 2210508 | 22 | 33 | nan | nan | nan | Caatinga | 14.5 |
| e2bc23c1-60e2-32c6-b653-6706634086f9 | -2.57722 | -48.411 | 2025-09-29 04:06:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 10.0 |
| baf653eb-2a87-3e2a-9ff3-db5e919842cc | -5.52066 | -42.73003 | 2025-09-29 04:06:00 | NOAA-20 | LAGOA DO PIAUÍ | PIAUÍ | Brasil | 2205581 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| de12c8bc-352d-37bf-b89a-aca5ae714247 | -6.11483 | -43.46165 | 2025-09-29 04:06:00 | NOAA-20 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 3abd9a17-8572-3801-ad95-d870b78f1d7c | -5.09 | -43.85432 | 2025-09-29 04:06:00 | NOAA-20 | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 6fe10fd1-dfd7-3021-b776-5d7481506d83 | -5.75368 | -42.54641 | 2025-09-29 04:06:00 | NOAA-20 | BARRO DURO | PIAUÍ | Brasil | 2201408 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| d3469ca7-0fb4-35d5-8d19-c78b947015f1 | -6.88981 | -44.5309 | 2025-09-29 04:06:00 | NOAA-20 | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 78fd1abd-a832-3201-bad0-cad195397438 | -6.06681 | -42.60701 | 2025-09-29 04:06:00 | NOAA-20 | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 29dd1061-9358-3a40-a63f-8f8687f2be91 | -7.24564 | -43.0152 | 2025-09-29 04:06:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| f5356ef3-8f1b-3b8c-9b38-c8455605d86e | -6.58006 | -43.42738 | 2025-09-29 04:06:00 | NOAA-20 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Caatinga | 2.7 |
| 74aa04fc-9816-302f-bff7-a0cfa4843d47 | -7.88923 | -44.59703 | 2025-09-29 04:06:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| e5eef715-57e0-3aa0-ba8e-d3f1c463486a | -7.49232 | -44.30159 | 2025-09-29 04:06:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.4 |
| b2b7e7f6-adae-3026-975b-f3fb6d7345a5 | -8.30013 | -45.48018 | 2025-09-29 04:06:00 | NOAA-20 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 5.1 |
| ae5a4b41-85a0-3592-9b73-f1d6c787ef3f | -6.27272 | -44.91703 | 2025-09-29 04:06:00 | NOAA-20 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 902eb8c2-3f0f-3b6c-87e4-4af0a07fce12 | -5.30747 | -43.16314 | 2025-09-29 04:06:00 | NOAA-20 | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 03e12f06-d196-328b-926b-29552ca68fa8 | -6.07449 | -42.4733 | 2025-09-29 04:06:00 | NOAA-20 | HUGO NAPOLEÃO | PIAUÍ | Brasil | 2204600 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 30461ef1-8a14-3135-9993-37d6adf4ac91 | -5.18817 | -43.76441 | 2025-09-29 04:06:00 | NOAA-20 | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 9.4 |
| e7a1f261-80b3-3bb2-a00a-39e7aeaaaebe | -5.51254 | -42.20732 | 2025-09-29 04:06:00 | NOAA-20 | ALTO LONGÁ | PIAUÍ | Brasil | 2200301 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| b39ad062-c62d-3473-be10-38757a996312 | -7.24227 | -43.01465 | 2025-09-29 04:06:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| a21c5361-2ae0-3ce6-83ac-fbfaa800ea98 | -8.30093 | -45.498 | 2025-09-29 04:06:00 | NOAA-20 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 14.8 |
| 681cd065-c284-36e8-92dc-785a078a9e0e | -7.69945 | -41.28668 | 2025-09-29 04:06:00 | NOAA-20 | PATOS DO PIAUÍ | PIAUÍ | Brasil | 2207777 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 4f208256-d7ef-30f6-8984-a05390d09881 | -5.72103 | -42.85835 | 2025-09-29 04:06:00 | NOAA-20 | SÃO PEDRO DO PIAUÍ | PIAUÍ | Brasil | 2210508 | 22 | 33 | nan | nan | nan | Caatinga | 2.2 |
| 7562ff91-2f17-38dc-9357-bde017ed1274 | -6.71284 | -44.58773 | 2025-09-29 04:06:00 | NOAA-20 | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 4f425aa2-d9ed-3fb8-bed4-7bac0730021a | -2.9177 | -48.19845 | 2025-09-29 04:06:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| cae65497-c02e-37dd-897c-39844c218631 | -6.89404 | -44.52745 | 2025-09-29 04:06:00 | NOAA-20 | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| f912ca54-6745-3c70-8b16-eddf51d46128 | -5.92966 | -48.19629 | 2025-09-29 04:06:00 | NOAA-20 | ARAGUATINS | TOCANTINS | Brasil | 1702208 | 17 | 33 | nan | nan | nan | Amazônia | 1.2 |
| b193faf5-5893-37bc-a579-7bfb4bd9659a | -5.71929 | -42.86926 | 2025-09-29 04:06:00 | NOAA-20 | SÃO PEDRO DO PIAUÍ | PIAUÍ | Brasil | 2210508 | 22 | 33 | nan | nan | nan | Caatinga | 3.3 |
| 81fe2cb8-b23c-3c67-b9f5-a2a8d6447084 | -6.14074 | -42.65163 | 2025-09-29 04:06:00 | NOAA-20 | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| fe762aec-e468-34aa-bbad-3900eeb18be7 | -5.73308 | -42.67501 | 2025-09-29 04:06:00 | NOAA-20 | MIGUEL LEÃO | PIAUÍ | Brasil | 2206308 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 58462d8f-4150-332a-a835-61bc224dcf34 | -5.47648 | -42.87566 | 2025-09-29 04:06:00 | NOAA-20 | NAZÁRIA | PIAUÍ | Brasil | 2206720 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 180b3703-e7ab-334d-8e04-532863159412 | -6.15078 | -42.80391 | 2025-09-29 04:06:00 | NOAA-20 | AMARANTE | PIAUÍ | Brasil | 2200509 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 8ee188a7-a42d-3094-abcb-4aaf61d70c18 | -6.2187 | -44.19868 | 2025-09-29 04:06:00 | NOAA-20 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 4322f394-e88c-369c-90c8-a68d68a724c5 | -6.0594 | -42.4818 | 2025-09-29 04:06:00 | NOAA-20 | HUGO NAPOLEÃO | PIAUÍ | Brasil | 2204600 | 22 | 33 | nan | nan | nan | Caatinga | 5.3 |
| 73b9d70d-d6b3-3519-9eaf-584957fd6154 | -6.12554 | -43.4827 | 2025-09-29 04:06:00 | NOAA-20 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 4.6 |
| b3d27e40-dc22-370b-a89a-87b51e6913c9 | -5.74155 | -42.66525 | 2025-09-29 04:06:00 | NOAA-20 | AGRICOLÂNDIA | PIAUÍ | Brasil | 2200103 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 97a518d7-9d62-37a8-bedd-268d7184b8d2 | -7.03698 | -45.18705 | 2025-09-29 04:06:00 | NOAA-20 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| eaccde34-d909-3a57-bd3f-fa9ae3913bcb | -7.72782 | -44.79168 | 2025-09-29 04:06:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 318b6cd9-5495-3245-b0a9-b2684ac93b0c | -8.16566 | -46.39289 | 2025-09-29 04:06:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 6.9 |
| 545c4ee2-6fdf-3542-ac66-f6a7053b564a | -8.26487 | -45.47293 | 2025-09-29 04:06:00 | NOAA-20 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 42488666-4472-3f63-9cac-8087790f7a6c | -6.13796 | -42.6475 | 2025-09-29 04:06:00 | NOAA-20 | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | 2.2 |
| e968c8a3-1c5f-35d2-9702-16a20de3aaf8 | -6.46912 | -44.51331 | 2025-09-29 04:06:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 214208a6-033e-3cd5-a6cc-6490d98ec33c | -5.80293 | -42.853 | 2025-09-29 04:06:00 | NOAA-20 | SÃO PEDRO DO PIAUÍ | PIAUÍ | Brasil | 2210508 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 24dfc0d2-02a3-3dce-aee6-749613f97162 | -5.89737 | -42.50026 | 2025-09-29 04:06:00 | NOAA-20 | OLHO D'ÁGUA DO PIAUÍ | PIAUÍ | Brasil | 2207108 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 3a23ea78-91e0-3004-ab4b-baaf689348ef | -7.86889 | -44.59101 | 2025-09-29 04:06:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 8af82a61-6244-3050-9f95-2e9b41ac5a74 | -6.22157 | -44.2034 | 2025-09-29 04:06:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| f8225913-29af-30a3-be4d-ec2856227ec1 | -7.73344 | -46.9707 | 2025-09-29 04:06:00 | NOAA-20 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 501aa942-7706-36f9-8b3e-1cb6766cf966 | -6.74593 | -44.74793 | 2025-09-29 04:06:00 | NOAA-20 | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 4.3 |
| b110fbc2-3daf-34ca-a2e7-c36a93e9694a | -3.40269 | -46.9034 | 2025-09-29 04:06:00 | NOAA-20 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| ba03161e-e2f0-31c4-ab8e-1d13f44638b4 | -6.61875 | -44.9557 | 2025-09-29 04:06:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 5.7 |
| ff1dfc78-7fbf-30fa-be65-a11b81e115e4 | -8.11819 | -42.37891 | 2025-09-29 04:06:00 | NOAA-20 | PEDRO LAURENTINO | PIAUÍ | Brasil | 2207934 | 22 | 33 | nan | nan | nan | Caatinga | 0.4 |
| c0d1540c-1cc8-3be2-bec9-c7e7be01d13f | -7.30628 | -43.81641 | 2025-09-29 04:06:00 | NOAA-20 | LANDRI SALES | PIAUÍ | Brasil | 2205607 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| d9cf6e5b-c6da-3588-a7cb-ae1509862ac9 | -7.56369 | -42.40454 | 2025-09-29 04:06:00 | NOAA-20 | SÃO MIGUEL DO FIDALGO | PIAUÍ | Brasil | 2210391 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 239a73af-6d50-3e09-af58-adf486af95c4 | -5.73187 | -42.834 | 2025-09-29 04:06:00 | NOAA-20 | SÃO PEDRO DO PIAUÍ | PIAUÍ | Brasil | 2210508 | 22 | 33 | nan | nan | nan | Caatinga | 3.5 |
| 7b61d592-be84-38ff-8dfe-0584784204b2 | -5.12689 | -47.38703 | 2025-09-29 04:06:00 | NOAA-20 | SÃO FRANCISCO DO BREJÃO | MARANHÃO | Brasil | 2110856 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| cb693567-6fc6-30cf-9503-53e0fda670f8 | -4.38494 | -44.08836 | 2025-09-29 04:06:00 | NOAA-20 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| d879221e-a12e-358e-83a6-8e6f097394f9 | -6.62373 | -45.89658 | 2025-09-29 04:06:00 | NOAA-20 | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 1c3782c1-3717-3465-8f77-2f442f0b650a | -5.63314 | -44.91312 | 2025-09-29 04:06:00 | NOAA-20 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 7.3 |
| 18ff636d-b309-35ab-8a1b-e7a69e8ac350 | -6.1221 | -43.48212 | 2025-09-29 04:06:00 | NOAA-20 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| d9ef7091-043f-3536-86ec-3ceb1a9d59dc | -4.71139 | -41.98639 | 2025-09-29 04:06:00 | NOAA-20 | CAMPO MAIOR | PIAUÍ | Brasil | 2202208 | 22 | 33 | nan | nan | nan | Caatinga | 6.9 |
| 9895494e-8191-3cde-8335-df8a839d56f4 | -6.20835 | -42.84295 | 2025-09-29 04:06:00 | NOAA-20 | AMARANTE | PIAUÍ | Brasil | 2200509 | 22 | 33 | nan | nan | nan | Caatinga | 3.2 |
| 6f537981-42fa-375a-a95b-7abbbb894896 | -6.89048 | -44.52679 | 2025-09-29 04:06:00 | NOAA-20 | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| c9f734f5-7fd0-3189-bc9e-8e12658073d1 | -6.46854 | -42.92157 | 2025-09-29 04:06:00 | NOAA-20 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 8ff883d7-89e5-39e4-829d-0b146cb1e49c | -7.58612 | -44.79009 | 2025-09-29 04:06:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| c142390a-6e6e-3fc1-8ae4-036c472860e0 | -6.7667 | -45.61914 | 2025-09-29 04:06:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| fb9943f0-c9c4-35e3-9c50-05e6581813eb | -6.47006 | -43.94896 | 2025-09-29 04:06:00 | NOAA-20 | PARAIBANO | MARANHÃO | Brasil | 2107704 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| af778739-d431-3488-9b70-577110ce9db1 | -7.57985 | -44.80582 | 2025-09-29 04:06:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 221f47cb-9b4c-3872-802c-0da3cef44cab | -3.94074 | -49.13447 | 2025-09-29 04:06:00 | NOAA-20 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| be25eb6f-b10f-391c-8b34-1cff3fb2c2df | -6.14458 | -43.47429 | 2025-09-29 04:06:00 | NOAA-20 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 56b182e0-a189-3ab4-a133-308a040907d6 | -6.69152 | -42.77958 | 2025-09-29 04:06:00 | NOAA-20 | FRANCISCO AYRES | PIAUÍ | Brasil | 2204105 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 730a5db9-f101-31df-85bf-ffd5dfcbf356 | -4.74137 | -43.27954 | 2025-09-29 04:06:00 | NOAA-20 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 97db388d-31e7-3e91-b6ab-09772cdd5790 | -5.42097 | -41.32697 | 2025-09-29 04:06:00 | NOAA-20 | CASTELO DO PIAUÍ | PIAUÍ | Brasil | 2202604 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| ef182d9c-b632-3652-85a2-d0005e1f89ce | -7.73378 | -46.9933 | 2025-09-29 04:06:00 | NOAA-20 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 2fbcd521-3169-3eac-bdca-347854d6e3ee | -6.9865 | -43.77766 | 2025-09-29 04:06:00 | NOAA-20 | MARCOS PARENTE | PIAUÍ | Brasil | 2206001 | 22 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 115e04ff-0019-3e4b-a04b-30cabbd73396 | -4.70601 | -41.982 | 2025-09-29 04:06:00 | NOAA-20 | CAMPO MAIOR | PIAUÍ | Brasil | 2202208 | 22 | 33 | nan | nan | nan | Caatinga | 17.3 |
| 5c43713d-d061-3f80-a41c-a6abdb03d05e | -7.92702 | -42.68249 | 2025-09-29 04:06:00 | NOAA-20 | RIBEIRA DO PIAUÍ | PIAUÍ | Brasil | 2208874 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| a050887c-2952-31be-91c2-b16771b8dad7 | -6.11739 | -41.82026 | 2025-09-29 04:06:00 | NOAA-20 | AROAZES | PIAUÍ | Brasil | 2200905 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| e1fb4539-5d47-372f-b695-916be2b47196 | -5.29708 | -41.22942 | 2025-09-29 04:06:00 | NOAA-20 | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| c3b45ecf-b1af-3463-bc25-2b7ebcab3cab | -7.54495 | -46.11395 | 2025-09-29 04:06:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 8102ce2a-7c47-3f3c-82ca-59908404ca62 | -5.24778 | -45.35626 | 2025-09-29 04:06:00 | NOAA-20 | JENIPAPO DOS VIEIRAS | MARANHÃO | Brasil | 2105476 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| c55c3f7a-55e7-34ec-b24e-421ab2f7b403 | -6.38503 | -43.39731 | 2025-09-29 04:06:00 | NOAA-20 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| f7442645-fec2-3520-bc69-839e8f313078 | -4.97192 | -44.50765 | 2025-09-29 04:06:00 | NOAA-20 | SANTO ANTÔNIO DOS LOPES | MARANHÃO | Brasil | 2110302 | 21 | 33 | nan | nan | nan | Cerrado | 11.7 |
| a04798c0-0c95-3a19-ba2b-c12abeafad32 | -4.97263 | -44.50334 | 2025-09-29 04:06:00 | NOAA-20 | SANTO ANTÔNIO DOS LOPES | MARANHÃO | Brasil | 2110302 | 21 | 33 | nan | nan | nan | Cerrado | 11.7 |
| ef9b88c3-3650-3843-b2bc-378a2f83139e | -6.06959 | -42.61111 | 2025-09-29 04:06:00 | NOAA-20 | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 7017d651-8ba1-3d09-a8b0-c6984b449c0b | -6.47718 | -44.25953 | 2025-09-29 04:06:00 | NOAA-20 | SUCUPIRA DO NORTE | MARANHÃO | Brasil | 2111904 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| e2780e20-24e2-3db2-b0c6-b82b667f3fbb | -5.71238 | -42.65338 | 2025-09-29 04:06:00 | NOAA-20 | MIGUEL LEÃO | PIAUÍ | Brasil | 2206308 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 0698c56f-b186-39f2-b6ab-fecb99336701 | -4.70545 | -41.98552 | 2025-09-29 04:06:00 | NOAA-20 | CAMPO MAIOR | PIAUÍ | Brasil | 2202208 | 22 | 33 | nan | nan | nan | Caatinga | 17.3 |


[Clique aqui para ver as próximas entradas](README35.md)
