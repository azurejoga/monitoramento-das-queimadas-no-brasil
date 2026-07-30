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

## Dados Diários - Página 7

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 1fa24867-378c-3a25-97d0-b56496891ea7 | -12.15053 | -48.95259 | 2026-07-30 04:14:00 | NOAA-20 | SUCUPIRA | TOCANTINS | Brasil | 1720853 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 3d29ebaf-35ee-39d7-8365-e5f4beb8feaa | -12.62215 | -44.62095 | 2026-07-30 04:14:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 1cdc20b7-0b87-3f65-9bde-6abfe66c60ff | -8.79378 | -46.73988 | 2026-07-30 04:14:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| d272b691-7a01-3ffc-98e6-27f1892235b4 | -11.41797 | -50.09619 | 2026-07-30 04:14:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 7ef30c4f-b09c-3280-bfae-8161230f4729 | -8.99752 | -45.19065 | 2026-07-30 04:14:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 2fdb16c4-5d0b-3d01-992e-cfa3cadba8f5 | -14.18926 | -43.98723 | 2026-07-30 04:14:00 | NOAA-20 | CARINHANHA | BAHIA | Brasil | 2907103 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 6db0d479-c1f1-3fc3-884e-e2156c8e1482 | -13.33192 | -54.29223 | 2026-07-30 04:14:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 0305a585-4ad9-3d41-802f-6477175db789 | -13.78851 | -44.09203 | 2026-07-30 04:14:00 | NOAA-20 | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 4b45c9f7-ce90-3759-85a3-1365a679d495 | -12.8206 | -41.95681 | 2026-07-30 04:14:00 | NOAA-20 | BONINAL | BAHIA | Brasil | 2904001 | 29 | 33 | nan | nan | nan | Caatinga | 1.4 |
| e26d09f1-0ca6-3bba-8ab7-96e2a0fea8bf | -15.87801 | -43.60008 | 2026-07-30 04:14:00 | NOAA-20 | CAPITÃO ENÉAS | MINAS GERAIS | Brasil | 3112703 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 61895637-e166-3f08-bd64-d811c8952c99 | -8.99104 | -45.18565 | 2026-07-30 04:14:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 49f9bc9a-7e9b-31c1-9a60-45ddc45c5739 | -13.3182 | -43.59133 | 2026-07-30 04:14:00 | NOAA-20 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 16.5 |
| 6bde06c5-4c31-3fc4-a7e6-4b2056a6e8c1 | -11.41051 | -50.0846 | 2026-07-30 04:14:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| b78cf283-cff0-3e92-955e-6be2e7acea21 | -10.93291 | -43.05817 | 2026-07-30 04:14:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 39.5 |
| 672a61cc-ef87-369f-9cb5-983e12b0983a | -8.99464 | -45.18603 | 2026-07-30 04:14:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 02a7e85d-1953-3d0c-8c1f-1913d60515eb | -12.62552 | -44.62152 | 2026-07-30 04:14:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| c02c7de6-d136-3fdc-96e5-3265dc999868 | -11.41886 | -50.09128 | 2026-07-30 04:14:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 7668aa5c-3ec6-3cae-b5ac-5d69e6660415 | -12.28255 | -50.35282 | 2026-07-30 04:14:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 0717d771-7b7e-3371-ac34-be70f8e5405f | -12.2815 | -50.34888 | 2026-07-30 04:14:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| ab644ffd-881d-37e1-a6f4-e3d9ada6be59 | -9.61431 | -47.76158 | 2026-07-30 04:14:00 | NOAA-20 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 11.2 |
| f8c91cf6-6111-3559-ad2e-04b2d8e79a27 | -12.3093 | -46.7522 | 2026-07-30 04:14:00 | NOAA-20 | TAGUATINGA | TOCANTINS | Brasil | 1720903 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 2de87379-5bc1-37ca-8562-f3787341541f | -13.06896 | -42.03684 | 2026-07-30 04:14:00 | NOAA-20 | PIATÃ | BAHIA | Brasil | 2924306 | 29 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 40435f72-8d7f-377c-9a19-07ac759d1a58 | -8.80448 | -49.15468 | 2026-07-30 04:14:00 | NOAA-20 | GOIANORTE | TOCANTINS | Brasil | 1708304 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 50874078-28d1-34b6-8aae-a737d20a5e49 | -9.55243 | -48.66592 | 2026-07-30 04:14:00 | NOAA-20 | MIRANORTE | TOCANTINS | Brasil | 1713304 | 17 | 33 | nan | nan | nan | Cerrado | 4.3 |
| b7f37e0b-62d9-3338-b986-4eb834a52f08 | -11.92906 | -43.43739 | 2026-07-30 04:14:00 | NOAA-20 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 2cbd9ebf-1e48-35eb-8e88-cd67783c7cf1 | -12.14628 | -48.95183 | 2026-07-30 04:14:00 | NOAA-20 | SUCUPIRA | TOCANTINS | Brasil | 1720853 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 460743aa-ca15-354d-87b3-399978acbdeb | -13.78908 | -44.08847 | 2026-07-30 04:14:00 | NOAA-20 | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 56187037-f984-314c-b82a-3791d5544c94 | -10.93622 | -43.0587 | 2026-07-30 04:14:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 39.5 |
| e6b21c64-0635-32b8-9a9f-155d712a1983 | -10.63346 | -47.4869 | 2026-07-30 04:14:00 | NOAA-20 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 7fc6b11f-6361-3ffa-a495-bf7f2dc0306c | -11.54073 | -47.55423 | 2026-07-30 04:14:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 0fa10f59-2139-34e0-bfff-fa2be8d84246 | -11.53988 | -47.55909 | 2026-07-30 04:14:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| fb523637-f543-39db-8c98-bdc442a0a97b | -8.23598 | -43.78252 | 2026-07-30 04:14:00 | NOAA-20 | COLÔNIA DO GURGUÉIA | PIAUÍ | Brasil | 2202752 | 22 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 3bcbafcf-7a86-330d-9b1e-8dcc3d021e38 | -13.79183 | -44.09259 | 2026-07-30 04:14:00 | NOAA-20 | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 160145f0-b399-3e6b-911d-aeece2b0595e | -8.12664 | -46.77679 | 2026-07-30 04:14:00 | NOAA-20 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 8ac24026-4be6-37be-9cae-c10b682f4cdc | -14.19429 | -43.97711 | 2026-07-30 04:14:00 | NOAA-20 | CARINHANHA | BAHIA | Brasil | 2907103 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 67ae370f-82aa-3c0d-af00-f3466b7642ca | -9.61024 | -47.76077 | 2026-07-30 04:14:00 | NOAA-20 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 11.2 |
| 02fa54a5-667d-35fa-8538-45abf3bb07af | -11.923 | -43.43279 | 2026-07-30 04:14:00 | NOAA-20 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 120c353d-3e5e-3b0c-a908-efc1660ea71f | -10.20704 | -38.54872 | 2026-07-30 04:14:00 | NOAA-20 | JEREMOABO | BAHIA | Brasil | 2918100 | 29 | 33 | nan | nan | nan | Caatinga | 1.1 |
| cb5ca431-611c-3a05-9961-651558ce0fab | -11.91969 | -43.43224 | 2026-07-30 04:14:00 | NOAA-20 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 088f3ad6-ccbc-3593-9eff-437fe65ee4e9 | -10.63023 | -47.48928 | 2026-07-30 04:14:00 | NOAA-20 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 85f03db8-7a1a-3a12-84e7-d13f001f73c8 | -10.93566 | -43.06221 | 2026-07-30 04:14:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 43.3 |
| b078e666-e593-3311-b9cb-50ebc624a47d | -13.44053 | -43.67651 | 2026-07-30 04:14:00 | NOAA-20 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| a7ac98ef-2d96-3bd9-a8c0-6b6ef3988168 | -11.09108 | -47.80406 | 2026-07-30 04:14:00 | NOAA-20 | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 01c01d4e-3c1e-39e0-935c-55c077e2c417 | -10.62952 | -47.48611 | 2026-07-30 04:14:00 | NOAA-20 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 389ee95a-58cb-38f3-ab86-184e06e7fb23 | -14.03857 | -42.55199 | 2026-07-30 04:14:00 | NOAA-20 | CAETITÉ | BAHIA | Brasil | 2905206 | 29 | 33 | nan | nan | nan | Caatinga | 0.5 |
| 830e779b-16a8-3dce-8b16-14584c329e5b | -15.44449 | -41.38027 | 2026-07-30 04:14:00 | NOAA-20 | CÂNDIDO SALES | BAHIA | Brasil | 2906709 | 29 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 5de516b8-fa54-3126-92e3-1797a1031690 | -11.93238 | -43.43794 | 2026-07-30 04:14:00 | NOAA-20 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 20.2 |
| c3f90d61-3b36-3290-b9ab-6f3b6de17dda | -11.08772 | -47.79958 | 2026-07-30 04:14:00 | NOAA-20 | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 30fcc093-7dd3-3744-8719-29585df9cfd4 | -12.15124 | -48.94863 | 2026-07-30 04:14:00 | NOAA-20 | SUCUPIRA | TOCANTINS | Brasil | 1720853 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 72e0f213-0ba8-3a32-8e49-8dfa1fa9eab4 | -10.6311 | -47.48418 | 2026-07-30 04:14:00 | NOAA-20 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 8aa7e5c1-c15d-3338-aa26-93a69a380e38 | -9.61366 | -47.76525 | 2026-07-30 04:14:00 | NOAA-20 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 9c240877-b503-3e14-83cf-f249275747b7 | -10.90212 | -45.20571 | 2026-07-30 04:14:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 69e9ab5c-d27f-33bf-8102-f16420d785c6 | -10.89863 | -45.20512 | 2026-07-30 04:14:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| fa776ca9-dfee-3354-b2ae-4f75a530330a | -10.19713 | -42.21199 | 2026-07-30 04:14:00 | NOAA-20 | SENTO SÉ | BAHIA | Brasil | 2930204 | 29 | 33 | nan | nan | nan | Caatinga | 2.6 |
| 17dc1eb5-f7b4-39e7-b6c0-065d9234e214 | -9.4476 | -50.31024 | 2026-07-30 04:14:00 | NOAA-20 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| d87ba049-0093-32f7-a49b-fcdced7bb251 | -13.7525 | -51.89469 | 2026-07-30 04:14:00 | NOAA-20 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 82ac9ff1-a26a-3e10-af6a-9789ad2617f4 | -13.75691 | -51.89874 | 2026-07-30 04:14:00 | NOAA-20 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| e7531196-08de-3494-a9c2-71d868b1ba9e | -8.07658 | -46.00802 | 2026-07-30 04:14:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| ec2224a2-923d-323e-994d-81ebb8e5c324 | -13.74191 | -51.89565 | 2026-07-30 04:14:00 | NOAA-20 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 2129ce88-f082-3fc4-9dbf-6d0ac6950804 | -14.18309 | -44.00448 | 2026-07-30 04:14:00 | NOAA-20 | CARINHANHA | BAHIA | Brasil | 2907103 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 48c0838e-e223-35e6-933f-b6c583cb1fcf | -12.147 | -48.94786 | 2026-07-30 04:14:00 | NOAA-20 | SUCUPIRA | TOCANTINS | Brasil | 1720853 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 87e90efe-d429-31e8-ac99-73472cc8d32a | -14.19086 | -43.99847 | 2026-07-30 04:14:00 | NOAA-20 | CARINHANHA | BAHIA | Brasil | 2907103 | 29 | 33 | nan | nan | nan | Cerrado | 2.7 |
| dc70cfc0-1839-3053-b846-eb3cc9375f0d | -13.60598 | -42.93126 | 2026-07-30 04:14:00 | NOAA-20 | RIACHO DE SANTANA | BAHIA | Brasil | 2926400 | 29 | 33 | nan | nan | nan | Caatinga | 0.4 |
| 947ef12a-c052-36de-997e-772e8b5a6153 | -13.31876 | -43.58779 | 2026-07-30 04:14:00 | NOAA-20 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 3fe91ca7-82d0-365f-9b5c-86036d0a1ee9 | -12.313 | -46.75286 | 2026-07-30 04:14:00 | NOAA-20 | TAGUATINGA | TOCANTINS | Brasil | 1720903 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 7dc5e226-4969-3d38-8be1-06ebc56ef77f | -9.45247 | -50.31111 | 2026-07-30 04:14:00 | NOAA-20 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 641067ec-8513-3078-b253-6308c1d3fcd9 | -10.89985 | -45.20437 | 2026-07-30 04:14:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 554e9a68-81e8-3491-807f-1b32496636d9 | -8.80363 | -49.1594 | 2026-07-30 04:14:00 | NOAA-20 | GOIANORTE | TOCANTINS | Brasil | 1708304 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 34e85470-353b-3c64-973d-c3a893d5f0ef | -9.55364 | -48.66513 | 2026-07-30 04:14:00 | NOAA-20 | MIRANORTE | TOCANTINS | Brasil | 1713304 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 0615ed3f-7312-33bc-b935-69bb08802a5b | -12.81669 | -41.9599 | 2026-07-30 04:14:00 | NOAA-20 | BONINAL | BAHIA | Brasil | 2904001 | 29 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 56d51c71-dc88-3fed-ad99-45da5103998b | -11.66312 | -43.76092 | 2026-07-30 04:14:00 | NOAA-20 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 25adda28-4beb-30c9-ab48-99bf576d71ba | -7.38757 | -49.74748 | 2026-07-30 04:14:00 | NOAA-20 | FLORESTA DO ARAGUAIA | PARÁ | Brasil | 1503044 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| fa7f817f-1ae0-3ccf-b7f6-92edce72344f | -8.12737 | -46.77536 | 2026-07-30 04:14:00 | NOAA-20 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| bf435f73-b3e6-349b-8b80-2ded9b47c23c | -10.77643 | -42.71739 | 2026-07-30 04:14:00 | NOAA-20 | XIQUE-XIQUE | BAHIA | Brasil | 2933604 | 29 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 6042434d-7be2-3b8a-b212-21065b0e13ab | -11.41424 | -50.09039 | 2026-07-30 04:14:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| b1880094-d101-3e4e-b185-38c772f27a23 | -12.82004 | -41.96045 | 2026-07-30 04:14:00 | NOAA-20 | BONINAL | BAHIA | Brasil | 2904001 | 29 | 33 | nan | nan | nan | Caatinga | 1.1 |
| a208d302-6cbd-369d-9cab-f97040f38524 | -14.19806 | -43.99603 | 2026-07-30 04:14:00 | NOAA-20 | CARINHANHA | BAHIA | Brasil | 2907103 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| b621e1c5-ef64-35f0-b947-18a27637dcff | -11.38383 | -50.12535 | 2026-07-30 04:14:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| d3e729f3-5dc9-392c-9df8-203a665855ca | -14.16518 | -42.67455 | 2026-07-30 04:14:00 | NOAA-20 | GUANAMBI | BAHIA | Brasil | 2911709 | 29 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 3d3849d5-7647-3599-b282-c8d3eb4b0a33 | -9.55289 | -48.6693 | 2026-07-30 04:14:00 | NOAA-20 | MIRANORTE | TOCANTINS | Brasil | 1713304 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| a9120b0f-a1ed-3575-a070-532658d667a6 | -10.07897 | -37.45123 | 2026-07-30 04:14:00 | NOAA-20 | MONTE ALEGRE DE SERGIPE | SERGIPE | Brasil | 2804201 | 28 | 33 | nan | nan | nan | Caatinga | 0.4 |
| 8458d57e-d3d9-3400-a8a4-8b56151ddc95 | -15.71238 | -42.25806 | 2026-07-30 04:14:00 | NOAA-20 | RIO PARDO DE MINAS | MINAS GERAIS | Brasil | 3155603 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 6159babc-f2e0-3d37-bdee-31ce25707bd2 | -11.39402 | -50.1222 | 2026-07-30 04:14:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| ae1221ff-2a3a-3ef0-b9c4-c41b8c8b76c7 | -9.6109 | -47.75703 | 2026-07-30 04:14:00 | NOAA-20 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 11.2 |
| edb45cc3-26c4-3df2-bcac-8e1d79b5f453 | -9.21943 | -50.09663 | 2026-07-30 04:14:00 | NOAA-20 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 2b4d52d4-3aa0-32ac-995b-273a0702e6e8 | -10.93678 | -43.0552 | 2026-07-30 04:14:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 39.5 |
| 00aa76da-b7f1-3764-9e9d-73d6a3ca9c17 | -11.55162 | -47.56126 | 2026-07-30 04:14:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 4de96a38-5769-347f-b6e4-e9527e7c00fc | -9.21846 | -50.10197 | 2026-07-30 04:14:00 | NOAA-20 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 1b5424ce-1b69-3ecc-b227-acb38393a9f1 | -21.35777 | -44.81485 | 2026-07-30 04:17:00 | NOAA-20 | ITUMIRIM | MINAS GERAIS | Brasil | 3134301 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.4 |
| 4cbcb720-6c8b-3068-8dbf-affa728190ec | -22.76325 | -43.73847 | 2026-07-30 04:17:00 | NOAA-20 | SEROPÉDICA | RIO DE JANEIRO | Brasil | 3305554 | 33 | 33 | nan | nan | nan | Mata Atlântica | 3.6 |
| 3ab7736e-06db-35ba-83d3-b5bbb20c4831 | -22.76295 | -43.73909 | 2026-07-30 04:17:00 | NOAA-20 | SEROPÉDICA | RIO DE JANEIRO | Brasil | 3305554 | 33 | 33 | nan | nan | nan | Mata Atlântica | 3.1 |
| fd2444fe-711b-38e5-9618-9b0f1a322b48 | -22.41534 | -42.24584 | 2026-07-30 04:17:00 | NOAA-20 | CASIMIRO DE ABREU | RIO DE JANEIRO | Brasil | 3301306 | 33 | 33 | nan | nan | nan | Mata Atlântica | 2.1 |
| a9b44d00-451f-3745-9df2-87b2bd091ca8 | -18.2266 | -42.21113 | 2026-07-30 04:17:00 | NOAA-20 | ÁGUA BOA | MINAS GERAIS | Brasil | 3100609 | 31 | 33 | nan | nan | nan | Mata Atlântica | 10.2 |
| 7cc7e860-7392-3222-9d0d-6b26e7b56e3f | -19.17775 | -47.34945 | 2026-07-30 04:17:00 | NOAA-20 | PERDIZES | MINAS GERAIS | Brasil | 3149804 | 31 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 0635e40c-f44e-39b2-a43a-45cb8c42e8ec | -26.48281 | -53.57502 | 2026-07-30 04:17:00 | NOAA-20 | SÃO JOSÉ DO CEDRO | SANTA CATARINA | Brasil | 4216701 | 42 | 33 | nan | nan | nan | Mata Atlântica | 2.0 |
| 9c4b8ca1-ddb8-36a5-b2ed-dc64e4561e3f | -21.4544 | -43.76493 | 2026-07-30 04:17:00 | NOAA-20 | ANTÔNIO CARLOS | MINAS GERAIS | Brasil | 3102902 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 6f3485aa-83c2-3db3-a8ea-76923515456b | -18.23004 | -42.21177 | 2026-07-30 04:17:00 | NOAA-20 | ÁGUA BOA | MINAS GERAIS | Brasil | 3100609 | 31 | 33 | nan | nan | nan | Mata Atlântica | 10.2 |
| f91c264e-0daa-39d9-8a64-3c07a3d58ecb | -18.80647 | -53.14487 | 2026-07-30 04:17:00 | NOAA-20 | COSTA RICA | MATO GROSSO DO SUL | Brasil | 5003256 | 50 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 796641da-cd00-3923-b3d5-16c0bddf6df6 | -20.73085 | -42.04423 | 2026-07-30 04:17:00 | NOAA-20 | CARANGOLA | MINAS GERAIS | Brasil | 3113305 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| c0e73c38-c0dd-3e9d-b769-d8108c8975f4 | -20.34841 | -40.9338 | 2026-07-30 04:17:00 | NOAA-20 | DOMINGOS MARTINS | ESPÍRITO SANTO | Brasil | 3201902 | 32 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |


[Clique aqui para ver as próximas entradas](README8.md)
