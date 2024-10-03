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

## Dados Diários - Página 70

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| e93527fe-606b-395d-b71c-a7a86f085773 | -20.13833 | -43.84689 | 2024-10-03 03:38:00 | NOAA-20 | RIO ACIMA | MINAS GERAIS | Brasil | 3154804 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.2 |
| 299db238-9aec-36f8-b463-719429425cea | -20.13741 | -43.85157 | 2024-10-03 03:38:00 | NOAA-20 | RIO ACIMA | MINAS GERAIS | Brasil | 3154804 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.2 |
| bc9827a1-5b23-3a79-8875-cd01bb28b57c | -20.09403 | -43.28076 | 2024-10-03 03:38:00 | NOAA-20 | ALVINÓPOLIS | MINAS GERAIS | Brasil | 3102308 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| 6bfcbace-32a4-3a39-aef3-a5dea7461880 | -20.09313 | -43.28535 | 2024-10-03 03:38:00 | NOAA-20 | ALVINÓPOLIS | MINAS GERAIS | Brasil | 3102308 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| e035d5bb-119b-3ced-bab9-d7ff92fc063c | -20.07071 | -43.21617 | 2024-10-03 03:38:00 | NOAA-20 | ALVINÓPOLIS | MINAS GERAIS | Brasil | 3102308 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.1 |
| 7f93c117-f4c8-3328-9b3c-af4f76bd1104 | -20.06986 | -44.59419 | 2024-10-03 03:38:00 | NOAA-20 | ITAÚNA | MINAS GERAIS | Brasil | 3133808 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| 88431af2-fa21-30b2-a382-0604c1d6a79e | -20.06982 | -43.22067 | 2024-10-03 03:38:00 | NOAA-20 | ALVINÓPOLIS | MINAS GERAIS | Brasil | 3102308 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.1 |
| ba10d2a7-cb83-3167-b1f1-57de0526bc25 | -20.06639 | -43.21524 | 2024-10-03 03:38:00 | NOAA-20 | ALVINÓPOLIS | MINAS GERAIS | Brasil | 3102308 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| 384989d7-c30c-339a-9020-ea0bb82581a8 | -20.06489 | -43.21697 | 2024-10-03 03:38:00 | NOAA-20 | ALVINÓPOLIS | MINAS GERAIS | Brasil | 3102308 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 34ff33f7-985b-3e89-a30c-4dcac4cde6e6 | -20.01995 | -44.52609 | 2024-10-03 03:38:00 | NOAA-20 | ITAÚNA | MINAS GERAIS | Brasil | 3133808 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.4 |
| 607a9869-e481-3134-9027-10ca3f44b903 | -20.01891 | -44.53113 | 2024-10-03 03:38:00 | NOAA-20 | ITAÚNA | MINAS GERAIS | Brasil | 3133808 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| 58fd3436-bef3-3472-bff5-a52305bc0de9 | -20.01839 | -44.50989 | 2024-10-03 03:38:00 | NOAA-20 | ITAÚNA | MINAS GERAIS | Brasil | 3133808 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.5 |
| f0d2d86d-a10f-328c-9d08-2a76b1f5130e | -20.01736 | -44.5149 | 2024-10-03 03:38:00 | NOAA-20 | ITAÚNA | MINAS GERAIS | Brasil | 3133808 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.5 |
| 8989c525-de44-3002-94c9-18d436f25b17 | -20.01642 | -44.51307 | 2024-10-03 03:38:00 | NOAA-20 | ITAÚNA | MINAS GERAIS | Brasil | 3133808 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.7 |
| 054e85ff-a30d-304d-af93-6e4acd904b48 | -20.01542 | -44.51807 | 2024-10-03 03:38:00 | NOAA-20 | ITAÚNA | MINAS GERAIS | Brasil | 3133808 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.7 |
| 635aa406-5ba5-388c-b20a-857f3af58350 | -20.01378 | -44.5085 | 2024-10-03 03:38:00 | NOAA-20 | ITAÚNA | MINAS GERAIS | Brasil | 3133808 | 31 | 33 | nan | nan | nan | Mata Atlântica | 4.3 |
| cdbb745e-299a-32b0-bf5b-a6c5618a78ee | -20.0128 | -44.50667 | 2024-10-03 03:38:00 | NOAA-20 | ITAÚNA | MINAS GERAIS | Brasil | 3133808 | 31 | 33 | nan | nan | nan | Mata Atlântica | 6.7 |
| 73a397e2-e917-39aa-99ca-a81a03fceeda | -20.01275 | -44.51349 | 2024-10-03 03:38:00 | NOAA-20 | ITAÚNA | MINAS GERAIS | Brasil | 3133808 | 31 | 33 | nan | nan | nan | Mata Atlântica | 4.3 |
| a687a5fa-132a-3b9d-96dd-effc8742f47b | -20.0118 | -44.51168 | 2024-10-03 03:38:00 | NOAA-20 | ITAÚNA | MINAS GERAIS | Brasil | 3133808 | 31 | 33 | nan | nan | nan | Mata Atlântica | 5.2 |
| 20bcbc68-1f17-3479-b9b4-9f3c6862003d | -20.01019 | -44.50222 | 2024-10-03 03:38:00 | NOAA-20 | ITAÚNA | MINAS GERAIS | Brasil | 3133808 | 31 | 33 | nan | nan | nan | Mata Atlântica | 5.8 |
| 24a80bd7-55da-34b7-85e8-8c60728e3ae9 | -20.00915 | -44.50722 | 2024-10-03 03:38:00 | NOAA-20 | ITAÚNA | MINAS GERAIS | Brasil | 3133808 | 31 | 33 | nan | nan | nan | Mata Atlântica | 4.3 |
| 64b18fd1-afac-3b52-a3e8-05fd36974550 | -20.00816 | -44.50542 | 2024-10-03 03:38:00 | NOAA-20 | ITAÚNA | MINAS GERAIS | Brasil | 3133808 | 31 | 33 | nan | nan | nan | Mata Atlântica | 6.7 |
| 51830db1-57eb-36d1-be99-9bcd60f4be89 | -20.00812 | -44.51219 | 2024-10-03 03:38:00 | NOAA-20 | ITAÚNA | MINAS GERAIS | Brasil | 3133808 | 31 | 33 | nan | nan | nan | Mata Atlântica | 4.3 |
| ceffd38b-435b-39c2-a123-e8f414a6e07c | -20.00716 | -44.5104 | 2024-10-03 03:38:00 | NOAA-20 | ITAÚNA | MINAS GERAIS | Brasil | 3133808 | 31 | 33 | nan | nan | nan | Mata Atlântica | 5.2 |
| 8b2ae219-6035-3fa7-8f8d-a3830f2cc1fa | -19.98897 | -43.14561 | 2024-10-03 03:38:00 | NOAA-20 | RIO PIRACICABA | MINAS GERAIS | Brasil | 3155702 | 31 | 33 | nan | nan | nan | Mata Atlântica | 6.5 |
| 12d90ced-f270-334f-bdc6-f8b9b44e0c9b | -19.89314 | -41.40351 | 2024-10-03 03:38:00 | NOAA-20 | MUTUM | MINAS GERAIS | Brasil | 3144003 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.8 |
| 9a3bb914-9bc8-31d1-911a-ea4d42fb8d7a | -19.8922 | -41.40857 | 2024-10-03 03:38:00 | NOAA-20 | MUTUM | MINAS GERAIS | Brasil | 3144003 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.8 |
| d237566a-38ac-379f-b30b-41dc4fa05c5f | -19.88921 | -41.40296 | 2024-10-03 03:38:00 | NOAA-20 | MUTUM | MINAS GERAIS | Brasil | 3144003 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.8 |
| 826f9072-7df6-31f2-b315-e2e859f7692d | -19.88827 | -41.40804 | 2024-10-03 03:38:00 | NOAA-20 | MUTUM | MINAS GERAIS | Brasil | 3144003 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.8 |
| 193210d0-20b8-36a8-b17f-d430f7ac97f6 | -19.88659 | -42.11007 | 2024-10-03 03:38:00 | NOAA-20 | SANTA RITA DE MINAS | MINAS GERAIS | Brasil | 3159357 | 31 | 33 | nan | nan | nan | Mata Atlântica | 14.0 |
| 4abcb04e-750e-3fe7-8b97-22f3a29ccc05 | -19.8858 | -42.1143 | 2024-10-03 03:38:00 | NOAA-20 | SANTA RITA DE MINAS | MINAS GERAIS | Brasil | 3159357 | 31 | 33 | nan | nan | nan | Mata Atlântica | 7.1 |
| 989eb8ea-4042-3279-adba-34e390b3036c | -19.88334 | -42.10503 | 2024-10-03 03:38:00 | NOAA-20 | SANTA RITA DE MINAS | MINAS GERAIS | Brasil | 3159357 | 31 | 33 | nan | nan | nan | Mata Atlântica | 14.0 |
| 3eea7575-5fbf-3320-9d34-fb2cc30d2caf | -19.88253 | -42.10931 | 2024-10-03 03:38:00 | NOAA-20 | SANTA RITA DE MINAS | MINAS GERAIS | Brasil | 3159357 | 31 | 33 | nan | nan | nan | Mata Atlântica | 14.0 |
| 6a72954d-aa24-3f48-ad0f-c435e00f442e | -19.87451 | -43.14919 | 2024-10-03 03:38:00 | NOAA-20 | JOÃO MONLEVADE | MINAS GERAIS | Brasil | 3136207 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.3 |
| 17429c03-c5d9-32e5-8101-a9aac95c6f13 | -19.87206 | -43.16167 | 2024-10-03 03:38:00 | NOAA-20 | JOÃO MONLEVADE | MINAS GERAIS | Brasil | 3136207 | 31 | 33 | nan | nan | nan | Mata Atlântica | 4.0 |
| 39635a4d-5ae3-3bfc-a594-b2b92038239c | -19.87125 | -43.16576 | 2024-10-03 03:38:00 | NOAA-20 | JOÃO MONLEVADE | MINAS GERAIS | Brasil | 3136207 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.0 |
| 32ee2f53-1d47-32e9-a5b8-4d99943e0eac | -19.86781 | -43.16042 | 2024-10-03 03:38:00 | NOAA-20 | JOÃO MONLEVADE | MINAS GERAIS | Brasil | 3136207 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.3 |
| 3dc3eb29-d41b-3674-bcd1-279ad5f829a0 | -19.86702 | -43.16442 | 2024-10-03 03:38:00 | NOAA-20 | JOÃO MONLEVADE | MINAS GERAIS | Brasil | 3136207 | 31 | 33 | nan | nan | nan | Mata Atlântica | 4.5 |
| 15374deb-b983-3fd8-8478-d65ff0668d4a | -19.85796 | -42.37447 | 2024-10-03 03:38:00 | NOAA-20 | CÓRREGO NOVO | MINAS GERAIS | Brasil | 3120003 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.9 |
| baf7d24a-cc66-3590-afd9-8eac378de821 | -19.85391 | -42.3733 | 2024-10-03 03:38:00 | NOAA-20 | CÓRREGO NOVO | MINAS GERAIS | Brasil | 3120003 | 31 | 33 | nan | nan | nan | Mata Atlântica | 4.6 |
| fa5b5ea2-e956-36eb-97e7-1a14bccfa76d | -19.81353 | -43.83476 | 2024-10-03 03:38:00 | NOAA-20 | SANTA LUZIA | MINAS GERAIS | Brasil | 3157807 | 31 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 040b35d7-30eb-3573-afb2-8d25c22f3d7d | -19.81259 | -43.83957 | 2024-10-03 03:38:00 | NOAA-20 | SANTA LUZIA | MINAS GERAIS | Brasil | 3157807 | 31 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 1cf5a1fb-0607-3491-9fc6-bcef5fa978e5 | -19.80902 | -43.83377 | 2024-10-03 03:38:00 | NOAA-20 | SANTA LUZIA | MINAS GERAIS | Brasil | 3157807 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| fe26ca6c-89fd-3537-a06d-9ada8a1e8897 | -19.79633 | -43.63754 | 2024-10-03 03:38:00 | NOAA-20 | CAETÉ | MINAS GERAIS | Brasil | 3110004 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 04023427-dc0e-3c1b-931c-ad092b3f74e0 | -19.79536 | -43.64241 | 2024-10-03 03:38:00 | NOAA-20 | CAETÉ | MINAS GERAIS | Brasil | 3110004 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| a8645788-33a9-3d2c-98fe-dbd22ec312f1 | -19.79187 | -45.01346 | 2024-10-03 03:38:00 | NOAA-20 | NOVA SERRANA | MINAS GERAIS | Brasil | 3145208 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 845b753d-7903-379c-802d-545ab9a12ba8 | -19.79179 | -43.63698 | 2024-10-03 03:38:00 | NOAA-20 | CAETÉ | MINAS GERAIS | Brasil | 3110004 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 02348cd7-9871-3085-82ae-572fcae1fc9a | -19.7908 | -43.64197 | 2024-10-03 03:38:00 | NOAA-20 | CAETÉ | MINAS GERAIS | Brasil | 3110004 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 98c18a0b-d1f1-31d7-ae92-bec002e3f28d | -19.787 | -45.01244 | 2024-10-03 03:38:00 | NOAA-20 | NOVA SERRANA | MINAS GERAIS | Brasil | 3145208 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 901c53fe-78ee-3fcf-9640-9fe165bb4f10 | -19.7667 | -43.63527 | 2024-10-03 03:38:00 | NOAA-20 | CAETÉ | MINAS GERAIS | Brasil | 3110004 | 31 | 33 | nan | nan | nan | Cerrado | 2.3 |
| f7c0cf51-49d8-3be0-832a-71cdbff595e6 | -19.76396 | -43.63685 | 2024-10-03 03:38:00 | NOAA-20 | CAETÉ | MINAS GERAIS | Brasil | 3110004 | 31 | 33 | nan | nan | nan | Cerrado | 2.2 |
| cc992f4d-4dfd-3c4d-8d2b-02eef20c18cf | -19.75692 | -44.2592 | 2024-10-03 03:38:00 | NOAA-20 | ESMERALDAS | MINAS GERAIS | Brasil | 3124104 | 31 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 7d3b3036-a749-3b91-97e4-c037a9209a8c | -19.7545 | -44.25754 | 2024-10-03 03:38:00 | NOAA-20 | ESMERALDAS | MINAS GERAIS | Brasil | 3124104 | 31 | 33 | nan | nan | nan | Cerrado | 7.6 |
| d7acf1f0-ba8d-3de3-91a2-880781a6a109 | -19.75355 | -44.26239 | 2024-10-03 03:38:00 | NOAA-20 | ESMERALDAS | MINAS GERAIS | Brasil | 3124104 | 31 | 33 | nan | nan | nan | Cerrado | 7.6 |
| 963b06a3-8ca0-3c5b-a2a9-46814517852c | -19.75231 | -44.25805 | 2024-10-03 03:38:00 | NOAA-20 | ESMERALDAS | MINAS GERAIS | Brasil | 3124104 | 31 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 0452dda5-ff52-38eb-bca4-e6243ab444a7 | -19.75091 | -44.2512 | 2024-10-03 03:38:00 | NOAA-20 | ESMERALDAS | MINAS GERAIS | Brasil | 3124104 | 31 | 33 | nan | nan | nan | Cerrado | 1.8 |
| e2c70acc-674f-3a25-af67-43424ca384cb | -19.74889 | -44.26147 | 2024-10-03 03:38:00 | NOAA-20 | ESMERALDAS | MINAS GERAIS | Brasil | 3124104 | 31 | 33 | nan | nan | nan | Cerrado | 7.6 |
| 62146a1d-3cd0-3f58-8975-d4f2b414e151 | -19.74876 | -44.25172 | 2024-10-03 03:38:00 | NOAA-20 | ESMERALDAS | MINAS GERAIS | Brasil | 3124104 | 31 | 33 | nan | nan | nan | Cerrado | 3.3 |
| dc82b2a9-4eb1-3f44-a2dc-47a967633a5a | -19.74787 | -44.2667 | 2024-10-03 03:38:00 | NOAA-20 | ESMERALDAS | MINAS GERAIS | Brasil | 3124104 | 31 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 05aaf177-b6e5-362d-b6a0-a4ebb3a2e2fe | -19.74771 | -44.25688 | 2024-10-03 03:38:00 | NOAA-20 | ESMERALDAS | MINAS GERAIS | Brasil | 3124104 | 31 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 3dbac16c-5563-31b7-b66e-ddb437787991 | -19.74664 | -44.26214 | 2024-10-03 03:38:00 | NOAA-20 | ESMERALDAS | MINAS GERAIS | Brasil | 3124104 | 31 | 33 | nan | nan | nan | Cerrado | 11.0 |
| 7778fc79-a465-341f-9421-2bf0854facb5 | -19.74607 | -41.67309 | 2024-10-03 03:38:00 | NOAA-20 | TAPARUBA | MINAS GERAIS | Brasil | 3168051 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.1 |
| 894515ff-56dc-3049-a5ce-e292d9f9e55b | -19.74556 | -44.26738 | 2024-10-03 03:38:00 | NOAA-20 | ESMERALDAS | MINAS GERAIS | Brasil | 3124104 | 31 | 33 | nan | nan | nan | Cerrado | 11.0 |
| cf3d9ab9-91fd-32cb-b93c-bc122def2c07 | -19.74425 | -44.2605 | 2024-10-03 03:38:00 | NOAA-20 | ESMERALDAS | MINAS GERAIS | Brasil | 3124104 | 31 | 33 | nan | nan | nan | Cerrado | 4.3 |
| cefb0b58-dfbc-3c5d-9f0d-d8309ae86a49 | -19.74321 | -44.2658 | 2024-10-03 03:38:00 | NOAA-20 | ESMERALDAS | MINAS GERAIS | Brasil | 3124104 | 31 | 33 | nan | nan | nan | Cerrado | 11.4 |
| fcfbc3e8-4cbe-35ec-b861-1ebf3869c84e | -19.74198 | -44.26122 | 2024-10-03 03:38:00 | NOAA-20 | ESMERALDAS | MINAS GERAIS | Brasil | 3124104 | 31 | 33 | nan | nan | nan | Cerrado | 11.0 |
| 468c4587-6eda-3bbd-abb6-5927d4d4fc03 | -19.74115 | -40.67829 | 2024-10-03 03:38:00 | NOAA-20 | SÃO ROQUE DO CANAÃ | ESPÍRITO SANTO | Brasil | 3204955 | 32 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 510fd641-0e1b-383b-837b-c353eeff71ac | -19.7409 | -44.26648 | 2024-10-03 03:38:00 | NOAA-20 | ESMERALDAS | MINAS GERAIS | Brasil | 3124104 | 31 | 33 | nan | nan | nan | Cerrado | 11.0 |
| 1c0ea7a0-d46b-3af5-be9f-4afab87fff5a | -19.7396 | -44.25957 | 2024-10-03 03:38:00 | NOAA-20 | ESMERALDAS | MINAS GERAIS | Brasil | 3124104 | 31 | 33 | nan | nan | nan | Cerrado | 4.3 |
| a383963a-6d1c-3b4d-88f8-5ffb682a47bc | -19.7395 | -44.24968 | 2024-10-03 03:38:00 | NOAA-20 | ESMERALDAS | MINAS GERAIS | Brasil | 3124104 | 31 | 33 | nan | nan | nan | Cerrado | 7.2 |
| 91cc23c4-588e-3a95-80c1-64d3906dc51c | -19.73855 | -44.26487 | 2024-10-03 03:38:00 | NOAA-20 | ESMERALDAS | MINAS GERAIS | Brasil | 3124104 | 31 | 33 | nan | nan | nan | Cerrado | 11.4 |
| d46cc124-af63-3af5-bee1-3507a3e927c7 | -19.7374 | -40.67762 | 2024-10-03 03:38:00 | NOAA-20 | SÃO ROQUE DO CANAÃ | ESPÍRITO SANTO | Brasil | 3204955 | 32 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| cbbc0192-a3ad-3ef8-a7cf-989cfa1b2251 | -19.73706 | -44.24794 | 2024-10-03 03:38:00 | NOAA-20 | ESMERALDAS | MINAS GERAIS | Brasil | 3124104 | 31 | 33 | nan | nan | nan | Cerrado | 5.0 |
| b758412c-84ee-33d9-b188-57f1b1351062 | -19.73602 | -44.25318 | 2024-10-03 03:38:00 | NOAA-20 | ESMERALDAS | MINAS GERAIS | Brasil | 3124104 | 31 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 209355bf-85d7-3130-af22-73ec64ce917f | -19.72302 | -45.07607 | 2024-10-03 03:38:00 | NOAA-20 | LEANDRO FERREIRA | MINAS GERAIS | Brasil | 3138302 | 31 | 33 | nan | nan | nan | Cerrado | 2.5 |
| a21c68d0-ae90-3661-bed5-d9766fba85bd | -19.72109 | -44.15837 | 2024-10-03 03:38:00 | NOAA-20 | ESMERALDAS | MINAS GERAIS | Brasil | 3124104 | 31 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 6e2a4878-5d5c-3531-a1a3-31ef3d7442f4 | -19.71817 | -45.07483 | 2024-10-03 03:38:00 | NOAA-20 | LEANDRO FERREIRA | MINAS GERAIS | Brasil | 3138302 | 31 | 33 | nan | nan | nan | Cerrado | 7.7 |
| 7d84280d-b926-3ddf-aa34-e4897f599a54 | -19.71683 | -40.35224 | 2024-10-03 03:38:00 | NOAA-20 | JOÃO NEIVA | ESPÍRITO SANTO | Brasil | 3203130 | 32 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 5178e3a3-4b26-3e60-842b-99c7d98756c4 | -19.69036 | -42.0379 | 2024-10-03 03:38:00 | NOAA-20 | UBAPORANGA | MINAS GERAIS | Brasil | 3170057 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.9 |
| 7f3708b1-f572-38c2-bf60-1caadd148a14 | -19.68629 | -42.03724 | 2024-10-03 03:38:00 | NOAA-20 | UBAPORANGA | MINAS GERAIS | Brasil | 3170057 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.9 |
| 2df1518c-1ce6-3437-85d0-ff59bc338fa3 | -19.68224 | -42.03646 | 2024-10-03 03:38:00 | NOAA-20 | UBAPORANGA | MINAS GERAIS | Brasil | 3170057 | 31 | 33 | nan | nan | nan | Mata Atlântica | 7.8 |
| 490ee35b-7a82-355c-a762-def2b49cf458 | -19.67746 | -42.92711 | 2024-10-03 03:38:00 | NOAA-20 | ANTÔNIO DIAS | MINAS GERAIS | Brasil | 3103009 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 6ec1c881-f680-30fa-92c2-af5f674bcd75 | -19.62011 | -47.17297 | 2024-10-03 03:38:00 | NOAA-20 | ARAXÁ | MINAS GERAIS | Brasil | 3104007 | 31 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 4fd33ed2-0623-310c-9784-e2d67b9ab4e5 | -19.61927 | -47.17681 | 2024-10-03 03:38:00 | NOAA-20 | ARAXÁ | MINAS GERAIS | Brasil | 3104007 | 31 | 33 | nan | nan | nan | Cerrado | 3.2 |
| e60c3082-0dd5-3718-94d1-fded96900be3 | -19.52539 | -44.25249 | 2024-10-03 03:38:00 | NOAA-20 | SETE LAGOAS | MINAS GERAIS | Brasil | 3167202 | 31 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 540dd546-cc82-31a6-b60b-64ef8ae67d01 | -19.52258 | -44.25495 | 2024-10-03 03:38:00 | NOAA-20 | SETE LAGOAS | MINAS GERAIS | Brasil | 3167202 | 31 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 4010e77b-c0a6-32bf-b511-6772fcfb98b2 | -19.50626 | -42.86772 | 2024-10-03 03:38:00 | NOAA-20 | ANTÔNIO DIAS | MINAS GERAIS | Brasil | 3103009 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.9 |
| 860efb59-13e8-30d9-95d7-bcff6c8f43ca | -19.50548 | -42.87172 | 2024-10-03 03:38:00 | NOAA-20 | ANTÔNIO DIAS | MINAS GERAIS | Brasil | 3103009 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.9 |
| 5dde18be-c01a-3402-9595-4af8a449450f | -19.50238 | -42.88771 | 2024-10-03 03:38:00 | NOAA-20 | ANTÔNIO DIAS | MINAS GERAIS | Brasil | 3103009 | 31 | 33 | nan | nan | nan | Mata Atlântica | 8.2 |
| 595b197b-0ae1-3ddd-8f95-ff2e13197fbf | -19.50219 | -42.32207 | 2024-10-03 03:38:00 | NOAA-20 | CARATINGA | MINAS GERAIS | Brasil | 3113404 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 38f930b4-b5df-378e-ae8a-bef7e059b8a4 | -19.50142 | -42.89262 | 2024-10-03 03:38:00 | NOAA-20 | ANTÔNIO DIAS | MINAS GERAIS | Brasil | 3103009 | 31 | 33 | nan | nan | nan | Mata Atlântica | 16.8 |
| 42cff159-3a36-370f-a61f-8d15a5e85c5c | -19.50134 | -42.3265 | 2024-10-03 03:38:00 | NOAA-20 | CARATINGA | MINAS GERAIS | Brasil | 3113404 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| ab3e1e26-e98c-3d47-a43e-b0ffe749ea34 | -19.50123 | -42.87074 | 2024-10-03 03:38:00 | NOAA-20 | ANTÔNIO DIAS | MINAS GERAIS | Brasil | 3103009 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.9 |
| 269166c3-c53f-3a00-9d53-3598f148ddc8 | -19.50052 | -42.8744 | 2024-10-03 03:38:00 | NOAA-20 | ANTÔNIO DIAS | MINAS GERAIS | Brasil | 3103009 | 31 | 33 | nan | nan | nan | Mata Atlântica | 4.5 |
| 13cf784c-8b5a-3e80-9797-218c0e6c0fb0 | -19.50049 | -42.33096 | 2024-10-03 03:38:00 | NOAA-20 | CARATINGA | MINAS GERAIS | Brasil | 3113404 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| 6765c8fb-e725-3cf5-a548-3cdd30dc17cc | -19.49983 | -42.87795 | 2024-10-03 03:38:00 | NOAA-20 | ANTÔNIO DIAS | MINAS GERAIS | Brasil | 3103009 | 31 | 33 | nan | nan | nan | Mata Atlântica | 4.5 |
| cf44d831-cac6-3ae0-b4ce-559bcbc5dc3f | -19.49905 | -42.88194 | 2024-10-03 03:38:00 | NOAA-20 | ANTÔNIO DIAS | MINAS GERAIS | Brasil | 3103009 | 31 | 33 | nan | nan | nan | Mata Atlântica | 8.2 |
| f428f111-594b-313f-b9d2-f67094bd8fb9 | -19.49817 | -42.88648 | 2024-10-03 03:38:00 | NOAA-20 | ANTÔNIO DIAS | MINAS GERAIS | Brasil | 3103009 | 31 | 33 | nan | nan | nan | Mata Atlântica | 8.2 |
| fedd4519-e197-3d14-84df-948ecd7c7383 | -19.49808 | -42.32114 | 2024-10-03 03:38:00 | NOAA-20 | CARATINGA | MINAS GERAIS | Brasil | 3113404 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 10ab8475-4d0b-3690-8d88-2c3c02461b20 | -19.49561 | -42.87679 | 2024-10-03 03:38:00 | NOAA-20 | ANTÔNIO DIAS | MINAS GERAIS | Brasil | 3103009 | 31 | 33 | nan | nan | nan | Mata Atlântica | 29.2 |


[Clique aqui para ver as próximas entradas](README71.md)
