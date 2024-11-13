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

## Dados Diários - Página 41

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 4d90a8f8-4a95-3800-867b-0f5cdce48098 | -3.16483 | -48.36781 | 2024-11-13 04:57:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| cb700cb5-63e1-3f32-8b5a-8622609fed19 | -2.7338 | -51.83299 | 2024-11-13 04:57:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| bb038479-4751-3178-8d00-ff50cb28451d | -4.65104 | -45.1247 | 2024-11-13 04:57:00 | NOAA-21 | LAGO DA PEDRA | MARANHÃO | Brasil | 2105708 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| d84f7aa8-b9cf-3e9a-9616-7a5a666927ff | -3.06507 | -57.3024 | 2024-11-13 04:57:00 | NOAA-21 | BARREIRINHA | AMAZONAS | Brasil | 1300508 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 8159f330-9c40-3b31-bb80-6b674dfe76d1 | -1.52145 | -54.99049 | 2024-11-13 04:57:00 | NOAA-21 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 062eac5a-a904-38f1-9ce8-47db9d147f01 | -1.39394 | -52.07995 | 2024-11-13 04:57:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| a6d422fe-b447-300b-ac1a-b90d87e58384 | -3.34097 | -53.20986 | 2024-11-13 04:57:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 07ad7bb9-e888-3fe4-abab-1b5386a5734f | -2.14588 | -46.39951 | 2024-11-13 04:57:00 | NOAA-21 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 3ca057c7-7aa4-383c-a704-936f09434c24 | -3.04339 | -50.32893 | 2024-11-13 04:57:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 5fe1d0a2-65bf-32bc-983d-3a1114ac243e | -3.05958 | -50.34443 | 2024-11-13 04:57:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 7bd0f644-800d-3af6-9d59-7eb738ae6195 | -2.46142 | -47.83007 | 2024-11-13 04:57:00 | NOAA-21 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 856b5039-b7ca-3bde-871a-9af3c39fcf96 | -1.61196 | -52.2543 | 2024-11-13 04:57:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 8f2386bb-0620-3327-a36c-7bf3a52381dc | -2.64096 | -46.15653 | 2024-11-13 04:57:00 | NOAA-21 | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| cea0c6d9-08b7-32bc-89ae-185a6bb7da30 | -3.05872 | -50.3302 | 2024-11-13 04:57:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 32576e6c-d673-3d51-8823-e13f588bc08c | -4.67735 | -44.57968 | 2024-11-13 04:57:00 | NOAA-21 | PEDREIRAS | MARANHÃO | Brasil | 2108207 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 61c12d24-cc63-381f-a54e-327b5bac3b1c | -1.82494 | -50.64 | 2024-11-13 04:57:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 411c9241-b98a-3fe1-a166-56f3f5fe844b | -2.36389 | -48.51924 | 2024-11-13 04:57:00 | NOAA-21 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 1a5a438e-bcec-3980-a4de-5ca6e396d399 | -3.94923 | -48.18451 | 2024-11-13 04:57:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 7ded4284-2c32-3f3f-8fc4-76b7800faf7f | -2.55366 | -54.02626 | 2024-11-13 04:57:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 048c6508-4fe6-3e47-839d-6ba23a877cd7 | 3.60246 | -59.94298 | 2024-11-13 04:57:00 | NOAA-21 | NORMANDIA | RORAIMA | Brasil | 1400407 | 14 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 91deb04f-75a1-331c-92f3-a0e659a21fca | -2.28642 | -53.77644 | 2024-11-13 04:57:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| b8be7554-15f9-3682-a907-47473f8a15aa | -1.03351 | -48.85023 | 2024-11-13 04:57:00 | NOAA-21 | CACHOEIRA DO ARARI | PARÁ | Brasil | 1502004 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 73c09bf0-59cb-357f-a374-44ab8669d3e8 | -2.46887 | -50.11933 | 2024-11-13 04:57:00 | NOAA-21 | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 10.2 |
| b1f837a7-726e-33f6-8c1d-78b25d53123f | -2.86247 | -49.33831 | 2024-11-13 04:57:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| e7c4774d-2f38-3463-b72f-1c1591b1f175 | -1.62597 | -55.12958 | 2024-11-13 04:57:00 | NOAA-21 | CURUÁ | PARÁ | Brasil | 1502855 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 3a8b8a07-3fa6-3ae3-9e60-6ac4cd8a028b | -2.308 | -49.08133 | 2024-11-13 04:57:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 4d3f4e64-79ee-3590-9994-47109c6b547c | -3.66978 | -54.65546 | 2024-11-13 04:57:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 22309911-370d-3ebf-a91e-77ce9c3abcfc | -2.59777 | -54.24539 | 2024-11-13 04:57:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 139022c8-77f4-3b6d-9600-2531d6c4a32c | -2.13517 | -50.81403 | 2024-11-13 04:57:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 386bdefc-42da-3d5f-a58b-9c20d9912327 | -1.22241 | -51.78121 | 2024-11-13 04:57:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| d4602c45-da7f-3c19-803b-55d9de824722 | -3.63752 | -51.47704 | 2024-11-13 04:57:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 4276b7b7-94cd-321e-9f1c-ce15e8020b9f | -4.26879 | -48.18682 | 2024-11-13 04:57:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| a9f340e1-8746-365e-8e2c-8a1adb70097f | -2.4098 | -48.93687 | 2024-11-13 04:57:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 730e9375-4bd4-342c-a67c-7a033e9ff4c7 | -1.34744 | -51.39969 | 2024-11-13 04:57:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 1d391af5-136b-36c5-80cf-a92c8e429d9e | -3.40759 | -50.37444 | 2024-11-13 04:57:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 2f8fe2f5-2e1a-3daf-a3e5-8b287c529421 | -2.29026 | -53.77351 | 2024-11-13 04:57:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| c2e32610-a67c-34be-b1f3-72c4a198d794 | -2.22226 | -50.85553 | 2024-11-13 04:57:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 868346c8-5395-371b-8dee-612a011c69b4 | -1.625 | -52.52074 | 2024-11-13 04:57:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| f9d95750-cf53-313b-bf6b-27a59083148b | -0.89737 | -51.74978 | 2024-11-13 04:57:00 | NOAA-21 | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 8dd467c0-f188-30fd-8d80-8defb8c83d02 | -1.64049 | -52.53026 | 2024-11-13 04:57:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 7be6d96f-5c27-341e-960f-159b24f744f0 | -5.25275 | -49.79387 | 2024-11-13 04:57:00 | NOAA-21 | ITUPIRANGA | PARÁ | Brasil | 1503705 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| e002dcf2-11d1-3d02-a584-774c6ddd4543 | -1.6634 | -55.16199 | 2024-11-13 04:57:00 | NOAA-21 | CURUÁ | PARÁ | Brasil | 1502855 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 37d0cfc0-1f54-3141-9ee3-f1881e730736 | -2.57443 | -53.98007 | 2024-11-13 04:57:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| fe62ed49-1cd8-3490-bd4b-690c23765c21 | -3.76864 | -54.65356 | 2024-11-13 04:57:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| ae11ae04-cd38-3739-aeec-4d44db02cf8e | -3.79947 | -52.26941 | 2024-11-13 04:57:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 7303bb19-08ec-3264-8983-dc3048280cca | -2.76159 | -49.34023 | 2024-11-13 04:57:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| e18549f4-2ff0-3ee3-a589-dc242166868c | -2.98664 | -53.97767 | 2024-11-13 04:57:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 8.2 |
| 4b07acd4-460f-328f-b9c7-4d5c510a0944 | -4.06935 | -54.4945 | 2024-11-13 04:57:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| d5004f66-5a81-31bc-977f-415d6d5cce41 | 1.13729 | -60.60046 | 2024-11-13 04:57:00 | NOAA-21 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 4.0 |
| ccbfa26a-7736-3689-b3e9-409d8efd4cd0 | -3.08117 | -50.32938 | 2024-11-13 04:57:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 8df2b3f9-db8d-3f15-893d-becab88a5012 | -2.16093 | -50.52453 | 2024-11-13 04:57:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 4a12e010-2022-3063-bb6f-20e2fa3fc3e3 | -1.63995 | -52.53373 | 2024-11-13 04:57:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| ef3623a5-40ee-364a-b708-3c4987a3ac0c | -1.60688 | -52.39678 | 2024-11-13 04:57:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| e835f630-51c3-3f45-9137-9dcb0f8e7505 | -3.22979 | -54.85981 | 2024-11-13 04:57:00 | NOAA-21 | BELTERRA | PARÁ | Brasil | 1501451 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 476539f3-6ded-30fd-8ff8-6b6b14a93f2c | -3.95429 | -46.41768 | 2024-11-13 04:57:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 9.5 |
| 2514b178-c0cb-3c3b-8aa4-bc10d66ce603 | -16.13932 | -43.55756 | 2024-11-13 04:59:00 | AQUA_M-M | CAPITÃO ENÉAS | MINAS GERAIS | Brasil | 3112703 | 31 | 33 | nan | nan | nan | Cerrado | 6.6 |
| 70a08337-7d08-344e-bdb3-ce28636ea5ff | -10.73256 | -49.52674 | 2024-11-13 04:59:00 | AQUA_M-M | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 53.5 |
| f1938513-e01b-3e73-8abe-d12bef68ab1d | -6.92785 | -47.83123 | 2024-11-13 04:59:00 | NOAA-21 | WANDERLÂNDIA | TOCANTINS | Brasil | 1722081 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 609b496c-2df2-3f2d-b836-7d88f1846867 | -10.7408 | -49.52059 | 2024-11-13 04:59:00 | NOAA-21 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 26b6d039-4ceb-34f2-9fba-8619a7e8ebd3 | -10.73544 | -49.52804 | 2024-11-13 04:59:00 | NOAA-21 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 16.6 |
| b84dc081-7e92-3c33-8225-162e34b8f5f3 | -4.89811 | -55.91006 | 2024-11-13 04:59:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 978a9823-8c34-397a-8ef4-762876832045 | -4.16474 | -59.91073 | 2024-11-13 04:59:00 | NOAA-21 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 5c81b9ac-1058-3419-98c3-ef5d28065db4 | -6.82503 | -46.77889 | 2024-11-13 04:59:00 | NOAA-21 | SÃO PEDRO DOS CRENTES | MARANHÃO | Brasil | 2111573 | 21 | 33 | nan | nan | nan | Cerrado | 10.2 |
| eb601474-f0e3-3fc0-b08f-a3a42fb88367 | -6.95156 | -47.85857 | 2024-11-13 04:59:00 | NOAA-21 | WANDERLÂNDIA | TOCANTINS | Brasil | 1722081 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 407ff567-504b-3bb5-a0e0-19f908c862cd | -7.74125 | -49.86219 | 2024-11-13 04:59:00 | NOAA-21 | PAU D'ARCO | PARÁ | Brasil | 1505551 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 07467af1-0b86-38fc-abe2-94713b208688 | -4.16112 | -59.90601 | 2024-11-13 04:59:00 | NOAA-21 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| b4d43e3e-1523-3079-a48a-35ed26956d27 | -10.73119 | -49.52741 | 2024-11-13 04:59:00 | NOAA-21 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 16.6 |
| 15c89faf-5a05-3b85-9026-87abb8c3ebeb | -6.82435 | -46.77556 | 2024-11-13 04:59:00 | NOAA-21 | SÃO PEDRO DOS CRENTES | MARANHÃO | Brasil | 2111573 | 21 | 33 | nan | nan | nan | Cerrado | 6.7 |
| 79159f62-336c-378d-9510-6769da3cf192 | -10.72751 | -49.52279 | 2024-11-13 04:59:00 | NOAA-21 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 9acc56d8-7295-33bc-8745-30ac25ed3cf4 | -10.73599 | -49.52402 | 2024-11-13 04:59:00 | NOAA-21 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 16.6 |
| 28790f43-fba5-330e-946b-14b1ab464b5a | -10.72696 | -49.52676 | 2024-11-13 04:59:00 | NOAA-21 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 56537ee7-8227-3328-95fe-b70f27b3d4b4 | -10.46797 | -49.65323 | 2024-11-13 04:59:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| a8761a00-284b-33cc-ba6a-57859f637554 | -10.74024 | -49.52461 | 2024-11-13 04:59:00 | NOAA-21 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 2aa66cd9-f9ca-34b2-a1d9-a6b22037320a | -10.73488 | -49.53202 | 2024-11-13 04:59:00 | NOAA-21 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 60d8425a-99c6-31a5-aea5-7290ae275bdf | -10.46851 | -49.64936 | 2024-11-13 04:59:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 3821f684-a420-3a2c-9dd3-b818700b75c4 | -4.16227 | -59.91011 | 2024-11-13 04:59:00 | NOAA-21 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 7283ee20-86aa-3d36-9cd9-d746e9c9505b | -7.85878 | -45.92519 | 2024-11-13 04:59:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| d6e76a3b-5b17-3974-8254-368cb21171aa | -10.7323 | -49.5194 | 2024-11-13 04:59:00 | NOAA-21 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 85aa153e-4651-3106-aac2-2926adb86406 | -10.73175 | -49.52341 | 2024-11-13 04:59:00 | NOAA-21 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 16.6 |
| bafad701-2dc3-3486-bfa3-1fe27ef10541 | -5.00762 | -56.19345 | 2024-11-13 04:59:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 7bffc4d1-e250-3bb8-b7b4-d5e7fd64dce2 | -10.5582 | -47.59167 | 2024-11-13 04:59:00 | NOAA-21 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 6d7c1c9f-8987-38f6-8241-d0e0ca8fb737 | -6.94644 | -52.86378 | 2024-11-13 04:59:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| f5661b36-46aa-36fd-997d-311a187bcd07 | -10.73655 | -49.51999 | 2024-11-13 04:59:00 | NOAA-21 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 0d9f75bb-ec92-3d74-81ba-7c6dea10bc51 | -8.64121 | -54.55765 | 2024-11-13 04:59:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| b12cb60c-7adf-3320-a642-54e18f0de7aa | -6.9013 | -52.19222 | 2024-11-13 04:59:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| e0e4b574-321f-36e9-9df7-d91bb81198c2 | -4.99885 | -56.05078 | 2024-11-13 04:59:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| b9f5d301-2047-39cd-a7ca-45860ca035e2 | -7.54467 | -48.30302 | 2024-11-13 04:59:00 | NOAA-21 | NOVA OLINDA | TOCANTINS | Brasil | 1714880 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 18278fc4-70f9-3eed-bf04-3a720f16e6bb | -5.0106 | -56.17484 | 2024-11-13 04:59:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| b9072bba-ea9d-33fc-9c09-2f72a031b95a | -8.6246 | -55.23141 | 2024-11-13 04:59:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 9450b97b-61ce-3ce5-a778-7050a552feb2 | -6.9522 | -47.85408 | 2024-11-13 04:59:00 | NOAA-21 | WANDERLÂNDIA | TOCANTINS | Brasil | 1722081 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 3e726254-2285-3a1d-ac4f-25b80150234a | -4.16292 | -59.90608 | 2024-11-13 04:59:00 | NOAA-21 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 5fdbd595-9ada-347b-b1df-fb1d4072e09e | -4.16542 | -59.9067 | 2024-11-13 04:59:00 | NOAA-21 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 38126387-25c6-3bd6-a18e-50107dd2f8d0 | -5.00719 | -56.17418 | 2024-11-13 04:59:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| b7adf9e4-267e-3ff5-b6e1-32ed4a361cc5 | -10.73968 | -49.52863 | 2024-11-13 04:59:00 | NOAA-21 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 57386f8b-f7ee-33f6-96f5-9c40a744fe2c | -3.3519 | -48.9475 | 2024-11-13 05:00:00 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 93.6 |
| 94413c41-59b4-3f27-84b2-96d05971cf2e | -2.9924 | -51.045 | 2024-11-13 05:00:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 58.4 |
| 8a206c16-fadc-3aab-bf8d-d0293f821314 | -3.3518 | -48.9689 | 2024-11-13 05:00:00 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 85.1 |
| 3685a907-135d-3082-ae9c-529bd3212de9 | -10.7235 | -49.5265 | 2024-11-13 05:00:00 | GOES-16 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 63.8 |
| eab41e09-6a8e-3188-aa15-2254995c0bbb | -3.0504 | -50.3332 | 2024-11-13 05:00:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 78.4 |
| 8d082811-d5ee-30d9-8878-766ce777aee7 | -2.9925 | -51.0242 | 2024-11-13 05:00:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 56.1 |


[Clique aqui para ver as próximas entradas](README42.md)
