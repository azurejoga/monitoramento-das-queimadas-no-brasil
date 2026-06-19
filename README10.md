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

## Dados Diários - Página 10

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 15cce497-249a-359e-8059-d2bfa9a873b2 | -12.84016 | -44.3709 | 2026-06-19 05:04:00 | NPP-375D | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 8.5 |
| c9f7377f-4909-3125-b400-77c774118b9b | -13.96422 | -47.38008 | 2026-06-19 05:04:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 86d277f7-f0f3-3484-9988-7b1fd4bcbf56 | -12.91434 | -49.48555 | 2026-06-19 05:04:00 | NPP-375D | ARAGUAÇU | TOCANTINS | Brasil | 1702000 | 17 | 33 | nan | nan | nan | Cerrado | 0.5 |
| b04e1bbe-fa10-3ace-a9ed-3d33566b0520 | -12.78471 | -44.50463 | 2026-06-19 05:04:00 | NPP-375D | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| b0f1755e-9863-33a8-941c-581ed26faeb0 | -11.48437 | -52.92203 | 2026-06-19 05:04:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| a379d176-b0c4-32b8-b79f-7a0ca2c246f4 | -12.78628 | -44.50613 | 2026-06-19 05:04:00 | NPP-375D | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| ce08db59-9792-36a9-ac43-9f71da00052e | -12.86868 | -44.37077 | 2026-06-19 05:04:00 | NPP-375D | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 10.6 |
| 5acbea08-aeea-3951-a9f5-7e6bc8c7e8cc | -13.93934 | -53.56033 | 2026-06-19 05:04:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 12.0 |
| ebf7c214-5230-3e75-8d27-6842e3659613 | -18.97805 | -52.45079 | 2026-06-19 05:04:00 | NPP-375D | CASSILÂNDIA | MATO GROSSO DO SUL | Brasil | 5002902 | 50 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 38f97f7a-58ed-333d-b5b2-6bca658fc8dc | -12.49401 | -43.7715 | 2026-06-19 05:04:00 | NPP-375D | BREJOLÂNDIA | BAHIA | Brasil | 2904407 | 29 | 33 | nan | nan | nan | Cerrado | 6.7 |
| 9748352e-bc4f-3919-a7f5-24c95299569c | -12.77199 | -44.53033 | 2026-06-19 05:04:00 | NPP-375D | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 0e870914-8fe5-37dd-ad08-557bb85308b5 | -12.79027 | -44.50534 | 2026-06-19 05:04:00 | NPP-375D | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 59d4fd48-b6d8-3d1d-837f-bb21590d69ce | -17.11097 | -49.75573 | 2026-06-19 05:04:00 | NPP-375D | CEZARINA | GOIÁS | Brasil | 5205455 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 2373e05d-8e5a-32ee-9ec0-0e32462f574a | -17.10734 | -49.75111 | 2026-06-19 05:04:00 | NPP-375D | CEZARINA | GOIÁS | Brasil | 5205455 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| dce14447-887f-3e6d-8148-6d376523d543 | -12.50031 | -43.76807 | 2026-06-19 05:04:00 | NPP-375D | BREJOLÂNDIA | BAHIA | Brasil | 2904407 | 29 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 91076f0c-4337-39af-bd11-a49026e1bfeb | -11.62561 | -55.18186 | 2026-06-19 05:04:00 | NPP-375D | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 123ba27d-ace1-3331-8331-ade3bfdb3098 | -11.71978 | -54.49364 | 2026-06-19 05:04:00 | NPP-375D | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 6795df06-aba0-3c00-b0cf-591d718ad016 | -12.14024 | -48.26762 | 2026-06-19 05:04:00 | NPP-375D | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 5f2aff19-382d-32d6-a67e-551125e9cade | -17.34747 | -53.81384 | 2026-06-19 05:04:00 | NPP-375D | SONORA | MATO GROSSO DO SUL | Brasil | 5007935 | 50 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 493d526a-3973-3cb2-9535-896fa32a9e7d | -15.73407 | -55.69537 | 2026-06-19 05:04:00 | NPP-375D | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Cerrado | 0.3 |
| 815ae896-7ca5-3257-ac9d-730f5c12a1fa | -12.54875 | -54.58253 | 2026-06-19 05:04:00 | NPP-375D | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 6cf6aebd-14dd-3efc-939d-cf8600e86eca | -12.87051 | -44.35559 | 2026-06-19 05:04:00 | NPP-375D | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 74eb8bd4-b571-3ef7-9771-037bc37d5248 | -13.32313 | -45.17431 | 2026-06-19 05:04:00 | NPP-375D | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 45b94554-4e98-3bac-9f23-edfe4b4c483b | -14.07719 | -59.4546 | 2026-06-19 05:04:00 | NPP-375D | NOVA LACERDA | MATO GROSSO | Brasil | 5106182 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 3bd673c5-cb17-3fe1-9b0e-e327803a5bb8 | -12.78072 | -44.5054 | 2026-06-19 05:04:00 | NPP-375D | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 00706420-8894-3250-9d58-3cdb420fc788 | -12.8743 | -44.37142 | 2026-06-19 05:04:00 | NPP-375D | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 10.6 |
| c7889fba-c493-302d-8210-930847cf1952 | -18.98168 | -52.45137 | 2026-06-19 05:04:00 | NPP-375D | CASSILÂNDIA | MATO GROSSO DO SUL | Brasil | 5002902 | 50 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 2ad40547-4e37-3f2d-8146-24713f14e2db | -18.9768 | -52.45968 | 2026-06-19 05:04:00 | NPP-375D | CASSILÂNDIA | MATO GROSSO DO SUL | Brasil | 5002902 | 50 | 33 | nan | nan | nan | Cerrado | 0.4 |
| c283da53-2fcd-3839-840a-746ce165bc97 | -17.31492 | -43.64626 | 2026-06-19 05:04:00 | NPP-375D | OLHOS-D'ÁGUA | MINAS GERAIS | Brasil | 3145455 | 31 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 7a684c99-7ad7-3e7f-9347-2e04b480ce7a | -11.35717 | -52.95761 | 2026-06-19 05:04:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 265516dd-727f-35b8-b7bf-4bf4bdfe59b8 | -18.97742 | -52.45525 | 2026-06-19 05:04:00 | NPP-375D | CASSILÂNDIA | MATO GROSSO DO SUL | Brasil | 5002902 | 50 | 33 | nan | nan | nan | Cerrado | 0.6 |
| da5df3de-f813-3b46-b789-b18f5187a845 | -11.52145 | -54.25791 | 2026-06-19 05:04:00 | NPP-375D | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 285194ad-ef04-3dc3-9f88-a09b2b3ba75e | -13.93823 | -53.56759 | 2026-06-19 05:04:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 9.7 |
| a196f72d-5478-38fe-a850-f42d86119ca6 | -17.35484 | -53.81117 | 2026-06-19 05:04:00 | NPP-375D | SONORA | MATO GROSSO DO SUL | Brasil | 5007935 | 50 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 4be5abfe-eedd-3f6e-9cc8-bd64a02938ef | -12.78582 | -44.5098 | 2026-06-19 05:04:00 | NPP-375D | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 6a99289d-b1dc-3be1-bc5e-3813968bd468 | -13.31903 | -45.16339 | 2026-06-19 05:04:00 | NPP-375D | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 449b02e0-c0b7-307c-a95e-df4eab7610a7 | -12.15385 | -48.45175 | 2026-06-19 05:04:00 | NPP-375D | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| ca5de5a7-9c9c-3794-a866-1b4465026d77 | -14.94983 | -52.87162 | 2026-06-19 05:04:00 | NPP-375D | NOVO SÃO JOAQUIM | MATO GROSSO | Brasil | 5106281 | 51 | 33 | nan | nan | nan | Cerrado | 0.7 |
| bc8d92e4-6a65-335b-b4ae-ae87e96b9bb4 | -17.34691 | -53.8176 | 2026-06-19 05:04:00 | NPP-375D | SONORA | MATO GROSSO DO SUL | Brasil | 5007935 | 50 | 33 | nan | nan | nan | Cerrado | 0.9 |
| ca9d01b8-171c-3cad-bb64-bd365105e2eb | -16.02264 | -43.427 | 2026-06-19 05:04:00 | NPP-375D | JANAÚBA | MINAS GERAIS | Brasil | 3135100 | 31 | 33 | nan | nan | nan | Cerrado | 10.1 |
| 99734786-4e53-319f-8d50-c650fc34cb87 | -12.68718 | -54.57952 | 2026-06-19 05:04:00 | NPP-375D | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| ebc6d7bd-dae5-3573-944b-a41b689a1bfb | -12.87338 | -44.37901 | 2026-06-19 05:04:00 | NPP-375D | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 30.5 |
| 20a6b32f-ca8b-352b-aac4-e34883635dbf | -12.7923 | -44.50312 | 2026-06-19 05:04:00 | NPP-375D | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| d3a64576-c393-3c40-a5f7-5a4d44be0adc | -22.78303 | -49.35027 | 2026-06-19 05:06:00 | NPP-375D | AGUDOS | SÃO PAULO | Brasil | 3500709 | 35 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 133954b0-8825-35ef-95b6-6c006acf5b01 | -21.27113 | -56.03406 | 2026-06-19 05:06:00 | NPP-375D | NIOAQUE | MATO GROSSO DO SUL | Brasil | 5005806 | 50 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 7960750a-4361-34c4-b431-174fa777e0c4 | -22.78358 | -49.34532 | 2026-06-19 05:06:00 | NPP-375D | ÁGUAS DE SANTA BÁRBARA | SÃO PAULO | Brasil | 3500550 | 35 | 33 | nan | nan | nan | Cerrado | 1.5 |
| a4ed5992-5c7a-3129-92cf-4f3f4a3bc844 | -22.8026 | -49.34242 | 2026-06-19 05:06:00 | NPP-375D | ÁGUAS DE SANTA BÁRBARA | SÃO PAULO | Brasil | 3500550 | 35 | 33 | nan | nan | nan | Cerrado | 1.5 |
| f0f37900-a2e4-349a-a822-d7677fe2f171 | -19.48593 | -52.71741 | 2026-06-19 05:06:00 | NPP-375D | PARAÍSO DAS ÁGUAS | MATO GROSSO DO SUL | Brasil | 5006275 | 50 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 5c5d3d92-39c8-3dba-82d5-2d91f1f3e21c | -19.48654 | -52.71303 | 2026-06-19 05:06:00 | NPP-375D | PARAÍSO DAS ÁGUAS | MATO GROSSO DO SUL | Brasil | 5006275 | 50 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 3ef151ee-b125-3dc5-a9e4-a4ea5a06ab9c | -22.78248 | -49.35526 | 2026-06-19 05:06:00 | NPP-375D | AGUDOS | SÃO PAULO | Brasil | 3500709 | 35 | 33 | nan | nan | nan | Cerrado | 1.3 |
| aa529f30-f192-3572-a67c-9d900b91a428 | -19.49016 | -52.71357 | 2026-06-19 05:06:00 | NPP-375D | PARAÍSO DAS ÁGUAS | MATO GROSSO DO SUL | Brasil | 5006275 | 50 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 8d7d5e6a-c309-3f1f-ab54-da24c3830bde | -22.78819 | -49.34587 | 2026-06-19 05:06:00 | NPP-375D | ÁGUAS DE SANTA BÁRBARA | SÃO PAULO | Brasil | 3500550 | 35 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 884a5c21-6723-320b-b227-4f5ef36805f4 | -19.741 | -53.54842 | 2026-06-19 05:06:00 | NPP-375D | CAMAPUÃ | MATO GROSSO DO SUL | Brasil | 5002605 | 50 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 1110cf27-b3c0-3627-8f56-1d2ecec1b0b6 | -21.08629 | -55.76564 | 2026-06-19 05:06:00 | NPP-375D | NIOAQUE | MATO GROSSO DO SUL | Brasil | 5005806 | 50 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 918eda1a-9466-333e-8abc-fffbd0e1442a | -19.48955 | -52.71795 | 2026-06-19 05:06:00 | NPP-375D | PARAÍSO DAS ÁGUAS | MATO GROSSO DO SUL | Brasil | 5006275 | 50 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 7f9e65aa-c789-36ea-b8c5-622807081dae | -21.08571 | -55.76937 | 2026-06-19 05:06:00 | NPP-375D | NIOAQUE | MATO GROSSO DO SUL | Brasil | 5005806 | 50 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 8f95bf70-7b12-38dd-8f3e-4f5a450749a0 | -21.27054 | -56.03777 | 2026-06-19 05:06:00 | NPP-375D | NIOAQUE | MATO GROSSO DO SUL | Brasil | 5005806 | 50 | 33 | nan | nan | nan | Cerrado | 1.1 |
| e5e3e9b7-cb42-3139-9006-5c2f60be58ba | -19.49316 | -52.7185 | 2026-06-19 05:06:00 | NPP-375D | PARAÍSO DAS ÁGUAS | MATO GROSSO DO SUL | Brasil | 5006275 | 50 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 0c46445a-2883-3663-87ed-8479f276a15e | -12.8736 | -44.3828 | 2026-06-19 05:10:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 98.5 |
| bac0306e-9cf0-3cdb-a65a-9b2e0c352d3f | -12.8741 | -44.3593 | 2026-06-19 05:10:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 114.8 |
| 28a5ce57-90cb-34a1-915d-8b3ad4336035 | -12.8741 | -44.3593 | 2026-06-19 05:20:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 119.7 |
| bd40fec1-3ed4-3fea-8078-66acd3fb8061 | -12.8736 | -44.3828 | 2026-06-19 05:20:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 91.0 |
| 5be5f350-3a61-3f67-aa21-8d7553609c41 | -7.80152 | -46.45155 | 2026-06-19 05:21:00 | NOAA-20 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 26386f14-45d9-3313-8c02-b4b07a8e61be | -8.90749 | -46.96064 | 2026-06-19 05:21:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 45cc852c-695e-3ff5-8868-48df67df6477 | -6.93584 | -51.9362 | 2026-06-19 05:21:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 2a57806a-f558-34f7-be10-ad311e8acf7a | -7.35425 | -49.8598 | 2026-06-19 05:21:00 | NOAA-20 | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 7565b29e-50d9-3c0e-90b6-74c1140c211f | -8.90821 | -46.95481 | 2026-06-19 05:21:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 23c52296-6970-39b7-9cda-43787af03878 | -3.85379 | -54.2248 | 2026-06-19 05:21:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 6e7cdc97-9afd-3439-bd0e-1baae8445f3b | -7.35768 | -49.85962 | 2026-06-19 05:21:00 | NOAA-20 | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 824d5ad4-7962-395c-b561-34a6aa6dcd7c | -3.84996 | -54.2242 | 2026-06-19 05:21:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 54992d2d-76c7-3704-8c02-0f068d0c52cd | -7.79703 | -46.45265 | 2026-06-19 05:21:00 | NOAA-20 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 6fe8383d-25ec-3078-b944-7e945d1a3f53 | -7.8336 | -55.4038 | 2026-06-19 05:21:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 32a31701-7360-3fc2-9393-75677849dc81 | -7.35718 | -49.86313 | 2026-06-19 05:21:00 | NOAA-20 | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 6b2ae9a2-1941-30a7-8ffc-7e7cd319fda0 | -8.90892 | -46.94897 | 2026-06-19 05:21:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 0cdbd81c-c567-31d3-a52d-08990a5f14c8 | -8.9115 | -46.95135 | 2026-06-19 05:21:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 185c2030-b63b-3ae9-8a54-55256ac7e313 | -7.83291 | -55.40835 | 2026-06-19 05:21:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| dee4c1df-a883-3f37-9e74-09900ece34f4 | -8.91226 | -46.94549 | 2026-06-19 05:21:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 44ee4a61-b3d3-36de-a756-10c6e463b881 | -6.93515 | -51.94096 | 2026-06-19 05:21:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 8c219a2d-2c5c-345e-8830-d633e3fda380 | -8.91074 | -46.95718 | 2026-06-19 05:21:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 2aab9fb8-1fe7-369a-aa09-c68252f36b63 | -8.90964 | -46.9431 | 2026-06-19 05:21:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 3.6 |
| cd929965-d0f8-3dc1-8a32-110be1fb9d70 | -7.3592 | -49.8641 | 2026-06-19 05:21:00 | NOAA-20 | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 352003e5-fa29-3c20-bdb6-84676a8ce005 | -7.35966 | -49.86061 | 2026-06-19 05:21:00 | NOAA-20 | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 4c9ccc9e-e8c6-3568-95ef-9d49b7f834a7 | -8.90406 | -46.95655 | 2026-06-19 05:21:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 43f8a9b7-d277-383f-a561-3c793f350940 | -6.93808 | -51.9384 | 2026-06-19 05:21:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| be34fd0f-5fd2-322f-98ca-4056bc5cc8d5 | -7.82983 | -55.40324 | 2026-06-19 05:21:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 81aa69fc-fe3d-3d81-bffe-4236761ea0a1 | -7.35472 | -49.85627 | 2026-06-19 05:21:00 | NOAA-20 | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 4fd15c43-d23a-3c63-991c-5874df9494b7 | -7.80375 | -46.45394 | 2026-06-19 05:21:00 | NOAA-20 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 0e7bcf76-0aa6-3bc7-bd5b-db68a154a9e3 | -7.80075 | -46.45734 | 2026-06-19 05:21:00 | NOAA-20 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 10ab14b5-03ad-3964-a102-ebcddc1c8c7c | -13.64434 | -55.29132 | 2026-06-19 05:23:00 | NOAA-20 | SANTA RITA DO TRIVELATO | MATO GROSSO | Brasil | 5107768 | 51 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 29fba7ab-adfd-375d-9c6e-480378523317 | -12.91627 | -49.48573 | 2026-06-19 05:23:00 | NOAA-20 | ARAGUAÇU | TOCANTINS | Brasil | 1702000 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 4913e7a3-eec0-32a7-bdc7-e3ac732fe7fb | -10.55234 | -46.33776 | 2026-06-19 05:23:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 4bd737dd-30e4-3e4e-b923-f0b0b8b91e3a | -10.90701 | -54.13785 | 2026-06-19 05:23:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 44b8a749-42ea-3d6a-b006-bd38496cabbf | -11.31093 | -51.41737 | 2026-06-19 05:23:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 5cef87ad-7063-38b5-b0b6-f1be05301846 | -10.98283 | -47.74599 | 2026-06-19 05:23:00 | NOAA-20 | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 46a838e9-6201-33df-949f-3ceb5c06e5ad | -10.5516 | -46.34433 | 2026-06-19 05:23:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 4.0 |
| e563fa1e-7bef-326c-8dfe-2f3d6c88e861 | -10.12348 | -56.81846 | 2026-06-19 05:23:00 | NOAA-20 | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 44bde3c3-74ab-31d3-81e8-468073b63038 | -11.35664 | -55.82267 | 2026-06-19 05:23:00 | NOAA-20 | SINOP | MATO GROSSO | Brasil | 5107909 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| a93a7630-89fe-30cf-aa98-8775281a39b2 | -11.71964 | -54.49219 | 2026-06-19 05:23:00 | NOAA-20 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 24f19a8f-eb3b-3a25-b35e-ceb4559ff7f4 | -10.15744 | -56.61814 | 2026-06-19 05:23:00 | NOAA-20 | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 2cf9163e-71cd-3ca5-aea1-3f9c480e139a | -18.82936 | -51.47471 | 2026-06-19 05:23:00 | NOAA-20 | ITARUMÃ | GOIÁS | Brasil | 5211305 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |


[Clique aqui para ver as próximas entradas](README11.md)
