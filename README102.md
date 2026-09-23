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

## Dados Diários - Página 102

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 89803090-640d-3667-a848-f455bd2dccbd | -9.30307 | -60.30865 | 2026-09-23 05:23:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.3 |
| 9a8aa840-99c2-38af-a09a-79891e6a0219 | -5.87623 | -52.1282 | 2026-09-23 05:23:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 884c2f31-aa50-342c-830a-9a80f3d422e3 | -3.05574 | -61.17866 | 2026-09-23 05:23:00 | NOAA-20 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 8eb52d90-efcd-38fe-92a9-636ea1dda60e | -9.9705 | -50.26019 | 2026-09-23 05:23:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 90b0e016-6299-376b-9f0a-6b43e6e3c524 | -10.87411 | -50.1552 | 2026-09-23 05:23:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 8254c24c-82ac-3366-b502-e8f059e7b702 | -3.50383 | -53.20247 | 2026-09-23 05:23:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 5.7 |
| c52348e8-8781-332b-8b35-0c73c6887e40 | -3.81607 | -59.00723 | 2026-09-23 05:23:00 | NOAA-20 | NOVA OLINDA DO NORTE | AMAZONAS | Brasil | 1303106 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 3269fe15-f137-3527-8e6e-c4f0c4fcf1aa | -3.1673 | -60.65779 | 2026-09-23 05:23:00 | NOAA-20 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| a108df1d-237a-3ac9-826b-b3281fba3b10 | -12.41971 | -46.97252 | 2026-09-23 05:23:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 6d52574b-be06-362e-8b7c-a168a43b6ae2 | -10.30375 | -50.50776 | 2026-09-23 05:23:00 | NOAA-20 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 12.9 |
| 7e723739-4a84-3a14-95a4-9693157be8ec | -3.04064 | -59.11835 | 2026-09-23 05:23:00 | NOAA-20 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| c4dc65a9-0cc3-345c-b5fe-0d290780f1d0 | -3.62878 | -58.92421 | 2026-09-23 05:23:00 | NOAA-20 | NOVA OLINDA DO NORTE | AMAZONAS | Brasil | 1303106 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| b06143d8-d29e-39ba-bbdd-dabcaba96012 | -9.55098 | -65.98071 | 2026-09-23 05:23:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 81af058d-5e4c-33a8-bbac-1b23d47aa6b0 | -10.44602 | -50.35786 | 2026-09-23 05:23:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 12082018-66c3-3f52-aa89-4875bf0443c3 | -3.82694 | -59.40736 | 2026-09-23 05:23:00 | NOAA-20 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| d2d89d0c-6379-399d-9d23-1fdfbfaea7f3 | -3.77381 | -60.74289 | 2026-09-23 05:23:00 | NOAA-20 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| ffa96cd5-b9ce-3868-95d7-6620e99d0bd4 | -3.11294 | -61.09248 | 2026-09-23 05:23:00 | NOAA-20 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 2df21f24-1d47-3b84-8798-676713b9df4d | -10.38251 | -54.41182 | 2026-09-23 05:23:00 | NOAA-20 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 2d423cef-16cb-3a2f-9515-20c5180d79bd | -2.62518 | -51.70249 | 2026-09-23 05:23:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| d5549f0e-c657-3cf8-845d-67b44123e577 | -8.18023 | -61.18698 | 2026-09-23 05:23:00 | NOAA-20 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| e926a868-ab29-3278-a4e6-280d08bfe07b | -4.45647 | -47.91909 | 2026-09-23 05:23:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| bb72a8a9-0092-3366-8e0f-ae841c6fc6d7 | -3.43018 | -58.4204 | 2026-09-23 05:23:00 | NOAA-20 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 1ed1dc8f-1577-301e-acdd-a49b440e7833 | -10.29252 | -50.55322 | 2026-09-23 05:23:00 | NOAA-20 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| d22f1ff1-29de-39d5-b883-f5925731e4b6 | -4.35142 | -55.65884 | 2026-09-23 05:23:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 277227ac-bc3f-3808-a1e1-ef0277bb93e8 | 0.78722 | -59.19902 | 2026-09-23 05:23:00 | NOAA-20 | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 0.8 |
| daef6068-7423-33d7-9ade-fc7e9c726852 | -3.14862 | -57.6857 | 2026-09-23 05:23:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 541869c2-1fea-35bc-86ae-d2bb86d16e14 | -5.34963 | -45.17229 | 2026-09-23 05:23:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 8eef3846-24f5-3880-9c61-20928e47d67c | -6.04292 | -53.27084 | 2026-09-23 05:23:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 8a7e5fbb-906f-3802-98f9-56917c4ee4b4 | -11.13117 | -49.4495 | 2026-09-23 05:23:00 | NOAA-20 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 82fa155e-f1b3-3031-89f4-aece99ec4d86 | -2.9548 | -57.73042 | 2026-09-23 05:23:00 | NOAA-20 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| e8c4a028-175f-31e3-957f-7c9caec049b7 | -3.77156 | -60.73478 | 2026-09-23 05:23:00 | NOAA-20 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| db1f11c6-db7b-3528-899e-12650de030d6 | -4.27173 | -55.44794 | 2026-09-23 05:23:00 | NOAA-20 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 41e20593-b36e-33e6-a9be-3a5702e42586 | -4.3544 | -55.66332 | 2026-09-23 05:23:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| e9126f90-a2ba-3e99-a2c7-39afaa88ed09 | -9.13039 | -65.93929 | 2026-09-23 05:23:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| cadd33fd-c972-3391-9deb-75f75de377c6 | -10.29265 | -50.5428 | 2026-09-23 05:23:00 | NOAA-20 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 7d8ed7f9-409b-34d1-9e2a-07f675fd798f | -10.30286 | -50.51487 | 2026-09-23 05:23:00 | NOAA-20 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 0aca5c01-b06e-3c10-a6b4-baa9a0e29df1 | -10.29094 | -50.51374 | 2026-09-23 05:23:00 | NOAA-20 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 7.0 |
| 680dc6b5-fe20-3b82-b74d-dff181cf5b9b | -6.03808 | -53.27419 | 2026-09-23 05:23:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 170d3015-fda5-3bf3-b0f2-ef6a0e89fc49 | -3.22519 | -61.04914 | 2026-09-23 05:23:00 | NOAA-20 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 4b2bdaa5-4ee6-3be0-ab47-076d4f3ab8bd | -4.25973 | -55.7619 | 2026-09-23 05:23:00 | NOAA-20 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 63eccbab-4073-3f62-b422-89974ee7d47d | -3.49632 | -59.93118 | 2026-09-23 05:23:00 | NOAA-20 | CAREIRO | AMAZONAS | Brasil | 1301100 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| ef9ad903-7c04-3279-9aa3-344bed26b3d9 | -8.49527 | -57.61499 | 2026-09-23 05:23:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |
| c46c5abd-2619-3d06-9d41-20ee1fdb9cb7 | -3.39762 | -61.05578 | 2026-09-23 05:23:00 | NOAA-20 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 711944e6-cc33-3609-a3d6-70b79a405344 | -10.07953 | -62.02014 | 2026-09-23 05:23:00 | NOAA-20 | THEOBROMA | RONDÔNIA | Brasil | 1101609 | 11 | 33 | nan | nan | nan | Amazônia | 6.4 |
| 888dd0b6-d850-3c22-bfb0-ac1cebe4ee00 | -9.70359 | -58.13669 | 2026-09-23 05:23:00 | NOAA-20 | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 3d06dc94-b99a-3aea-8836-23eedc80e7b1 | -7.87695 | -61.17899 | 2026-09-23 05:23:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 8c026e14-f9b5-32b5-8df1-bda1beeebe33 | -10.28128 | -50.54492 | 2026-09-23 05:23:00 | NOAA-20 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 99556628-bb55-3bb3-9ed4-23121041f05e | -10.27463 | -49.98044 | 2026-09-23 05:23:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 28022588-063f-3174-a9f1-428be82a7f56 | -10.29828 | -50.50025 | 2026-09-23 05:23:00 | NOAA-20 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 8.9 |
| 76229a07-16b1-373b-91de-980d8f46d7d1 | -3.43359 | -60.41382 | 2026-09-23 05:23:00 | NOAA-20 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 05bc0558-1ffe-3626-8f4e-43badaadbcad | -4.48197 | -55.49121 | 2026-09-23 05:23:00 | NOAA-20 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| cec74e0b-0487-3825-8cf0-949d2cdaff48 | -1.40131 | -49.05159 | 2026-09-23 05:23:00 | NOAA-20 | PONTA DE PEDRAS | PARÁ | Brasil | 1505700 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 2e35c8e0-938d-3f77-866b-cc0db9e2164c | -7.69826 | -61.54432 | 2026-09-23 05:23:00 | NOAA-20 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 0645aec0-8fcc-33a4-b646-52054cad00ca | -3.45696 | -58.31531 | 2026-09-23 05:23:00 | NOAA-20 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 71e3bcc8-7cc0-349e-86c0-af8db72c586c | -5.47637 | -57.1431 | 2026-09-23 05:23:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| c9aa4f74-677d-3a06-b4f9-be77eefdeab3 | -7.83656 | -63.41243 | 2026-09-23 05:23:00 | NOAA-20 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 4.4 |
| d73a25a4-76fd-3b8c-8c67-59b243cb922d | -3.22614 | -46.94325 | 2026-09-23 05:23:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 8.2 |
| a30f57f1-e8e0-3dfb-bd2b-5130f6e26315 | -7.04752 | -62.93824 | 2026-09-23 05:23:00 | NOAA-20 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 70e9dfeb-ddf3-3ef4-894e-9c1d80e53254 | -9.56245 | -65.99136 | 2026-09-23 05:23:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.1 |
| ff31c788-b94e-338f-b156-185e3b268b37 | -4.17466 | -53.66545 | 2026-09-23 05:23:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 403c9180-f08d-337e-8cc0-9d7f9d3ce096 | -6.87845 | -46.56508 | 2026-09-23 05:23:00 | NOAA-20 | FEIRA NOVA DO MARANHÃO | MARANHÃO | Brasil | 2104073 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| c9810dca-ce9a-3f52-aca7-73865b624dcc | -9.96497 | -50.25945 | 2026-09-23 05:23:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| b6cf0541-7cef-3fc0-a213-dc7f66cd0024 | -5.24209 | -48.19564 | 2026-09-23 05:23:00 | NOAA-20 | VILA NOVA DOS MARTÍRIOS | MARANHÃO | Brasil | 2112852 | 21 | 33 | nan | nan | nan | Amazônia | 2.6 |
| ae9e2a64-5cdf-3616-8de5-ce409266349f | -5.8005 | -49.15678 | 2026-09-23 05:23:00 | NOAA-20 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 022934f8-49e1-38eb-bf6e-f193d914d8c8 | -9.93032 | -48.4655 | 2026-09-23 05:23:00 | NOAA-20 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 0829bab5-cdb0-30a5-a2e0-fb3ce45453a4 | -3.81884 | -59.01121 | 2026-09-23 05:23:00 | NOAA-20 | NOVA OLINDA DO NORTE | AMAZONAS | Brasil | 1303106 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| e18b27ad-e8c8-3a5b-9dcd-944d339c3ba8 | -9.54563 | -65.68409 | 2026-09-23 05:23:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 5b0f04a7-68ba-353d-b7d3-98e5aceae515 | -4.42101 | -55.47757 | 2026-09-23 05:23:00 | NOAA-20 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 92d9076b-a16a-31f9-b81f-c6312ff7f027 | -3.16105 | -60.08242 | 2026-09-23 05:23:00 | NOAA-20 | IRANDUBA | AMAZONAS | Brasil | 1301852 | 13 | 33 | nan | nan | nan | Amazônia | 3.4 |
| f344befa-a77f-3a19-bc4e-7f7cfdbc9dfa | -3.62154 | -59.84815 | 2026-09-23 05:23:00 | NOAA-20 | CAREIRO | AMAZONAS | Brasil | 1301100 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 24d31f2d-1452-384a-ba59-c0e45c858a93 | -3.95632 | -59.99953 | 2026-09-23 05:23:00 | NOAA-20 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 96d5b61c-7369-3ee8-b3cd-500c52ef0b6a | -10.44012 | -50.36056 | 2026-09-23 05:23:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 8c9aed2b-4138-3ccb-afb9-be9eb43606c4 | -9.09767 | -61.43659 | 2026-09-23 05:23:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 197cc904-bc64-315d-84ce-c47b5562a970 | -3.89995 | -60.5892 | 2026-09-23 05:23:00 | NOAA-20 | CAREIRO | AMAZONAS | Brasil | 1301100 | 13 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 20511b01-f87f-3332-97a1-0d029bc6baa3 | -6.43494 | -48.45974 | 2026-09-23 05:23:00 | NOAA-20 | XAMBIOÁ | TOCANTINS | Brasil | 1722107 | 17 | 33 | nan | nan | nan | Amazônia | 1.0 |
| efa2af56-4338-3e5d-bbe9-4b36f8fbf711 | -3.82201 | -58.88438 | 2026-09-23 05:23:00 | NOAA-20 | NOVA OLINDA DO NORTE | AMAZONAS | Brasil | 1303106 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| ed43f298-5c99-3294-9cf6-54bfcd8395b1 | -3.15466 | -60.64803 | 2026-09-23 05:23:00 | NOAA-20 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 1ff4b382-dba5-31ce-bdb4-1faa5ecc3045 | -3.81553 | -59.01068 | 2026-09-23 05:23:00 | NOAA-20 | NOVA OLINDA DO NORTE | AMAZONAS | Brasil | 1303106 | 13 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 428893b9-3c32-31b0-8707-1e2d2e3a5987 | -3.32819 | -59.80531 | 2026-09-23 05:23:00 | NOAA-20 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| bb0d75dc-ff14-3dd8-985a-6db6c6e66371 | -3.37893 | -58.03434 | 2026-09-23 05:23:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 9986cdc7-865a-36b1-af81-2ba421a51627 | -3.63255 | -58.85764 | 2026-09-23 05:23:00 | NOAA-20 | NOVA OLINDA DO NORTE | AMAZONAS | Brasil | 1303106 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| a4a9bb9a-563e-3234-bd7f-522626b382d8 | -10.26898 | -49.97969 | 2026-09-23 05:23:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 6.4 |
| 4e881230-48e4-3d0b-9cb2-e004aa5455b0 | -9.55886 | -65.98643 | 2026-09-23 05:23:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 3.0 |
| ca858235-599d-3a00-a076-3fb35e25e4d6 | -3.39278 | -61.29068 | 2026-09-23 05:23:00 | NOAA-20 | CAAPIRANGA | AMAZONAS | Brasil | 1300839 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 3f2dd6a1-79c3-3562-895c-3bce1fd52605 | -10.29 | -50.52084 | 2026-09-23 05:23:00 | NOAA-20 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 7.5 |
| b72c4ac5-bbbc-302b-8d6d-1d0b36f621a9 | -9.55742 | -65.9948 | 2026-09-23 05:23:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.6 |
| cf02881c-8830-3771-8873-026cf6aa80a8 | -3.06739 | -54.39649 | 2026-09-23 05:23:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| b1227328-65dd-3d8c-92e5-514619ab6b6f | -3.30128 | -57.85919 | 2026-09-23 05:23:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 7c7e52ce-930f-3b22-8715-f1f3c6c3a4ce | -9.10844 | -61.43463 | 2026-09-23 05:23:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 9.9 |
| 35a15808-3e00-3ba4-82c0-44b8f4fc29e2 | -6.12824 | -52.76017 | 2026-09-23 05:23:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 5b08526f-19c7-3618-8169-a34c489fbf30 | -11.78677 | -50.97765 | 2026-09-23 05:23:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| d92d4afa-cfcc-3ac8-994a-1ccca64c3c47 | -3.68301 | -60.58656 | 2026-09-23 05:23:00 | NOAA-20 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 15.7 |
| 0622b9f8-36a0-3b43-828b-ae0e8594dc4e | -3.686 | -60.56787 | 2026-09-23 05:23:00 | NOAA-20 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 2.7 |
| fba2ce71-b48a-3047-8f34-48a42df5020f | -2.50726 | -56.61074 | 2026-09-23 05:23:00 | NOAA-20 | PARINTINS | AMAZONAS | Brasil | 1303403 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| f618dcac-6fb6-398a-b12b-aa794faca854 | -3.90527 | -55.83059 | 2026-09-23 05:23:00 | NOAA-20 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 2adade86-e300-3475-ba42-f2ff9962a51e | -3.00614 | -54.18769 | 2026-09-23 05:23:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 75f060db-873c-3673-a6fb-b743a8c707ef | -3.68345 | -60.60582 | 2026-09-23 05:23:00 | NOAA-20 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 319286d2-0111-3dd1-aa3b-a640fb190d7b | -3.6854 | -60.5716 | 2026-09-23 05:23:00 | NOAA-20 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 2.7 |
| fc6b04dd-b890-3d4f-910d-6f8fffd252e3 | 0.60763 | -55.98159 | 2026-09-23 05:23:00 | NOAA-20 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 2c02cc57-8396-37f5-a9e4-abe3aac5f10c | -3.6866 | -60.56414 | 2026-09-23 05:23:00 | NOAA-20 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 9.9 |


[Clique aqui para ver as próximas entradas](README103.md)
