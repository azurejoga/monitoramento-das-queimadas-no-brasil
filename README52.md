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

## Dados Diários - Página 52

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 82c3d51a-6f29-3fe6-b4dc-311eb3a20980 | -19.28381 | -50.36419 | 2026-09-18 04:23:00 | NOAA-21 | UNIÃO DE MINAS | MINAS GERAIS | Brasil | 3170438 | 31 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 1a97c94d-db64-3933-a12e-c743d9096895 | -19.17962 | -48.78268 | 2026-09-18 04:23:00 | NOAA-21 | PRATA | MINAS GERAIS | Brasil | 3152808 | 31 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 189d336f-77d9-3910-b73a-683e888ac203 | -16.56588 | -43.99373 | 2026-09-18 04:23:00 | NOAA-21 | MONTES CLAROS | MINAS GERAIS | Brasil | 3143302 | 31 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 4150b4ba-899c-3322-91f7-a9dcccf16457 | -15.67615 | -52.7375 | 2026-09-18 04:23:00 | NOAA-21 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| a2147b30-17d6-3b27-8c16-0c974f2005e6 | -18.8897 | -46.84835 | 2026-09-18 04:23:00 | NOAA-21 | PATROCÍNIO | MINAS GERAIS | Brasil | 3148103 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 29c4decd-7dc7-341c-bd74-dcc9d592eb1b | -15.66639 | -52.73504 | 2026-09-18 04:23:00 | NOAA-21 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 95028061-75fb-371d-91ac-79f8f7892d8b | -19.55282 | -47.62381 | 2026-09-18 04:23:00 | NOAA-21 | NOVA PONTE | MINAS GERAIS | Brasil | 3145000 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| a6c0b3cc-5449-3ea2-8016-5b0cc672dd8c | -16.56169 | -43.99741 | 2026-09-18 04:23:00 | NOAA-21 | MONTES CLAROS | MINAS GERAIS | Brasil | 3143302 | 31 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 7ec6ea89-c0b3-3051-affe-6221bff90242 | -19.09556 | -46.6504 | 2026-09-18 04:23:00 | NOAA-21 | SERRA DO SALITRE | MINAS GERAIS | Brasil | 3166808 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| d552fdda-0489-3ed8-bff4-4044dd4b2df6 | -17.77414 | -46.47803 | 2026-09-18 04:23:00 | NOAA-21 | LAGOA GRANDE | MINAS GERAIS | Brasil | 3137536 | 31 | 33 | nan | nan | nan | Cerrado | 7.6 |
| c4dc6b3a-40b3-3667-b158-2a27e0988df9 | -19.55557 | -47.62802 | 2026-09-18 04:23:00 | NOAA-21 | NOVA PONTE | MINAS GERAIS | Brasil | 3145000 | 31 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 63c0e792-6cca-370f-95d2-bd0a22d96e07 | -18.46017 | -49.302 | 2026-09-18 04:23:00 | NOAA-21 | ITUMBIARA | GOIÁS | Brasil | 5211503 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 7df9b46e-5d30-3e49-8f07-3c68b295aa55 | -15.46725 | -52.87375 | 2026-09-18 04:23:00 | NOAA-21 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 91ad28d2-51b5-38c9-9189-5e9d94221abc | -18.43316 | -54.64062 | 2026-09-18 04:23:00 | NOAA-21 | COXIM | MATO GROSSO DO SUL | Brasil | 5003306 | 50 | 33 | nan | nan | nan | Cerrado | 1.3 |
| eb6b45bb-8aef-3135-89df-b341add89ff9 | -19.18628 | -48.78385 | 2026-09-18 04:23:00 | NOAA-21 | PRATA | MINAS GERAIS | Brasil | 3152808 | 31 | 33 | nan | nan | nan | Cerrado | 11.5 |
| 75bb781b-6ecf-3cd5-a20b-eb6a7101a164 | -19.18746 | -48.77647 | 2026-09-18 04:23:00 | NOAA-21 | PRATA | MINAS GERAIS | Brasil | 3152808 | 31 | 33 | nan | nan | nan | Cerrado | 7.0 |
| 287518ed-9777-3a0c-86a4-fdf3d83062e1 | -19.55226 | -47.62746 | 2026-09-18 04:23:00 | NOAA-21 | NOVA PONTE | MINAS GERAIS | Brasil | 3145000 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| b997c8d9-e18a-33be-b20a-acc4385841b9 | -17.79306 | -53.14063 | 2026-09-18 04:23:00 | NOAA-21 | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| d50d0ca4-eed4-320d-b410-35b20ac80146 | -21.04929 | -48.47266 | 2026-09-18 04:23:00 | NOAA-21 | BEBEDOURO | SÃO PAULO | Brasil | 3506102 | 35 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 252073bd-33ce-3a16-847c-0a56ced553a6 | -19.1896 | -48.78444 | 2026-09-18 04:23:00 | NOAA-21 | PRATA | MINAS GERAIS | Brasil | 3152808 | 31 | 33 | nan | nan | nan | Cerrado | 25.1 |
| fdf2e60c-89dd-3548-8add-c4bad5fe61fc | -19.18687 | -48.78016 | 2026-09-18 04:23:00 | NOAA-21 | PRATA | MINAS GERAIS | Brasil | 3152808 | 31 | 33 | nan | nan | nan | Cerrado | 7.0 |
| 7489cb83-3c48-3929-a790-b6acc9a52084 | -19.1808 | -48.77529 | 2026-09-18 04:23:00 | NOAA-21 | PRATA | MINAS GERAIS | Brasil | 3152808 | 31 | 33 | nan | nan | nan | Cerrado | 8.4 |
| 2c48f37f-1a7f-32b3-b016-d87b01a156f1 | -15.39268 | -53.0198 | 2026-09-18 04:23:00 | NOAA-21 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 3d2fd3e3-b203-38d4-b116-d85b7c1dcccd | -15.4558 | -48.54103 | 2026-09-18 04:23:00 | NOAA-21 | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 5b15ded3-1078-347b-94e1-fd2d17ce2148 | -17.83547 | -44.85128 | 2026-09-18 04:23:00 | NOAA-21 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 2.8 |
| c67a5ce0-82a4-3390-959e-aba2b36ccf5c | -19.18354 | -48.77957 | 2026-09-18 04:23:00 | NOAA-21 | PRATA | MINAS GERAIS | Brasil | 3152808 | 31 | 33 | nan | nan | nan | Cerrado | 7.0 |
| f75e228b-6f66-3139-9cd6-40aae03b0836 | -19.46949 | -44.76584 | 2026-09-18 04:23:00 | NOAA-21 | PAPAGAIOS | MINAS GERAIS | Brasil | 3146909 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 4cf0d9b2-b10c-368c-9ed6-e1f86dccd07f | -20.12775 | -51.80007 | 2026-09-18 04:23:00 | NOAA-21 | SELVÍRIA | MATO GROSSO DO SUL | Brasil | 5007802 | 50 | 33 | nan | nan | nan | Cerrado | 2.5 |
| fa8e2a84-1995-3311-8ee0-a83f36170d72 | -16.56529 | -43.99798 | 2026-09-18 04:23:00 | NOAA-21 | MONTES CLAROS | MINAS GERAIS | Brasil | 3143302 | 31 | 33 | nan | nan | nan | Cerrado | 2.4 |
| f50cd413-59c9-3c51-aa8d-e305af0fa234 | -19.28659 | -50.36887 | 2026-09-18 04:23:00 | NOAA-21 | UNIÃO DE MINAS | MINAS GERAIS | Brasil | 3170438 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| d4db9c99-997e-35c7-af37-749f05716c35 | -19.55387 | -47.63897 | 2026-09-18 04:23:00 | NOAA-21 | NOVA PONTE | MINAS GERAIS | Brasil | 3145000 | 31 | 33 | nan | nan | nan | Cerrado | 10.1 |
| 9c6a640d-d452-3c6a-9f95-e0c39d21e2ec | -19.19175 | -48.7924 | 2026-09-18 04:23:00 | NOAA-21 | PRATA | MINAS GERAIS | Brasil | 3152808 | 31 | 33 | nan | nan | nan | Cerrado | 7.0 |
| 45f34354-22d6-3128-8fbc-dbed526a3d86 | -19.44252 | -47.56728 | 2026-09-18 04:23:00 | NOAA-21 | SANTA JULIANA | MINAS GERAIS | Brasil | 3157708 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 9efec383-e144-30ce-a139-a60fa50a4eb4 | -17.00005 | -45.46711 | 2026-09-18 04:23:00 | NOAA-21 | BURITIZEIRO | MINAS GERAIS | Brasil | 3109402 | 31 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 0dc5073d-672d-3db7-893b-3de7e2388a0e | -19.18472 | -48.77219 | 2026-09-18 04:23:00 | NOAA-21 | PRATA | MINAS GERAIS | Brasil | 3152808 | 31 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 54976178-ef7f-34da-9f29-762887e27b98 | -19.18295 | -48.78327 | 2026-09-18 04:23:00 | NOAA-21 | PRATA | MINAS GERAIS | Brasil | 3152808 | 31 | 33 | nan | nan | nan | Cerrado | 11.5 |
| 0f8bcc6e-9349-3fe6-8a34-72233d68cd13 | -21.46256 | -48.67809 | 2026-09-18 04:23:00 | NOAA-21 | TAQUARITINGA | SÃO PAULO | Brasil | 3553708 | 35 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 4c13ec59-e31f-3397-a338-03b3718fb1d8 | -21.03995 | -48.46722 | 2026-09-18 04:23:00 | NOAA-21 | BEBEDOURO | SÃO PAULO | Brasil | 3506102 | 35 | 33 | nan | nan | nan | Cerrado | 1.0 |
| a49dd993-d2c3-37b5-9ce4-95eb25966a07 | -15.99864 | -46.97593 | 2026-09-18 04:23:00 | NOAA-21 | CABECEIRA GRANDE | MINAS GERAIS | Brasil | 3109451 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| e34f6495-d9db-3cb2-9eeb-9d2171c61954 | -16.85813 | -45.4301 | 2026-09-18 04:23:00 | NOAA-21 | SANTA FÉ DE MINAS | MINAS GERAIS | Brasil | 3157609 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| fae81007-cf43-3a66-855c-a57db5f8a031 | -17.83639 | -44.84996 | 2026-09-18 04:23:00 | NOAA-21 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 6.1 |
| f86d76cd-ecff-3d42-886b-be26d07c7c37 | -16.55869 | -43.99259 | 2026-09-18 04:23:00 | NOAA-21 | MONTES CLAROS | MINAS GERAIS | Brasil | 3143302 | 31 | 33 | nan | nan | nan | Cerrado | 4.8 |
| f2d3a441-7f76-38ae-8d45-4459cbab7f3e | -21.04987 | -48.46898 | 2026-09-18 04:23:00 | NOAA-21 | BEBEDOURO | SÃO PAULO | Brasil | 3506102 | 35 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 96386ba5-3318-3ffc-964a-259e899fc124 | -25.90145 | -52.26974 | 2026-09-18 04:25:00 | NOAA-21 | MANGUEIRINHA | PARANÁ | Brasil | 4114401 | 41 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| a40ab07f-49ab-3fa5-af25-f06cf447a45b | -28.51803 | -50.55888 | 2026-09-18 04:25:00 | NOAA-21 | BOM JESUS | RIO GRANDE DO SUL | Brasil | 4302303 | 43 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 2595b673-7afc-31ba-b56e-f8ae2412fda2 | -27.71771 | -50.91948 | 2026-09-18 04:25:00 | NOAA-21 | ANITA GARIBALDI | SANTA CATARINA | Brasil | 4201000 | 42 | 33 | nan | nan | nan | Mata Atlântica | 1.9 |
| 65088c7e-d7b6-32d6-b2ea-9e51ad09084b | -28.35109 | -52.18401 | 2026-09-18 04:25:00 | NOAA-21 | MARAU | RIO GRANDE DO SUL | Brasil | 4311809 | 43 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| 9fc4644b-3e73-39e3-9bf3-72da4a71be12 | -28.19101 | -50.08549 | 2026-09-18 04:25:00 | NOAA-21 | SÃO JOAQUIM | SANTA CATARINA | Brasil | 4216503 | 42 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| b97f94a1-16ad-3690-89d9-864fff25dbbd | -22.24471 | -52.88729 | 2026-09-18 04:25:00 | NOAA-21 | ANAURILÂNDIA | MATO GROSSO DO SUL | Brasil | 5000807 | 50 | 33 | nan | nan | nan | Mata Atlântica | 4.3 |
| 29b5cedf-882f-396c-8110-7bf28fb32e42 | -21.85336 | -50.73814 | 2026-09-18 04:25:00 | NOAA-21 | PARAPUÃ | SÃO PAULO | Brasil | 3536000 | 35 | 33 | nan | nan | nan | Mata Atlântica | 3.1 |
| 392fd405-daf2-3060-ae5d-246d183dbdb3 | -28.34769 | -52.1833 | 2026-09-18 04:25:00 | NOAA-21 | MARAU | RIO GRANDE DO SUL | Brasil | 4311809 | 43 | 33 | nan | nan | nan | Mata Atlântica | 4.0 |
| 3f314f8e-dc9d-365f-8e27-2ccdcee05618 | 4.00301 | -51.64841 | 2026-09-18 04:53:00 | NPP-375D | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 2c47bff0-e673-342c-91c4-130e020e8bee | 3.97167 | -51.69452 | 2026-09-18 04:53:00 | NPP-375D | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 4e41bf80-ff03-343d-b957-c1f24b831a22 | 2.51296 | -50.84824 | 2026-09-18 04:53:00 | NPP-375D | CALÇOENE | AMAPÁ | Brasil | 1600204 | 16 | 33 | nan | nan | nan | Amazônia | 2.0 |
| a2ce26da-14d4-3600-a159-0e1c1f844353 | 2.51638 | -50.84771 | 2026-09-18 04:53:00 | NPP-375D | CALÇOENE | AMAPÁ | Brasil | 1600204 | 16 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 0a19ff9b-77cb-3ed9-a2d0-134b7939d7b2 | 4.10985 | -60.6683 | 2026-09-18 04:53:00 | NPP-375D | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 9396794d-8f74-31b8-83bc-8efac4007bea | 4.0066 | -51.64786 | 2026-09-18 04:53:00 | NPP-375D | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 0.8 |
| ab1616f8-6d20-3b32-82db-bda38ba070b8 | 4.10908 | -60.66299 | 2026-09-18 04:53:00 | NPP-375D | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 4.0 |
| f4256d03-b265-3b36-80fb-bf4a8074d8b5 | -4.4497 | -55.47723 | 2026-09-18 04:55:00 | NPP-375D | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 7a6ff61e-6833-3606-97c3-8dfe3965a73b | -1.49579 | -54.97617 | 2026-09-18 04:55:00 | NPP-375D | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 782224cf-8d9b-3078-a29e-527881244ff3 | -4.27563 | -55.55357 | 2026-09-18 04:55:00 | NPP-375D | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| dab0a903-f0f8-395b-89a6-68fd81596db8 | -2.82102 | -50.46853 | 2026-09-18 04:55:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 32.9 |
| 0210973f-5e54-3cb7-9f32-21feef6a7e6a | -4.43082 | -55.51716 | 2026-09-18 04:55:00 | NPP-375D | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| ef25f3cb-b0b5-351b-8ec1-af6526fce848 | -4.50705 | -54.97709 | 2026-09-18 04:55:00 | NPP-375D | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| b1b5a391-ff50-35d0-b18f-ce26b7f3ecae | -5.65175 | -43.38545 | 2026-09-18 04:55:00 | NPP-375D | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 348da639-d0d0-3c22-81f4-92c575b40936 | -3.49465 | -43.31303 | 2026-09-18 04:55:00 | NPP-375D | URBANO SANTOS | MARANHÃO | Brasil | 2112605 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| c02b127a-053e-3c0b-84d5-3a6864ec21cf | -4.55214 | -42.95437 | 2026-09-18 04:55:00 | NPP-375D | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 64996039-aaa6-3560-976c-d86708414478 | -2.35868 | -55.23528 | 2026-09-18 04:55:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| bd8ef148-d021-3e68-a1da-1222dc39389a | -3.38242 | -50.4516 | 2026-09-18 04:55:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 54a6a794-9598-38b0-967c-a05e78bb84b8 | -4.56913 | -42.94039 | 2026-09-18 04:55:00 | NPP-375D | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 4.2 |
| a548a490-7060-3b12-9b5f-f0edf0c49dbe | -3.07747 | -51.20084 | 2026-09-18 04:55:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 057d3add-0d7b-3342-b775-763bc9d6ad68 | -2.83541 | -48.65215 | 2026-09-18 04:55:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| d1b687fd-4f07-3d83-bbb5-193e7cbba912 | -3.04608 | -51.37655 | 2026-09-18 04:55:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 4a4cc4f9-9e21-3403-b007-981ed0e5277b | -4.55293 | -42.94904 | 2026-09-18 04:55:00 | NPP-375D | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 90559483-4713-3210-80ca-d17306c9e3e0 | -3.1632 | -48.60824 | 2026-09-18 04:55:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| fa46fcba-e3e5-3a39-b88b-5219681bff12 | -3.56905 | -43.47262 | 2026-09-18 04:55:00 | NPP-375D | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 71beb2e0-36c2-3982-b780-1511fb509add | -2.70305 | -57.60785 | 2026-09-18 04:55:00 | NPP-375D | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 6cd1b733-10a1-3d4a-af8f-e5ac4f7eb558 | -3.02484 | -51.33696 | 2026-09-18 04:55:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 4359977a-2b49-36d6-8d01-269181f39634 | -4.43471 | -55.07899 | 2026-09-18 04:55:00 | NPP-375D | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| c28fccf2-3752-3bc2-b32c-5aefa9ca113e | -1.37901 | -49.36408 | 2026-09-18 04:55:00 | NPP-375D | MUANÁ | PARÁ | Brasil | 1504901 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| be4a04cf-b134-302f-b820-666e6b052772 | -4.4126 | -42.31377 | 2026-09-18 04:55:00 | NPP-375D | CABECEIRAS DO PIAUÍ | PIAUÍ | Brasil | 2202059 | 22 | 33 | nan | nan | nan | Caatinga | 0.6 |
| 16d2eadd-bef4-365e-8525-b74e621018d6 | -4.36346 | -47.7824 | 2026-09-18 04:55:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 5.7 |
| 819f639b-d758-3dfb-b570-55571ce073fa | -3.36248 | -50.44847 | 2026-09-18 04:55:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 50a36d25-2097-3dcb-9a8e-a4160b0a6ad7 | -3.37245 | -50.45004 | 2026-09-18 04:55:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| ea657699-2e83-3417-be0d-33af26b7a4a9 | -2.89608 | -54.17669 | 2026-09-18 04:55:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| b59d0f7a-de0e-3231-afe4-70a957126f12 | -5.62769 | -40.86434 | 2026-09-18 04:55:00 | NPP-375D | NOVO ORIENTE | CEARÁ | Brasil | 2309409 | 23 | 33 | nan | nan | nan | Caatinga | 1.1 |
| ff4e468e-882a-3b5e-bb15-347b79771d69 | -3.36139 | -50.45538 | 2026-09-18 04:55:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 6.3 |
| 0ccd92fa-8dcf-309e-8f0f-aee8be2499f4 | -2.89534 | -54.18126 | 2026-09-18 04:55:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 884fe6e2-638b-3e90-8a73-69c415589af1 | -1.14831 | -54.16934 | 2026-09-18 04:55:00 | NPP-375D | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| acd5b010-a26c-3551-bba4-a3a3c9d761d9 | -5.5844 | -48.10715 | 2026-09-18 04:55:00 | NPP-375D | ARAGUATINS | TOCANTINS | Brasil | 1702208 | 17 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 98931a31-c399-30c0-9572-b8181c4c7f34 | -2.61103 | -54.75138 | 2026-09-18 04:55:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 12.1 |
| 2590f31f-1a6c-3065-93c1-3f250dec3ad3 | -1.78838 | -47.83419 | 2026-09-18 04:55:00 | NPP-375D | SÃO DOMINGOS DO CAPIM | PARÁ | Brasil | 1507201 | 15 | 33 | nan | nan | nan | Amazônia | 7.7 |
| dfce36b9-58e0-3010-a3a7-bc60bec394da | -3.91985 | -55.74282 | 2026-09-18 04:55:00 | NPP-375D | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 80cad6f5-a8ec-3e8d-95c3-4b7e13d705a3 | -3.3791 | -50.45108 | 2026-09-18 04:55:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 6af47146-f0ce-3882-b81a-17cfe8a1b89f | -4.56739 | -54.90641 | 2026-09-18 04:55:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 9048bbc6-bf36-33b2-b789-10f56c295974 | -3.73356 | -52.27594 | 2026-09-18 04:55:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| e4c1a483-bcfc-328d-ba98-08e790294e16 | -6.34855 | -43.37524 | 2026-09-18 04:55:00 | NPP-375D | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 7.3 |
| 6fec5ca6-cb6f-312f-bdcb-eb98a406c73c | 1.20512 | -50.76913 | 2026-09-18 04:55:00 | NPP-375D | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 7fe5ab5e-368d-3065-87d3-4e1159cfb051 | -3.48352 | -54.7241 | 2026-09-18 04:55:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 9325649b-586f-3406-8278-ecdbe9383b99 | -3.04048 | -51.36843 | 2026-09-18 04:55:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 7.0 |


[Clique aqui para ver as próximas entradas](README53.md)
