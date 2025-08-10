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

## Dados Diários - Página 30

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 0ce554b7-d808-320c-8a36-4da7d00aa949 | -6.93428 | -42.9269 | 2025-08-10 12:12:00 | TERRA_M-T | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 10.3 |
| 27b96a19-fba3-3963-b235-de82260165ad | -7.30159 | -39.63663 | 2025-08-10 12:12:00 | TERRA_M-T | SANTANA DO CARIRI | CEARÁ | Brasil | 2312106 | 23 | 33 | nan | nan | nan | Caatinga | 50.1 |
| 063ae082-45d4-39ac-af45-f5a0cf028206 | -5.82738 | -44.1055 | 2025-08-10 12:12:00 | TERRA_M-T | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 21.5 |
| c24b5580-5c7f-3552-85a9-157926b32927 | -3.99083 | -47.89281 | 2025-08-10 12:12:00 | TERRA_M-T | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 7.6 |
| 15ca490e-badb-3a9b-94e8-25f1dda026ad | -5.84915 | -38.25587 | 2025-08-10 12:12:00 | TERRA_M-T | IRACEMA | CEARÁ | Brasil | 2306009 | 23 | 33 | nan | nan | nan | Caatinga | 22.9 |
| 314bce7f-f4e9-34e2-a1ec-88cdc16a6368 | -7.29943 | -39.65289 | 2025-08-10 12:12:00 | TERRA_M-T | SANTANA DO CARIRI | CEARÁ | Brasil | 2312106 | 23 | 33 | nan | nan | nan | Caatinga | 49.0 |
| 7ec7016a-c349-3363-ba47-a0d1d01021f7 | -6.87162 | -43.17439 | 2025-08-10 12:12:00 | TERRA_M-T | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 9.8 |
| ef876638-2b20-39cb-9a0f-0c262e696fad | -6.76102 | -44.34328 | 2025-08-10 12:12:00 | TERRA_M-T | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 11.6 |
| 83861956-c147-365d-97b2-681edded8c56 | -6.06247 | -43.74969 | 2025-08-10 12:12:00 | TERRA_M-T | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 6.5 |
| 73412105-668d-3353-bb91-a1e42c582d7a | -5.8512 | -38.24142 | 2025-08-10 12:12:00 | TERRA_M-T | IRACEMA | CEARÁ | Brasil | 2306009 | 23 | 33 | nan | nan | nan | Caatinga | 18.2 |
| 3879f7ba-d448-36d2-aa5d-d9ed1a69a070 | -6.7975 | -44.3548 | 2025-08-10 12:12:00 | TERRA_M-T | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 16.0 |
| 2d63fc4f-36ec-3c14-8f98-7bb0d7aeb031 | -6.93565 | -42.91711 | 2025-08-10 12:12:00 | TERRA_M-T | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 16.0 |
| 86dd1143-8bdd-3b8e-ab65-224bcf020dc6 | -5.82865 | -44.0966 | 2025-08-10 12:12:00 | TERRA_M-T | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 0e6e8433-2ea8-3e3e-93db-16b7fd1c479d | -6.24549 | -42.78311 | 2025-08-10 12:12:00 | TERRA_M-T | AMARANTE | PIAUÍ | Brasil | 2200509 | 22 | 33 | nan | nan | nan | Caatinga | 15.6 |
| 4928fc82-76af-36e8-99d0-087967fa2da1 | -6.67756 | -44.73682 | 2025-08-10 12:12:00 | TERRA_M-T | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 6.7 |
| dfece00c-26e6-3681-942b-6c33adce3bf6 | -3.28383 | -42.91724 | 2025-08-10 12:12:00 | TERRA_M-T | SANTA QUITÉRIA DO MARANHÃO | MARANHÃO | Brasil | 2110104 | 21 | 33 | nan | nan | nan | Cerrado | 10.9 |
| 874e7b7e-fedc-3301-b2da-963afdedef15 | -2.8175 | -42.43521 | 2025-08-10 12:12:00 | TERRA_M-T | TUTÓIA | MARANHÃO | Brasil | 2112506 | 21 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 69c1242b-967b-340a-b9e9-4caac9fc0a58 | -5.53726 | -43.22421 | 2025-08-10 12:12:00 | TERRA_M-T | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 60.8 |
| ce1e35d7-149e-3cbc-a6a8-97175b1ce54f | -6.67883 | -44.72801 | 2025-08-10 12:12:00 | TERRA_M-T | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 6d996347-d891-3083-b97a-ada5fe33d868 | -5.53594 | -43.23345 | 2025-08-10 12:12:00 | TERRA_M-T | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 1b9b03cf-bf0d-3e1a-9a5d-95c70a40d97d | -5.6825 | -41.40475 | 2025-08-10 12:12:00 | TERRA_M-T | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 24.0 |
| d1a496c8-710b-3fa1-bbaa-acba1cf3af80 | -6.56675 | -42.85172 | 2025-08-10 12:12:00 | TERRA_M-T | AMARANTE | PIAUÍ | Brasil | 2200509 | 22 | 33 | nan | nan | nan | Caatinga | 6.9 |
| ef13537e-a82a-3544-ab03-843a443ebede | -5.68091 | -41.41624 | 2025-08-10 12:12:00 | TERRA_M-T | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 11.2 |
| c29f04d4-d000-3a40-88a2-e862a0d85b55 | -4.301 | -48.0745 | 2025-08-10 12:12:00 | TERRA_M-T | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 9.8 |
| 625c9f98-7aaf-3bc8-9c97-f342748ebea7 | -11.74387 | -45.03737 | 2025-08-10 12:14:00 | TERRA_M-T | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 17.9 |
| bcd74a13-8ddc-30ff-bdf6-559fbb68b82e | -9.49811 | -46.28854 | 2025-08-10 12:14:00 | TERRA_M-T | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 24.4 |
| ecd15335-b332-3820-af6f-75a16f5e1b72 | -8.77937 | -46.40365 | 2025-08-10 12:14:00 | TERRA_M-T | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 78.0 |
| 0eddbfb2-f1f5-36af-b09d-a097b2c9b5ad | -14.30081 | -51.98732 | 2025-08-10 12:14:00 | TERRA_M-T | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 18.3 |
| d77ebe58-6508-3c05-bfec-629005a2f0f2 | -10.35226 | -46.6337 | 2025-08-10 12:14:00 | TERRA_M-T | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 28.6 |
| 261343d1-2a28-3493-b83c-366c2e49152a | -11.48625 | -50.28518 | 2025-08-10 12:14:00 | TERRA_M-T | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 14.1 |
| af7e6f35-9f11-3b35-b116-940423338cc5 | -12.57493 | -47.14835 | 2025-08-10 12:14:00 | TERRA_M-T | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 5.9 |
| a97596fa-03bb-338d-b5bc-4b648081b16a | -7.43034 | -43.98671 | 2025-08-10 12:14:00 | TERRA_M-T | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 6.5 |
| df680a8b-5fc7-3060-99b1-e4aeb3794128 | -12.71743 | -46.36151 | 2025-08-10 12:14:00 | TERRA_M-T | AURORA DO TOCANTINS | TOCANTINS | Brasil | 1702703 | 17 | 33 | nan | nan | nan | Cerrado | 7.6 |
| bde9e619-ec49-3549-beb8-79f03633c4bb | -17.64408 | -44.22824 | 2025-08-10 12:14:00 | TERRA_M-T | FRANCISCO DUMONT | MINAS GERAIS | Brasil | 3126604 | 31 | 33 | nan | nan | nan | Cerrado | 11.2 |
| 3daeece3-1a2a-3aff-aad6-2835f847c164 | -7.39098 | -46.49347 | 2025-08-10 12:14:00 | TERRA_M-T | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 6.4 |
| 59567207-98b6-39d0-8c58-47f262bb6d0a | -7.10795 | -44.4346 | 2025-08-10 12:14:00 | TERRA_M-T | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 6.1 |
| 98714db2-e37d-3436-a1de-a3e4b51bae2d | -7.59995 | -44.42287 | 2025-08-10 12:14:00 | TERRA_M-T | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 44229192-0401-3d63-99e5-6ffe45357182 | -7.2807 | -44.57971 | 2025-08-10 12:14:00 | TERRA_M-T | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 2b1c2c02-3076-355d-bf83-dc4d2657cee4 | -8.75682 | -40.7781 | 2025-08-10 12:14:00 | TERRA_M-T | PETROLINA | PERNAMBUCO | Brasil | 2611101 | 26 | 33 | nan | nan | nan | Caatinga | 14.1 |
| c4ef3a7d-1154-3931-95bb-7eccaeff66be | -16.58612 | -46.97489 | 2025-08-10 12:14:00 | TERRA_M-T | UNAÍ | MINAS GERAIS | Brasil | 3170404 | 31 | 33 | nan | nan | nan | Cerrado | 4.4 |
| dfedfe53-62c3-3170-932d-f7d908fa6f0c | -13.63734 | -48.98549 | 2025-08-10 12:14:00 | TERRA_M-T | SANTA TEREZA DE GOIÁS | GOIÁS | Brasil | 5219605 | 52 | 33 | nan | nan | nan | Cerrado | 11.5 |
| 7dcb9009-aea5-3aa6-ab4c-02cdc2fcb2dd | -8.8841 | -44.79017 | 2025-08-10 12:14:00 | TERRA_M-T | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 10.2 |
| 59f5086f-45d4-3060-9703-df2db4e1674d | -14.01306 | -44.13844 | 2025-08-10 12:14:00 | TERRA_M-T | FEIRA DA MATA | BAHIA | Brasil | 2910776 | 29 | 33 | nan | nan | nan | Cerrado | 20.0 |
| ae9715d0-72c0-3d40-a089-284f4c65b82e | -6.95261 | -44.56046 | 2025-08-10 12:14:00 | TERRA_M-T | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 8.6 |
| 08356063-cc4f-3ca5-b6eb-2d22c1506f31 | -7.12204 | -44.20948 | 2025-08-10 12:14:00 | TERRA_M-T | ANTÔNIO ALMEIDA | PIAUÍ | Brasil | 2200806 | 22 | 33 | nan | nan | nan | Cerrado | 10.3 |
| 28c4c0e8-aec7-3c1e-8d0b-6afc09af6aa3 | -11.10106 | -50.45956 | 2025-08-10 12:14:00 | TERRA_M-T | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 23.9 |
| 795e927e-3afd-32fb-96f5-024ad8b30ceb | -7.4482 | -43.98919 | 2025-08-10 12:14:00 | TERRA_M-T | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 249.5 |
| 815d3860-1a4e-3099-91c0-a1711be307a4 | -7.3482 | -45.26802 | 2025-08-10 12:14:00 | TERRA_M-T | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 27.6 |
| 36552622-e54e-381a-8e56-cd7c3a7782af | -13.58963 | -44.89052 | 2025-08-10 12:14:00 | TERRA_M-T | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 3926ce91-d9bf-3bfc-a422-50f4060a9b36 | -8.37197 | -46.9769 | 2025-08-10 12:14:00 | TERRA_M-T | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 10.0 |
| 667156bb-dd98-3420-9c69-f3420c6e3332 | -7.12077 | -44.21842 | 2025-08-10 12:14:00 | TERRA_M-T | ANTÔNIO ALMEIDA | PIAUÍ | Brasil | 2200806 | 22 | 33 | nan | nan | nan | Cerrado | 10.9 |
| fb1fb031-83b2-3be2-a488-700198d2120f | -7.67288 | -44.8105 | 2025-08-10 12:14:00 | TERRA_M-T | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 11.7 |
| 0d398204-806b-3551-b79b-b928f64ef3fb | -16.58744 | -46.96575 | 2025-08-10 12:14:00 | TERRA_M-T | UNAÍ | MINAS GERAIS | Brasil | 3170404 | 31 | 33 | nan | nan | nan | Cerrado | 7.2 |
| ca56374e-6e03-31b7-8d0a-6f424a8db7bb | -6.95387 | -44.55161 | 2025-08-10 12:14:00 | TERRA_M-T | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 14.7 |
| a478bb9e-202d-3770-be34-2f42167bf2fd | -14.11623 | -45.41104 | 2025-08-10 12:14:00 | TERRA_M-T | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 26.6 |
| 3f00e8f6-224f-368e-9b67-b676450f4a21 | -13.58831 | -44.90001 | 2025-08-10 12:14:00 | TERRA_M-T | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 7.0 |
| ecc9618e-26ea-3d85-8478-91bd0a05c299 | -14.12516 | -45.41232 | 2025-08-10 12:14:00 | TERRA_M-T | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 9.2 |
| 54de0617-a412-3999-9e0e-1aa6e951ccfe | -11.74256 | -45.04658 | 2025-08-10 12:14:00 | TERRA_M-T | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 10.2 |
| 30d5259e-75e0-3a31-a5ec-5b589391dac3 | -8.76908 | -46.4115 | 2025-08-10 12:14:00 | TERRA_M-T | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 10.2 |
| 555b7564-932e-3e54-bcb8-0b51c5b510c1 | -7.60122 | -44.41392 | 2025-08-10 12:14:00 | TERRA_M-T | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 28.0 |
| 6e8baf07-ac2c-33f6-a18b-56c5c4c7a97e | -8.81883 | -40.81456 | 2025-08-10 12:14:00 | TERRA_M-T | PETROLINA | PERNAMBUCO | Brasil | 2611101 | 26 | 33 | nan | nan | nan | Caatinga | 15.5 |
| 7ffc98d5-5cc2-392b-8b44-f458ca05d937 | -8.77042 | -46.40234 | 2025-08-10 12:14:00 | TERRA_M-T | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 35.7 |
| df7874cd-c557-38fc-9ee1-1bbc5b24d217 | -13.95182 | -46.36694 | 2025-08-10 12:14:00 | TERRA_M-T | GUARANI DE GOIÁS | GOIÁS | Brasil | 5209408 | 52 | 33 | nan | nan | nan | Cerrado | 5.8 |
| 3e7d43ab-c483-3ed9-a9cc-789d68700651 | -14.01169 | -44.14874 | 2025-08-10 12:14:00 | TERRA_M-T | FEIRA DA MATA | BAHIA | Brasil | 2910776 | 29 | 33 | nan | nan | nan | Cerrado | 15.6 |
| 225f509d-12a2-3d7d-9bc8-6045be8ee9a6 | -7.44056 | -43.97889 | 2025-08-10 12:14:00 | TERRA_M-T | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 131.7 |
| 07bbaf9a-b530-3452-919a-ee75d88d6603 | -11.73366 | -45.04531 | 2025-08-10 12:14:00 | TERRA_M-T | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 224.6 |
| 4ffe5d9b-c9b3-31d5-8ed9-2f0ae2bebae0 | -10.96026 | -44.84893 | 2025-08-10 12:14:00 | TERRA_M-T | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 4.6 |
| f187b575-1221-35ed-a859-5ef2d7184c24 | -9.37396 | -48.22897 | 2025-08-10 12:14:00 | TERRA_M-T | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 9.4 |
| 107f5b8d-9c43-385c-9671-be82509634b3 | -8.50311 | -44.748 | 2025-08-10 12:14:00 | TERRA_M-T | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 8.1 |
| 6b594401-8dad-303c-9d97-e7edd2d656d4 | -10.35359 | -46.62468 | 2025-08-10 12:14:00 | TERRA_M-T | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 19.5 |
| d11434d3-f518-35ca-9a20-9ab9598e5696 | -15.73093 | -48.39072 | 2025-08-10 12:14:00 | TERRA_M-T | COCALZINHO DE GOIÁS | GOIÁS | Brasil | 5205513 | 52 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 1b8cf782-3694-3013-bfd7-060fbf46d6ad | -10.87581 | -42.37098 | 2025-08-10 12:14:00 | TERRA_M-T | ITAGUAÇU DA BAHIA | BAHIA | Brasil | 2915353 | 29 | 33 | nan | nan | nan | Caatinga | 7.8 |
| 15e9b8fb-15be-3d96-b21e-9889bfe7a088 | -14.12646 | -45.40303 | 2025-08-10 12:14:00 | TERRA_M-T | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 10.2 |
| 0f8fb866-6521-3f70-ac78-34befe499ed0 | -7.43928 | -43.98792 | 2025-08-10 12:14:00 | TERRA_M-T | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 185.2 |
| 406c97be-e60b-344e-af37-18c60718e0b6 | -14.10987 | -45.39118 | 2025-08-10 12:14:00 | TERRA_M-T | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 117.5 |
| 1c28a9ae-91c3-33da-b8f9-3bf8c9c28ae1 | -13.613 | -46.93258 | 2025-08-10 12:14:00 | TERRA_M-T | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 10.4 |
| 89837081-d89c-3833-9612-bdb1b6494d22 | -12.5575 | -47.07357 | 2025-08-10 12:14:00 | TERRA_M-T | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 15.7 |
| abcb2c43-c56d-3395-8e97-df97d6362f3b | -13.63577 | -48.9957 | 2025-08-10 12:14:00 | TERRA_M-T | SANTA TEREZA DE GOIÁS | GOIÁS | Brasil | 5219605 | 52 | 33 | nan | nan | nan | Cerrado | 6.5 |
| 19871e4d-c70d-34bb-bcde-03ca60b15ca1 | -7.38804 | -48.13282 | 2025-08-10 12:14:00 | TERRA_M-T | ARAGUAÍNA | TOCANTINS | Brasil | 1702109 | 17 | 33 | nan | nan | nan | Cerrado | 9.2 |
| fb618487-c8e8-32df-a0dd-c77e97851338 | -11.64718 | -50.22506 | 2025-08-10 12:14:00 | TERRA_M-T | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 15.3 |
| 45d2a3e6-17de-323d-8a2a-4c3844df2111 | -7.92518 | -40.11589 | 2025-08-10 12:14:00 | TERRA_M-T | OURICURI | PERNAMBUCO | Brasil | 2609907 | 26 | 33 | nan | nan | nan | Caatinga | 20.0 |
| 791991d8-91b9-3a7d-b1cc-ee00fd2e468d | -17.6426 | -44.23954 | 2025-08-10 12:14:00 | TERRA_M-T | FRANCISCO DUMONT | MINAS GERAIS | Brasil | 3126604 | 31 | 33 | nan | nan | nan | Cerrado | 5.9 |
| af016156-1694-3e7d-bf23-fc1640160a6b | -12.71613 | -46.37049 | 2025-08-10 12:14:00 | TERRA_M-T | AURORA DO TOCANTINS | TOCANTINS | Brasil | 1702703 | 17 | 33 | nan | nan | nan | Cerrado | 8.4 |
| be90f7b3-b706-398b-b3cd-7ff7f9b4f556 | -8.50184 | -44.75689 | 2025-08-10 12:14:00 | TERRA_M-T | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 10.8 |
| 5e2408d4-50d8-3e29-9808-0ebc88663f7d | -9.49942 | -46.27952 | 2025-08-10 12:14:00 | TERRA_M-T | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 17.6 |
| 9f4e5456-c060-372a-8734-e35f3f70fa88 | -7.38974 | -48.12145 | 2025-08-10 12:14:00 | TERRA_M-T | ARAGUAÍNA | TOCANTINS | Brasil | 1702109 | 17 | 33 | nan | nan | nan | Cerrado | 9.7 |
| 16f366d8-b511-3132-9a4f-622390a918fb | -7.60424 | -45.28717 | 2025-08-10 12:14:00 | TERRA_M-T | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 6.5 |
| d657628d-330f-3c57-ad8c-982f9ab699cc | -7.8889 | -43.54738 | 2025-08-10 12:14:00 | TERRA_M-T | CANAVIEIRA | PIAUÍ | Brasil | 2202251 | 22 | 33 | nan | nan | nan | Cerrado | 9.6 |
| fbaa24b6-cc61-3102-9a58-60872befecb7 | -7.71238 | -45.4893 | 2025-08-10 12:14:00 | TERRA_M-T | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 57b7fe82-4008-36bf-899c-2909d62400e9 | -8.88537 | -44.78127 | 2025-08-10 12:14:00 | TERRA_M-T | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 13.3 |
| 4f79fec8-78d4-3b38-b4d3-2d781458ba18 | -7.34243 | -44.60386 | 2025-08-10 12:14:00 | TERRA_M-T | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 6.6 |
| 059ab913-1be4-31b9-818c-1b56bde39cda | -8.46989 | -46.93893 | 2025-08-10 12:14:00 | TERRA_M-T | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 6.8 |
| b4f2b51c-590c-3b37-8a59-5673900f9232 | -9.53429 | -45.40339 | 2025-08-10 12:14:00 | TERRA_M-T | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 7.4 |
| c3ec85f3-2f64-3701-87b8-1110b983182f | -7.67161 | -44.81933 | 2025-08-10 12:14:00 | TERRA_M-T | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 11.7 |
| cef25823-8d13-3528-a290-60cfd028e149 | -14.11752 | -45.40175 | 2025-08-10 12:14:00 | TERRA_M-T | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 55.5 |
| bc75d49e-e14a-3e88-9725-4a865262618e | -7.44341 | -43.76474 | 2025-08-10 12:14:00 | TERRA_M-T | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 8.3 |
| c020cc16-8f75-3fb0-a494-8fa8582028ab | -14.10858 | -45.40047 | 2025-08-10 12:14:00 | TERRA_M-T | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 103.8 |
| 59cc2759-a182-3b73-a68d-f2a27394955d | -11.78525 | -44.94665 | 2025-08-10 12:14:00 | TERRA_M-T | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 1960006a-31fa-32f2-8bfa-da1c8ab1aa01 | -8.77804 | -46.41279 | 2025-08-10 12:14:00 | TERRA_M-T | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 26.6 |
| 8b83e487-5005-3970-9e84-9ae071a30c66 | -11.73497 | -45.03607 | 2025-08-10 12:14:00 | TERRA_M-T | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 64.0 |


[Clique aqui para ver as próximas entradas](README31.md)
