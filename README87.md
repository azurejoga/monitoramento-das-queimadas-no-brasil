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

## Dados Diários - Página 87

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 4273e399-24a6-3b76-864f-885a1c14e87a | -9.3755 | -50.1779 | 2026-09-15 15:40:00 | GOES-19 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 73.4 |
| 6f90f0cc-1777-36b1-9be1-1d32254ad9eb | -10.2926 | -45.3161 | 2026-09-15 15:40:00 | GOES-19 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 182.7 |
| 0eedb30c-5ed4-3c47-8cef-03832eebabb1 | -2.6785 | -57.5115 | 2026-09-15 15:40:00 | GOES-19 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 63.2 |
| c1bcbdbd-f27a-3b96-8f00-f290a123a2bc | -9.3577 | -50.0943 | 2026-09-15 15:40:00 | GOES-19 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 71.6 |
| c7861180-0d1e-39b3-8716-204718f08c52 | -9.4931 | -56.7564 | 2026-09-15 15:40:00 | GOES-19 | PARANAÍTA | MATO GROSSO | Brasil | 5106299 | 51 | 33 | nan | nan | nan | Amazônia | 49.0 |
| 14fb70dd-0ba5-3ac4-8895-7c015eac5497 | -10.5924 | -57.3151 | 2026-09-15 15:40:00 | GOES-19 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 51.2 |
| 824393b5-f182-3cad-a638-c4afbdda44ef | -8.8361 | -62.489 | 2026-09-15 15:40:00 | GOES-19 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 70.4 |
| c03a9393-9759-34e2-80e3-a8d8f534ea9d | 3.9353 | -59.6446 | 2026-09-15 15:40:00 | GOES-19 | NORMANDIA | RORAIMA | Brasil | 1400407 | 14 | 33 | nan | nan | nan | Amazônia | 87.5 |
| e2a49246-9751-39e6-8ad6-6600c6f2c7cb | -9.7687 | -46.1067 | 2026-09-15 15:40:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 87.7 |
| 923e5f8c-68fd-3a61-91d5-c8328e29b767 | -8.2966 | -62.9268 | 2026-09-15 15:40:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 55.9 |
| ba7e6868-4210-312a-9396-19ad04f009a3 | -10.312 | -45.2907 | 2026-09-15 15:40:00 | GOES-19 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 97.1 |
| a7086714-ee49-3690-9500-1f9b8cb13b47 | -8.8456 | -45.8939 | 2026-09-15 15:40:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 88.4 |
| ecc76e71-10ff-370d-8c43-650bcbca94c6 | -9.1337 | -65.844 | 2026-09-15 15:40:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 70.2 |
| f5f281a6-b6de-3afc-8f9f-cf79972d8a85 | -7.5582 | -44.9116 | 2026-09-15 15:40:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 85.2 |
| 8cbfb8d8-60e3-3b9e-a4d1-041da9e436f7 | -15.5779 | -53.8451 | 2026-09-15 15:40:00 | GOES-19 | GENERAL CARNEIRO | MATO GROSSO | Brasil | 5103908 | 51 | 33 | nan | nan | nan | Cerrado | 40.2 |
| 753ee0c8-2023-3ed7-b464-b3fdd1c6404a | -10.6962 | -47.4953 | 2026-09-15 15:40:00 | GOES-19 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 83.7 |
| 8ceb18af-4a2f-32db-ad35-06937d1cd89a | -13.4273 | -54.6195 | 2026-09-15 15:40:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 66.5 |
| cefeb64a-79f7-3b6a-8f8e-8975871e94bc | -15.597 | -53.8636 | 2026-09-15 15:40:00 | GOES-19 | GENERAL CARNEIRO | MATO GROSSO | Brasil | 5103908 | 51 | 33 | nan | nan | nan | Cerrado | 38.8 |
| 1a30acb9-cef9-32a2-ba29-db0eee6b0815 | 1.0951 | -50.9778 | 2026-09-15 15:40:00 | GOES-19 | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 89.7 |
| 3f532443-6271-3aa5-bb4d-687af6047504 | -7.5397 | -44.8905 | 2026-09-15 15:40:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 100.4 |
| 225d8ce2-7ab7-3028-9ec1-c55200f6bcf3 | -8.3902 | -62.7152 | 2026-09-15 15:40:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 46.0 |
| 89dfca83-4cd7-3d38-920b-9b6aeb99fdd7 | -8.7889 | -45.8999 | 2026-09-15 15:40:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 77.3 |
| c532c26e-f880-36f4-8077-c372ed1b8fad | -8.8459 | -45.8713 | 2026-09-15 15:40:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 200.0 |
| 430d1a97-3a51-3267-b66f-46617945b8ed | -2.6601 | -57.5702 | 2026-09-15 15:40:00 | GOES-19 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 57.8 |
| c603e250-6452-3a50-a730-ea3e3e2f1cd6 | -8.6191 | -44.4588 | 2026-09-15 15:40:00 | GOES-19 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 191.2 |
| c3ca365c-78f0-343e-9f3c-0a0c7c29ba22 | -9.7358 | -47.0958 | 2026-09-15 15:40:00 | GOES-19 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 108.7 |
| 44c6faf8-5d4c-3eeb-b892-fe9b20a38e78 | -15.3598 | -52.989 | 2026-09-15 15:40:00 | GOES-19 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 71.2 |
| 280b5a91-2a66-363c-bf27-cc344c804907 | -14.1822 | -51.7653 | 2026-09-15 15:40:00 | GOES-19 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 77.0 |
| 42c98f3d-c742-310f-9009-be269ffc9b53 | -3.7237 | -57.1969 | 2026-09-15 15:40:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 102.0 |
| 21896218-b202-306d-b0b3-cc0e0eb0bb1f | -8.638 | -44.4567 | 2026-09-15 15:40:00 | GOES-19 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 522.2 |
| 7873ec5d-5b70-3d7e-86bb-31e5dc6dea2e | 1.0951 | -50.957 | 2026-09-15 15:40:00 | GOES-19 | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 86.5 |
| db02b2eb-95b0-3190-a95a-523967192cb0 | -9.1337 | -65.8253 | 2026-09-15 15:40:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 74.5 |
| b501fe62-b29b-3d3d-bbf7-00853c328480 | -10.792 | -46.2071 | 2026-09-15 15:40:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 184.2 |
| 46ab2597-b9fe-3c6a-9e14-502025beac22 | -2.6603 | -57.4924 | 2026-09-15 15:40:00 | GOES-19 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 62.2 |
| 62847255-391d-3ad2-8a6a-37023f89920b | -15.5195 | -53.8527 | 2026-09-15 15:40:00 | GOES-19 | GENERAL CARNEIRO | MATO GROSSO | Brasil | 5103908 | 51 | 33 | nan | nan | nan | Cerrado | 85.6 |
| b4f8830f-2a8a-3c31-88ac-a6fb65f681b2 | -3.1816 | -61.1045 | 2026-09-15 15:40:00 | GOES-19 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 86.2 |
| fcbeff5a-97fe-37c4-ad2f-cd37ee9cd009 | -15.5584 | -53.8477 | 2026-09-15 15:40:00 | GOES-19 | GENERAL CARNEIRO | MATO GROSSO | Brasil | 5103908 | 51 | 33 | nan | nan | nan | Cerrado | 45.7 |
| 024e2d08-1348-3957-b51b-e611fae5d192 | -10.6112 | -57.3138 | 2026-09-15 15:40:00 | GOES-19 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 64.9 |
| 7bf84b45-9b31-3b4d-8270-cf74af2f134d | 1.0767 | -50.9572 | 2026-09-15 15:50:00 | GOES-19 | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 78.2 |
| 359f29d0-5831-3406-896b-69b56a3a7bcf | -15.5977 | -53.8216 | 2026-09-15 15:50:00 | GOES-19 | GENERAL CARNEIRO | MATO GROSSO | Brasil | 5103908 | 51 | 33 | nan | nan | nan | Cerrado | 34.4 |
| 6cbf1ac5-c027-32bb-a394-c1694349072c | -2.6601 | -57.5702 | 2026-09-15 15:50:00 | GOES-19 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 48.6 |
| 658acba9-d661-3be5-a196-0073e084bfc8 | -7.5582 | -44.9116 | 2026-09-15 15:50:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 77.1 |
| d491ba89-0d55-3489-89f3-053b026f0101 | -9.1337 | -65.844 | 2026-09-15 15:50:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 72.9 |
| 861a3364-defc-3504-bd86-678bb8eb08b0 | -8.3902 | -62.7152 | 2026-09-15 15:50:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 47.8 |
| eefa145a-eca4-3a52-82f7-8ed30082ab5c | -10.6417 | -46.0906 | 2026-09-15 15:50:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 115.5 |
| 035d4528-8bf2-34ba-80cc-21111a7aa792 | -15.6168 | -53.8401 | 2026-09-15 15:50:00 | GOES-19 | GENERAL CARNEIRO | MATO GROSSO | Brasil | 5103908 | 51 | 33 | nan | nan | nan | Cerrado | 29.1 |
| c310e0e9-20a6-30a2-94ea-60061e727fa5 | -13.414 | -57.0225 | 2026-09-15 15:50:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Cerrado | 134.6 |
| ddd2e552-cdc3-3ef7-bcd9-f45193eeb63a | -10.5924 | -57.3151 | 2026-09-15 15:50:00 | GOES-19 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 61.3 |
| 2e0252c4-2fea-3178-b25a-accb1b59f9ee | -10.2926 | -45.3161 | 2026-09-15 15:50:00 | GOES-19 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 97.8 |
| 187a7d32-eba8-37a0-892f-aad77e6503b4 | -13.3946 | -57.0444 | 2026-09-15 15:50:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Cerrado | 42.3 |
| d47a3462-c624-3a1f-b4bc-5debbf94eb01 | -15.5779 | -53.8451 | 2026-09-15 15:50:00 | GOES-19 | GENERAL CARNEIRO | MATO GROSSO | Brasil | 5103908 | 51 | 33 | nan | nan | nan | Cerrado | 54.8 |
| 092cc73e-2f71-3451-a2ac-48613c106444 | -14.1822 | -51.7653 | 2026-09-15 15:50:00 | GOES-19 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 71.2 |
| 42613707-26ff-3a31-b245-7da7a1b7bbbc | 1.0952 | -50.9363 | 2026-09-15 15:50:00 | GOES-19 | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 58.7 |
| 2abd3d2b-d004-3aae-a1b2-6b31badaf98b | -2.6785 | -57.5115 | 2026-09-15 15:50:00 | GOES-19 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 61.5 |
| c0c356b4-e920-3c0e-810e-dfc9cbe665e4 | -9.7687 | -46.1067 | 2026-09-15 15:50:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 125.7 |
| 659fdc36-2d55-37ca-b946-b46a4e006abf | -5.1256 | -55.9352 | 2026-09-15 15:50:00 | GOES-19 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 222.7 |
| 34f7a978-402f-3b9a-8cd1-a458d822b482 | -9.3572 | -50.137 | 2026-09-15 15:50:00 | GOES-19 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 105.4 |
| 7eeed7d5-04a8-3ffe-8c65-cd6685b0949f | 2.2187 | -50.8977 | 2026-09-15 15:50:00 | GOES-19 | CALÇOENE | AMAPÁ | Brasil | 1600204 | 16 | 33 | nan | nan | nan | Amazônia | 85.1 |
| b8d7fbb1-2b16-342e-ab68-428c3338561c | -6.0169 | -52.1614 | 2026-09-15 15:50:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 56.1 |
| 0653c1d9-12fa-3687-b2b3-6bfb4c532f4f | -2.6968 | -57.5112 | 2026-09-15 15:50:00 | GOES-19 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 46.0 |
| 8dcd7571-5617-32e6-b400-2464beba8a89 | -13.4273 | -54.6195 | 2026-09-15 15:50:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 68.3 |
| 6e73e31b-5049-3ab2-8312-6cbd3cc28c7d | -3.3676 | -59.8285 | 2026-09-15 15:50:00 | GOES-19 | CAREIRO | AMAZONAS | Brasil | 1301100 | 13 | 33 | nan | nan | nan | Amazônia | 57.5 |
| d855b6da-a2e8-3990-8d31-857ba32c0d32 | -10.792 | -46.2071 | 2026-09-15 15:50:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 85.2 |
| 2bef8403-a987-3e72-b4d1-d6a4d1c360cc | -10.312 | -45.2907 | 2026-09-15 15:50:00 | GOES-19 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 112.9 |
| 2f2e29f3-ba0a-3a72-b169-a44d548a9f14 | -3.1997 | -61.1799 | 2026-09-15 15:50:00 | GOES-19 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 57.1 |
| 794a5931-2ca9-36bf-afc4-3d8b85fb6d21 | -1.2268 | -49.1899 | 2026-09-15 15:50:00 | GOES-19 | MUANÁ | PARÁ | Brasil | 1504901 | 15 | 33 | nan | nan | nan | Amazônia | 59.6 |
| ba0da0e2-b993-3387-8c42-d5b75fce285b | -9.3575 | -50.1156 | 2026-09-15 15:50:00 | GOES-19 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 92.3 |
| 00a66030-eaf9-3720-a411-fc43977c734e | 1.0951 | -50.957 | 2026-09-15 15:50:00 | GOES-19 | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 84.0 |
| 7cde6d57-baa0-3086-baa8-83ebe6f01130 | -2.6603 | -57.4924 | 2026-09-15 15:50:00 | GOES-19 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 58.4 |
| bfb30a94-7d9c-3e82-a410-8b2e4ded0985 | -3.1998 | -61.161 | 2026-09-15 15:50:00 | GOES-19 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 54.4 |
| 3a184052-e3f5-3051-8a9e-945c17c73b1e | -2.6603 | -57.4924 | 2026-09-15 16:00:00 | GOES-19 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 55.8 |
| 9f9cdb2b-b165-3027-8644-3d81c631b5e1 | -15.5584 | -53.8477 | 2026-09-15 16:00:00 | GOES-19 | GENERAL CARNEIRO | MATO GROSSO | Brasil | 5103908 | 51 | 33 | nan | nan | nan | Cerrado | 54.5 |
| 69049ba1-0130-30b9-bfdf-3728e7b71ba5 | -1.2268 | -49.1899 | 2026-09-15 16:00:00 | GOES-19 | MUANÁ | PARÁ | Brasil | 1504901 | 15 | 33 | nan | nan | nan | Amazônia | 63.1 |
| 252c5aa3-8068-30c9-8d0b-0de8a992cc77 | -14.1822 | -51.7653 | 2026-09-15 16:00:00 | GOES-19 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 69.7 |
| 0cac8361-b305-3e3a-a412-697faec554c5 | -2.6968 | -57.5112 | 2026-09-15 16:00:00 | GOES-19 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 47.5 |
| 1be5d77e-7a7c-3d0e-82ca-ba9651407753 | -9.1337 | -65.8253 | 2026-09-15 16:00:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 118.5 |
| de8152be-4af3-3487-916e-5c8a385b4d79 | 2.6904 | -60.2971 | 2026-09-15 16:00:00 | GOES-19 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 53.6 |
| 8d19d5f7-0d6b-3aa5-8f5b-f64fbd2ea59f | -9.7687 | -46.1067 | 2026-09-15 16:00:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 97.7 |
| 7145c4d2-93e3-3e27-8c46-9fc9e70a2acf | -3.3676 | -59.8285 | 2026-09-15 16:00:00 | GOES-19 | CAREIRO | AMAZONAS | Brasil | 1301100 | 13 | 33 | nan | nan | nan | Amazônia | 69.4 |
| 1bdc0272-0ca7-3a2d-8bf1-b33eb64a3c13 | -2.9723 | -57.214 | 2026-09-15 16:00:00 | GOES-19 | BARREIRINHA | AMAZONAS | Brasil | 1300508 | 13 | 33 | nan | nan | nan | Amazônia | 42.6 |
| 1b5a3d62-b46f-3284-accd-8199ab2f9231 | -10.7535 | -46.2347 | 2026-09-15 16:00:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 97.6 |
| d2f7b790-a218-3ca2-aeb7-a9d71fdc60d9 | -10.2926 | -45.3161 | 2026-09-15 16:00:00 | GOES-19 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 92.2 |
| 7ed15212-1301-3567-89a3-f9f3c4125460 | -10.7726 | -46.2322 | 2026-09-15 16:00:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 220.9 |
| d1ed66ec-cb13-3089-af25-71ebca77d158 | -5.2537 | -59.9732 | 2026-09-15 16:00:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 224.4 |
| 0d32f15b-ed6c-3881-8d25-2292cb114d25 | -9.1523 | -65.8248 | 2026-09-15 16:00:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 53.6 |
| 7bc0fdcb-11ff-35cf-be5e-8cdd340e1a22 | -2.6785 | -57.5115 | 2026-09-15 16:00:00 | GOES-19 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 62.2 |
| 0bc4fa73-be23-3e8a-a990-16429dce4d94 | -3.7181 | -58.863 | 2026-09-15 16:00:00 | GOES-19 | NOVA OLINDA DO NORTE | AMAZONAS | Brasil | 1303106 | 13 | 33 | nan | nan | nan | Amazônia | 47.9 |
| 19affc3c-954e-3e58-87aa-25b2bb22977c | -8.8134 | -46.9272 | 2026-09-15 16:00:00 | GOES-19 | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 76.9 |
| 2b79306c-cf6a-3233-8cc3-f828b54d7a42 | -15.539 | -53.8502 | 2026-09-15 16:00:00 | GOES-19 | GENERAL CARNEIRO | MATO GROSSO | Brasil | 5103908 | 51 | 33 | nan | nan | nan | Cerrado | 64.2 |
| cd4542ec-1fde-375f-ac7f-1af3a1b79115 | -9.376 | -50.1352 | 2026-09-15 16:00:00 | GOES-19 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 97.8 |
| 6f69ca1b-76db-3b7d-86ba-9fd3374238d6 | -9.3941 | -50.1974 | 2026-09-15 16:00:00 | GOES-19 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 65.3 |
| e247b3cc-16ad-392b-a3c6-bdb66ad2217e | -8.638 | -44.4567 | 2026-09-15 16:00:00 | GOES-19 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 370.7 |
| 78dc9ffb-af65-3bd8-8ce6-2eb9c3d5dcdc | -3.7181 | -58.863 | 2026-09-15 16:10:00 | GOES-19 | NOVA OLINDA DO NORTE | AMAZONAS | Brasil | 1303106 | 13 | 33 | nan | nan | nan | Amazônia | 55.8 |
| 68f9695f-b9ab-3886-b544-c68a514edbaa | -12.1265 | -44.199 | 2026-09-15 16:10:00 | GOES-19 | CRISTÓPOLIS | BAHIA | Brasil | 2909703 | 29 | 33 | nan | nan | nan | Cerrado | 121.5 |
| 3f48fcca-62ff-3353-9a42-754890373b27 | -9.3941 | -50.1974 | 2026-09-15 16:10:00 | GOES-19 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 62.4 |
| 1d3a1d77-7b37-331f-8669-aae7cb26e6b4 | -9.7687 | -46.1067 | 2026-09-15 16:10:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 171.8 |
| c0e65fd9-20fe-31ae-83a5-12ed0bab891c | -3.7311 | -60.6018 | 2026-09-15 16:10:00 | GOES-19 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 42.6 |
| 8a25c7c5-c2ec-3008-b5da-c7b608cfb5fb | -8.638 | -44.4567 | 2026-09-15 16:10:00 | GOES-19 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 184.6 |
| f9ec2c9d-e375-370b-ab46-37f6ef3bd927 | -9.3572 | -50.137 | 2026-09-15 16:10:00 | GOES-19 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 120.6 |
| 081bafd1-388e-324e-b404-18b186a4e0c3 | -2.6968 | -57.5112 | 2026-09-15 16:10:00 | GOES-19 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 48.5 |


[Clique aqui para ver as próximas entradas](README88.md)
