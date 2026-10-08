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

## Dados Diários - Página 164

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| d5265de9-dc94-3ff3-bc30-3192e78c2e47 | -8.65368 | -67.17834 | 2026-10-08 05:23:00 | NPP-375D | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 5.5 |
| e8c124ca-4faf-3125-908e-76771d520502 | -1.12868 | -57.28135 | 2026-10-08 05:23:00 | NPP-375D | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| b7e46092-424c-318d-9838-ec855d06e220 | -4.26693 | -54.88343 | 2026-10-08 05:23:00 | NPP-375D | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 8fc1979d-abb8-352b-9b12-0bdf71a801e1 | -6.08835 | -55.72631 | 2026-10-08 05:23:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 2561aeab-8b7a-31d6-9e4e-abf0e9e56e3f | -3.18219 | -50.55505 | 2026-10-08 05:23:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 480dbd7c-d3af-3331-8063-c3e1c28a4637 | -3.29132 | -54.05325 | 2026-10-08 05:23:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 8fa261f8-0569-3a69-a2d2-12035ffd266c | -2.98635 | -54.08776 | 2026-10-08 05:23:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 1bb62aaa-37b9-3425-aa9a-c016879eb7a7 | -2.93337 | -54.15067 | 2026-10-08 05:23:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 1bd70267-e229-3497-a75b-6f4bec83e385 | -5.25571 | -55.91774 | 2026-10-08 05:23:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 87fa3f2d-8048-3aa1-8c92-816a2cd1b710 | -3.29652 | -54.06604 | 2026-10-08 05:23:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 0615ea1f-4a29-30c4-94a1-71d71a925a48 | -3.9867 | -59.2187 | 2026-10-08 05:23:00 | NPP-375D | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 9e19e80b-b057-3011-ae30-f86441afa92a | -3.30208 | -54.03082 | 2026-10-08 05:23:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 5c87b8ca-6b89-3a5e-847d-2175eb4c3404 | -4.08399 | -55.38203 | 2026-10-08 05:23:00 | NPP-375D | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 9245e623-e784-31ca-b637-17186f2599df | -3.63078 | -59.32196 | 2026-10-08 05:23:00 | NPP-375D | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| e569013a-d2ea-3248-a44d-381a8bea56b4 | -3.00764 | -54.76472 | 2026-10-08 05:23:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 015cfa26-5004-320c-a843-8e3ba10e8e0b | -10.49722 | -67.88765 | 2026-10-08 05:23:00 | NPP-375D | CAPIXABA | ACRE | Brasil | 1200179 | 12 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 7543d95e-cbdd-312f-aa8a-cc3136de6f53 | -3.29345 | -54.08549 | 2026-10-08 05:23:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 5b550951-43bb-3c37-9b12-a6a0d0788015 | -3.05638 | -54.21685 | 2026-10-08 05:23:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 166b443a-e828-319e-bee4-f8f878e34fe6 | -3.68273 | -55.93658 | 2026-10-08 05:23:00 | NPP-375D | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 48c097eb-bdef-38e9-ac1c-0df47493f7cf | -4.34305 | -55.12904 | 2026-10-08 05:23:00 | NPP-375D | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| fd451a78-ca6c-31b6-845b-ee041710fa22 | -3.99651 | -56.24585 | 2026-10-08 05:23:00 | NPP-375D | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| d2d84cc8-4437-3229-9467-8201194afbf1 | -3.57583 | -54.65727 | 2026-10-08 05:23:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 8d52b0dd-01b8-3722-b8ef-da2e80a68bf0 | -2.76464 | -54.09875 | 2026-10-08 05:23:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 353e7085-a311-3ee6-a254-e4a2636d27bb | -1.83016 | -54.99487 | 2026-10-08 05:23:00 | NPP-375D | CURUÁ | PARÁ | Brasil | 1502855 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 922a9b1a-0833-3671-aa25-3bf37596c302 | -9.4787 | -64.3616 | 2026-10-08 05:23:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 974d8a0e-8776-332a-b37f-748759509f5f | -3.13332 | -54.3682 | 2026-10-08 05:23:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 8df113c6-2c43-3b71-b58d-3a27a0cfce41 | -3.67719 | -55.95001 | 2026-10-08 05:23:00 | NPP-375D | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 24ad1528-2fce-3bd1-886b-b47a92e613c4 | -4.08311 | -55.33796 | 2026-10-08 05:23:00 | NPP-375D | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 2351407f-cccc-3c35-a40c-6688fb854aee | -3.13392 | -54.36441 | 2026-10-08 05:23:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 6d3d95d4-0991-32b1-85df-060d8b516c8c | -2.30192 | -58.11442 | 2026-10-08 05:23:00 | NPP-375D | SÃO SEBASTIÃO DO UATUMÃ | AMAZONAS | Brasil | 1303957 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| dbe962bd-945a-318d-b87c-fa48d8f49ca4 | -3.5371 | -54.66328 | 2026-10-08 05:23:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| eb5a145c-468f-3e56-9619-b9ba756ca105 | -3.20728 | -53.87582 | 2026-10-08 05:23:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| d9fc7179-829a-3ff9-b853-9c61cc4e26bc | -4.91601 | -55.86156 | 2026-10-08 05:23:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 132d026f-d064-3e41-8238-282cb29060cd | -3.58385 | -54.67379 | 2026-10-08 05:23:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 914feb57-7c6a-3b13-b706-2d1d828aae6d | -3.05805 | -54.22889 | 2026-10-08 05:23:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| df75a720-64b0-368c-9d58-c2ca7b59519e | -5.73336 | -45.16186 | 2026-10-08 05:23:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 891fade2-1a77-3c04-a18d-12a4fd107d82 | -2.58332 | -54.62128 | 2026-10-08 05:23:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| dc568a40-6f50-3342-abc3-1076fae9f44f | -6.09605 | -49.40783 | 2026-10-08 05:23:00 | NPP-375D | ELDORADO DO CARAJÁS | PARÁ | Brasil | 1502954 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| a69fc8ea-03b2-3bb2-86fc-8fba923dcebd | -3.2892 | -54.02082 | 2026-10-08 05:23:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 50a0aa75-56dd-31db-a025-6b237253a295 | -2.77152 | -54.08321 | 2026-10-08 05:23:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| dfe9c574-e229-3c91-86cd-b454426b228e | -3.31225 | -54.05531 | 2026-10-08 05:23:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 7d49fe70-6c8c-3133-a6b0-4b1ae830b214 | -3.58646 | -54.52042 | 2026-10-08 05:23:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 845b71fb-b77d-3162-990c-680f5a3d3a43 | -4.40397 | -49.95821 | 2026-10-08 05:23:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| cfb342bb-e932-3184-bcdb-60250a21f368 | -6.67037 | -55.09817 | 2026-10-08 05:23:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 8688df47-0bb7-3fb7-a963-3c52bac7558b | -2.51164 | -56.33161 | 2026-10-08 05:23:00 | NPP-375D | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| e4d36ecc-ee07-3987-841c-c1361212756c | -10.23235 | -58.22244 | 2026-10-08 05:23:00 | NPP-375D | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 071440c9-cb2a-3170-bd40-c810d788cda1 | -3.68613 | -57.00964 | 2026-10-08 05:23:00 | NPP-375D | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 0.5 |
| f261a956-4754-3671-b533-0b94acce55f3 | -2.97977 | -54.10656 | 2026-10-08 05:23:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| ddc55109-0a78-3190-b8a0-33a1118650cc | -5.11512 | -47.12379 | 2026-10-08 05:23:00 | NPP-375D | JOÃO LISBOA | MARANHÃO | Brasil | 2105500 | 21 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 725c5608-a017-3e01-98dc-69c92a424b48 | -3.00801 | -54.09098 | 2026-10-08 05:23:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 9.6 |
| d2f4bd54-c8ac-3848-9c35-3d33b65f52e0 | -3.0199 | -54.17579 | 2026-10-08 05:23:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 75651374-25d2-3042-aa62-6405518d8177 | -3.00699 | -54.0511 | 2026-10-08 05:23:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 9ae59b9c-092d-36ee-a0dd-97628dd12a74 | -2.85831 | -59.21299 | 2026-10-08 05:23:00 | NPP-375D | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| d50d41b3-0074-3202-b88f-71f27eaaf462 | -3.17526 | -50.5998 | 2026-10-08 05:23:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 8.3 |
| 4b1241fb-0e6f-3ced-8b2d-205c63ef6265 | -3.5147 | -59.21463 | 2026-10-08 05:23:00 | NPP-375D | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 2b928006-ead4-36c3-a9b7-d2712a1bacc9 | -6.13535 | -47.93593 | 2026-10-08 05:23:00 | NPP-375D | CACHOEIRINHA | TOCANTINS | Brasil | 1703826 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 5c699658-1d87-32b9-b9da-1cc919f5cf10 | -3.49965 | -59.28515 | 2026-10-08 05:23:00 | NPP-375D | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 67f660b9-276f-3e0b-9a5f-00e34b814d83 | -3.00364 | -54.79038 | 2026-10-08 05:23:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| f9e91abb-74a2-3e8e-850f-1ab11c0db338 | -3.30335 | -53.86124 | 2026-10-08 05:23:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| fed53c2f-8cce-3fe5-9725-a3e032f95f4a | -4.58434 | -54.92756 | 2026-10-08 05:23:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 22db62ab-c9c8-3de9-8689-876d385f4e35 | -5.85986 | -53.46659 | 2026-10-08 05:23:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| f52ba321-0a77-380a-bac3-6f5adbc99d34 | -4.30769 | -50.78569 | 2026-10-08 05:23:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 91305cda-0ce6-39e2-8874-0d4b0d2cd94e | -3.17184 | -58.63381 | 2026-10-08 05:23:00 | NPP-375D | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 87f75dd8-7bb1-320b-b328-e38df0ed326a | -3.51452 | -59.32829 | 2026-10-08 05:23:00 | NPP-375D | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 90eddbe4-0901-31c8-a270-cd4074568852 | -3.56378 | -59.48774 | 2026-10-08 05:23:00 | NPP-375D | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| fc6723e0-cf7f-3812-ac32-d0d8e5530bf4 | -2.85769 | -59.26204 | 2026-10-08 05:23:00 | NPP-375D | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| fca6fbc6-5bb5-3f57-b6d5-6e38b9746fe4 | -3.12985 | -54.36766 | 2026-10-08 05:23:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 7859281b-548b-3806-b655-255ecde3ddea | -2.99928 | -54.07772 | 2026-10-08 05:23:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 31.1 |
| 43cff9b4-0e49-3ae2-99f8-dc066004cd76 | -3.17519 | -54.7452 | 2026-10-08 05:23:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 15af47ab-d639-3f08-b992-397f7d11fd26 | -3.52902 | -54.66969 | 2026-10-08 05:23:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 8aff716f-6521-347a-9b8c-a89c6d8aac3f | -6.43714 | -60.05804 | 2026-10-08 05:23:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 9e1c299f-4ebb-3034-b07b-5d43be363ce6 | -2.45634 | -56.37954 | 2026-10-08 05:23:00 | NPP-375D | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 95d1f006-82ba-33a3-a1ab-298c942073c0 | -2.78962 | -54.08205 | 2026-10-08 05:23:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| bd6f6608-53bd-30a6-961a-0483b2aa0532 | -11.31817 | -46.68252 | 2026-10-08 05:23:00 | NPP-375D | RIO DA CONCEIÇÃO | TOCANTINS | Brasil | 1718659 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 49070154-c61a-38d7-9967-5ff9208592f5 | -3.36086 | -50.47352 | 2026-10-08 05:23:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 022ed35a-1229-3d70-91b5-f688f4879357 | -2.5663 | -56.1524 | 2026-10-08 05:23:00 | NPP-375D | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| be538b27-5e0a-35bc-90b3-27e0e5eb509e | -1.33219 | -56.4043 | 2026-10-08 05:23:00 | NPP-375D | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 41203ea7-8c38-35be-882b-378293db00a7 | -2.09982 | -52.06448 | 2026-10-08 05:23:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| a3a01333-8aa2-34c3-8a7c-a1c4f0eac771 | -3.72636 | -54.21974 | 2026-10-08 05:23:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| cb3f2ad2-e45a-3017-9000-8c943feb362f | -3.30955 | -54.05206 | 2026-10-08 05:23:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 9bd9ea1c-0b2f-312e-8fcf-a38e42555dd5 | -3.07052 | -54.24538 | 2026-10-08 05:23:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 9f293788-8e86-3190-9eee-3149dc92ff10 | -3.26729 | -54.04548 | 2026-10-08 05:23:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 276d6ce5-2531-34e1-af89-832acc330309 | -3.18441 | -60.05746 | 2026-10-08 05:23:00 | NPP-375D | IRANDUBA | AMAZONAS | Brasil | 1301852 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 5af120e6-8346-30aa-932d-93bf62672f0c | -3.29116 | -54.07716 | 2026-10-08 05:23:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 83fd0b7a-fe5d-3f64-8273-f781ebcf7a38 | -3.17652 | -50.59169 | 2026-10-08 05:23:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 9.2 |
| 1be3d3cc-923c-362f-9b50-d8f2bf18af64 | -2.49694 | -58.07352 | 2026-10-08 05:23:00 | NPP-375D | SÃO SEBASTIÃO DO UATUMÃ | AMAZONAS | Brasil | 1303957 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 71975f21-3ee4-3733-a6cf-e697a0518687 | -6.52069 | -55.27741 | 2026-10-08 05:23:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 8bf996fe-f6ca-397c-866a-00e63137b07a | -3.09211 | -58.0213 | 2026-10-08 05:23:00 | NPP-375D | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 368489e6-85ea-352e-9041-0aa3fc11563e | -4.45521 | -47.92444 | 2026-10-08 05:23:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| c1125f12-6093-3953-9d97-d87bdea18bcb | -3.48033 | -54.61993 | 2026-10-08 05:23:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| cbe33e0b-0028-3a32-9897-105c78041e9d | -2.75279 | -54.03766 | 2026-10-08 05:23:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 6b2a1325-d259-3183-afe6-d4fd9ff3382e | -3.18162 | -58.63924 | 2026-10-08 05:23:00 | NPP-375D | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 0b238884-9815-3a4d-a4e4-64addcebba98 | -3.54306 | -54.66369 | 2026-10-08 05:23:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 62d48428-7c11-33b4-b81d-248ff40c3bf7 | -4.15631 | -54.91565 | 2026-10-08 05:23:00 | NPP-375D | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 903daa5b-c5b2-37e6-8640-7f64a1b794d9 | -3.57094 | -54.35903 | 2026-10-08 05:23:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 206c949a-b4f5-31a4-9039-e79fbf8ea2db | -3.43994 | -56.93846 | 2026-10-08 05:23:00 | NPP-375D | BARREIRINHA | AMAZONAS | Brasil | 1300508 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 7d6b5da7-3c53-3f1a-9f05-009303639b88 | -3.01856 | -53.9529 | 2026-10-08 05:23:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 1e162a5f-44ca-3923-a244-a5fba27ff8c8 | -3.10175 | -53.92965 | 2026-10-08 05:23:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 4f0b9c26-27c2-3a6a-a688-7e330b9c8e0f | -3.01221 | -54.06386 | 2026-10-08 05:23:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 15.1 |
| ddc35c0b-754f-34e0-b056-b5b1528ac452 | -3.03168 | -53.91472 | 2026-10-08 05:23:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |


[Clique aqui para ver as próximas entradas](README165.md)
